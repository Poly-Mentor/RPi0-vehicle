from flask import Flask, Response
from picamera2 import Picamera2
import time

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration())
picam2.start()

@app.route('/')
def index():
    # Return an HTML page with an embedded MJPEG stream
    return """
    <html><body>
    <h1>Raspberry Pi Camera Stream</h1>
    <img src="/stream.mjpg" width="640" height="480" />
    </body></html>
    """

def gen_frames():
    while True:
        frame = picam2.capture_array()
        # Convert raw NumPy frame to JPEG in-memory
        import cv2
        import threading
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        jpg_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n')
        time.sleep(0.05)  # ~20 FPS

@app.route('/stream.mjpg')
def stream():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Listen on all interfaces, e.g. port 8080
    app.run(host='0.0.0.0', port=8080, debug=False)

