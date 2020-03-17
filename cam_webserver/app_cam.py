from flask import Flask, render_template, Response

# Raspberry Pi camera module (requires picamera package, developed by Miguel Grinberg)
from dummy_camera import Camera
import os
import logging

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        #frame = camera.get_frame()
        app.logger.info("gen()")
        frame = camera.frames()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    try:
        imgs = [open(os.path.join("../data/images/", f), 'rb').read() for f in ['000.jpg', '001.jpg', '002.jpg']]
        app.logger.info("load succeed")
    except Exception as e:
        app.logger.error(e)

    #app.run(host='0.0.0.0', port =80, debug=True, threaded=True)
    app.run(host='0.0.0.0', debug=True, threaded=True)
