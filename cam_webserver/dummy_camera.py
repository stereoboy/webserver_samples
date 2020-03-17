import time
import os
from base_camera import BaseCamera

class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    try:
        imgs = [open(os.path.join("../data/images/", f), 'rb').read() for f in ['000.jpg', '001.jpg', '002.jpg']]
    except Exception as e:
        print(e)

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            yield Camera.imgs[int(time.time()) % 3]
