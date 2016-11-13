# Embedded file name: /home/pi/project/catFood/src/capture.py
import picamera as _picamera
from PIL import Image
from io import BytesIO
import time as _time
import os as _os

class Capturerer:
    """ Tool to capture a still image from raspberry pi camera module"""

    def __init__(self):
        self._stream = BytesIO()
        self._camera = _picamera.PiCamera()
        self._data_root = '../data'

    def capture(self):
        """ Caputer a still image, return a PIL.Image"""
        self._camera.capture(self._stream, format='png')
        self._stream.seek(0)
        return Image.open(self._stream)

    def capture_n_save(self, file_name):
        """ Capture and save still image"""
        img = self.capture()
        img.save(file_name)

    def caputre_n_save_avec_timestamp(self):
        """capture and save file with time stamp
        Return the file name"""
        file_name = _os.path.join(self._data_root, _time.strftime('%Y%m%d-%H%M%S') + '.png')
        self._camera.capture(file_name)
        return file_name

    def capture_video_avec_timestamp(self, length, resolution = (640, 480)):
        """ Capture `length` seconds of video and save to `file_name`"""
        file_name = _os.path.join(self._data_root, _time.strftime('%Y%m%d-%H%M%S') + '.h264')
        self._camera.resolution = resolution
        self._camera.start_recording(file_name)
        self._camera.wait_recording(length)
        self._camera.stop_recording()
        return self._convert_h264_2_mp4(file_name)

    def _convert_h264_2_mp4(self, file_name):
        """ Convert file to mp4, return the file name"""
        output = file_name.replace('.h264', '.mp4')
        cmd = 'MP4Box -add ' + file_name + ' ' + output
        _os.system(cmd)
        _os.system('rm ' + file_name)
        return output


if __name__ == '__main__':
    c = Capturerer()
    print c.capture_video_avec_timestamp(5)