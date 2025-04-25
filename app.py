from flask import Flask, render_template, request, jsonify, send_file
import os
import cv2
import base64
import time
import zipfile
import tempfile
import threading
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

IMAGE_FOLDER = "Images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-camera-image', methods=['POST'])
def fetch_camera_image():
    data = request.get_json()
    camera_ip = data.get("camera_ip")
    username = data.get("username")
    password = data.get("password")
    camera_brand = data.get("camera_brand")
    print(username,password)

    if not all([camera_ip, username, password, camera_brand]):
        return jsonify(success=False, message="Required fields are missing.")

    if camera_brand == "dahua":
        url = f"http://{username}:{password}@{camera_ip}/cgi-bin/snapshot.cgi?channel=1"
    elif camera_brand == "oinone":
        url = f"http://{username}:{password}@{camera_ip}/GetSnapshot/0"

    else:
        return jsonify(success=False, message="Unsupported camera brand.")
    
    print("URL:", url)
    print("Username:", username)
    print("Password:", password)
    
    try:
        if camera_brand == "oinone":
         
            res = requests.get(url, timeout=5)

            if res.status_code == 401:
                return jsonify(success=False, message="Incorrect username or password.")
            elif res.status_code != 200:
                return jsonify(success=False, message=f"Camera request failed. Status code: {res.status_code}")

            image_bytes = res.content

        else: 
            cap = cv2.VideoCapture(url)

            if not cap.isOpened():
                return jsonify(success=False, message="Failed to connect to camera using OpenCV.")

            ret, frame = cap.read()
            cap.release()

            if not ret or frame is None:
                return jsonify(success=False, message="Image could not be retrieved (frame is empty).")

            _, jpeg = cv2.imencode('.jpg', frame)
            image_bytes = jpeg.tobytes()

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}.jpg"
        filepath = os.path.join(IMAGE_FOLDER, filename)

        with open(filepath, "wb") as f:
            f.write(image_bytes)

        b64_data = base64.b64encode(image_bytes).decode('utf-8')
        data_url = f"data:image/jpeg;base64,{b64_data}"

        delete_old_images(IMAGE_FOLDER)

        return jsonify(success=True, image_url=data_url)

    except requests.exceptions.ConnectTimeout:
        return jsonify(success=False, message="Could not connect to the camera (timeout).")
    except requests.exceptions.ConnectionError:
        return jsonify(success=False, message="Failed to connect to the camera. Check the IP address.")
    except Exception as e:
        return jsonify(success=False, message=f"An unknown error occurred: {str(e)}")
    
@app.route('/download-zip')
def download_zip():
    delete_old_images(IMAGE_FOLDER)  
    temp_zip = tempfile.NamedTemporaryFile(delete=False, suffix='.zip')

    with zipfile.ZipFile(temp_zip.name, 'w') as zipf:
        for filename in os.listdir(IMAGE_FOLDER):
            filepath = os.path.join(IMAGE_FOLDER, filename)
            if os.path.isfile(filepath):
                zipf.write(filepath, arcname=filename)

    return send_file(temp_zip.name, as_attachment=True, download_name="Images.zip")

def delete_old_images(folder, seconds=300):
    def delete_task():
        now = time.time()
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                file_age = now - os.path.getmtime(filepath)
                if file_age > seconds:
                    os.remove(filepath)
                    print(f"Deleted: {filepath}")
    threading.Thread(target=delete_task).start()

if __name__ == '__main__':
    app.run(debug=True)