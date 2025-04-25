document.addEventListener('DOMContentLoaded', function () {
    const captureBtn = document.getElementById('captureBtn');
    const capturedImage = document.getElementById('capturedImage');
    const placeholderText = document.getElementById('placeholderText');
    const singleRadio = document.getElementById('single');
    const realtimeRadio = document.getElementById('realtime');
    const dahuaRadio = document.getElementById('dahua');
    const oinoneRadio = document.getElementById('oinone');
    const ipInput = document.getElementById('cameraIpInput');

    let intervalId = null;

    function updateIpPlaceholder() {
        ipInput.value = '';
    }

    updateIpPlaceholder();

    dahuaRadio.addEventListener('change', updateIpPlaceholder);
    oinoneRadio.addEventListener('change', updateIpPlaceholder);

    function sendSnapshotRequest() {
        const cameraIp = document.getElementById('cameraIpInput').value.trim();
        const username = document.getElementById('usernameInput').value.trim();
        const password = document.getElementById('passwordInput').value.trim();
        const cameraBrand = document.querySelector('input[name="cameraBrand"]:checked').value;

        fetch('/fetch-camera-image', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                camera_ip: cameraIp,
                username: username,
                password: password,
                camera_brand: cameraBrand
            })
        })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    capturedImage.onload = function () {
                        adjustImageHeight();
                    };
                    capturedImage.src = data.image_url;
                    capturedImage.style.display = 'block';
                    placeholderText.style.display = 'none';
                } else {
                    alert("Error: " + data.message);
                }
            })
            .catch(err => {
                alert("Server error: " + err);
            });
    }


    captureBtn.addEventListener('click', function () {
        const mode = document.querySelector('input[name="mode"]:checked').value;

        if (mode === 'single') {
            if (intervalId) {
                clearInterval(intervalId);
                intervalId = null;
                captureBtn.textContent = 'Take Image';
            }
            sendSnapshotRequest();

        } else if (mode === 'realtime') {
            if (intervalId) {
                clearInterval(intervalId);
                intervalId = null;
                captureBtn.textContent = 'Take Image';
            } else {
                sendSnapshotRequest();
                intervalId = setInterval(sendSnapshotRequest, 1000);
                captureBtn.textContent = ' Stop';
            }
        }
    });

    function adjustImageHeight() {
        const headerHeight = document.querySelector('.top-input-container').offsetHeight;
        const windowHeight = window.innerHeight;
        const imageHeight = windowHeight - headerHeight;

        const capturedImage = document.getElementById('capturedImage');
        capturedImage.style.width = "100vw";
        capturedImage.style.height = `${imageHeight}px`;
        capturedImage.style.objectFit = "contain";
        capturedImage.style.display = "block";
    }

    window.addEventListener('resize', adjustImageHeight);
    document.addEventListener('DOMContentLoaded', adjustImageHeight);

});
