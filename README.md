(English)
# 📸 ImageCollector

ImageCollector is a Flask-based web application that allows capturing images from IP cameras, displaying them in Single Time or Real Time modes, and optionally downloading them all as a ZIP archive.
Currently supports Dahua and Oinone brand cameras.

---

🔒 Connect to IP cameras (with username & password)

📷 Capture images once or in real-time mode

💾 Save images in the Images/ directory

📦 Download all captured images as a ZIP archive

🧼 Automatically delete old images (default: after 5 minutes)

## 🛠️ Installation

🔹 1. Clone the Repository

git clone https://github.com/SelinBeyazzz/Image-Collector.git
cd Image-Collector


🔹 2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate  # (Linux/macOS: source venv/bin/activate)


🔹 3.  Install Dependencies
pip install -r requirements.txt


▶️ Start the Application
python app.py
Once the app is running, open your browser and go to:
👉 http://127.0.0.1:5000


🌐 Web Interface Features
Connect to the camera by entering IP, username, and password

Select the camera brand (Dahua or Oinone)

Choose between two modes:

🖼️ Single Shot: Captures one image

📡 Real Time: Captures an image every second

View captured images directly on the interface

Use the "Download as ZIP" button to download all saved images


📁 Project Structure
ImageCollector/
├── app.py                  # Flask server code
├── requirements.txt        # Required Python packages
├── static/
│   ├── style.css           # UI styles
│   └── script.js           # JavaScript for camera control
├── templates/
│   └── index.html          # Main HTML UI
├── Images/                 # Folder to store captured images
└── README.md               # This documentation file


📤 Remote Camera Access Notes
Ensure the IP address and login credentials are correct

The camera should be on the local network or publicly accessible

Network latency may cause delays in Real Time mode

Oinone cameras return images directly via HTTP

Dahua cameras are accessed using OpenCV streaming



🧹 Automatic Cleanup
Captured images in the Images/ folder are automatically deleted after 5 minutes.
You can modify this duration in the delete_old_images() function in app.py by changing the seconds=300 value.



🧑‍💻 Contributing
Want to contribute? Here's how:

Fork the repository

Create a new branch: feature/your-feature-name

Make your changes

Submit a Pull Request


📄 License
This project is open source and licensed under the MIT License.


🙋‍♀️ Developer
Selin Beyaz
GitHub: @SelinBeyazzz


---------------------------------------------------------------------------------------------

(Turkish)
# 📸 ImageCollector

**ImageCollector**, IP kameralar üzerinden görüntü yakalayabilen, bu görüntüleri **Single Time** veya **Real Time** gösteren ve istenirse topluca **ZIP** olarak indirilebilen bir **Flask tabanlı web uygulamasıdır**.  
Şu an **Dahua** ve **Oinone** marka kameraları desteklemektedir.

---

## 🚀 Özellikler

- 🔒 IP kamera bağlantısı (kullanıcı adı & şifre ile)
- 📷 Tek seferlik veya sürekli fotoğraf çekimi (Real-time mod)
- 💾 Görüntüleri `Images/` klasöründe saklama
- 📦 ZIP olarak tüm görüntüleri indirme
- 🧼 Eski görüntüleri otomatik temizleme (varsayılan: 5 dakika)

---

## 🛠️ Kurulum

🔹 1. Projeyi Klonlayın

git clone https://github.com/SelinBeyazzz/Image-Collector.git
cd Image-Collector


🔹 2. Sanal Ortam Oluşturun
python -m venv venv
venv\Scripts\activate  # (Linux/macOS: source venv/bin/activate)


🔹 3. Gereksinimleri Yükleyin
pip install -r requirements.txt


▶️ Uygulamayı Başlat
python app.py
Uygulama çalıştığında tarayıcınızdan şu adrese gidin:
👉 http://127.0.0.1:5000


🌐 Arayüz Özellikleri
IP, kullanıcı adı ve şifre girerek kameraya bağlanabilirsiniz.

Kamera markasını seçebilirsiniz (Dahua veya Oinone).

Mod seçimi yapılabilir:

🖼️ Single Shot: Tek fotoğraf alır

📡 Real Time: Her saniye fotoğraf alır

Görüntüyü canlı olarak ekranda izleyebilirsiniz.

"Download as ZIP" butonuyla tüm görüntüleri tek seferde indirebilirsiniz.


📁 Proje Yapısı
ImageCollector/
├── app.py                  # Flask sunucu kodu
├── requirements.txt        # Gerekli Python kütüphaneleri
├── static/
│   ├── style.css           # Arayüz tasarımı
│   └── script.js           # JavaScript ile kamera kontrolü
├── templates/
│   └── index.html          # Ana HTML arayüz
├── Images/                 # Yakalanan görüntülerin saklandığı klasör
└── README.md               # Bu dökümantasyon dosyası


📤 Uzak Kamera Erişimi Notları
Kamera IP’si ve giriş bilgileri doğru olmalıdır.

Kamera, yerel ağda veya dışarıdan erişilebilir bir IP adresine sahip olmalıdır.

Real Time modda ağ yavaşsa gecikmeler yaşanabilir.

Oinone kameraları HTTP üzerinden doğrudan görsel döndürür.

Dahua kameralar için OpenCV ile bağlantı sağlanır.


🧹 Otomatik Temizlik
Images/ klasöründeki görüntüler, uygulama tarafından otomatik olarak 5 dakika sonra silinir.
Bu süreyi app.py içindeki delete_old_images() fonksiyonundaki seconds=300 değerini değiştirerek ayarlayabilirsiniz.


🧑‍💻 Katkıda Bulunmak
Katkı sağlamak isterseniz:

Reponun bir kopyasını fork'layın

Yeni bir dal (branch) oluşturun: feature/yenilik

Değişikliklerinizi yapın

Pull Request gönderin


📄 Lisans
Bu proje açık kaynaklıdır ve MIT Lisansı ile lisanslanmıştır.


🙋‍♀️ Geliştirici
Selin Beyaz
GitHub: @SelinBeyazzz

