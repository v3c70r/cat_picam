# Embedded file name: /home/pi/project/catFood/src/file_manager.py
import os as _os

class FileManager:
    """ Manage saved data files 
    Including delete, ls image, video and all files
    """

    def __init__(self):
        self._data_root = '../data'

    def list_images(self):
        files = self._find_files_with_extension('.png')
        if not files:
            return 'Empty'
        return '\n'.join(files)

    def list_videos(self):
        files = self._find_files_with_extension('.h264')
        if not files:
            return 'Empty'
        return '\n'.join(files)

    def list(self):
        files = [ f for f in _os.listdir(self._data_root) ]
        if not files:
            return 'Empty'
        return '\n'.join(files)

    def clear_videos(self):
        files = self._find_files_with_extension('.mp4')
        if not files:
            return 'No file to remove'
        for f in files:
            _os.remove(_os.path.join(self._data_root, f))

        return 'Removed \n' + '\n'.join(files)

    def clear_images(self):
        files = self._find_files_with_extension('.png')
        if not files:
            return 'No file to remove'
        for f in files:
            _os.remove(_os.path.join(self._data_root, f))

        return 'Removed \n' + '\n'.join(files)

    def clear(self):
        files = [ f for f in _os.listdir(self._data_root) ]
        if not files:
            return 'No file to remove'
        for f in files:
            _os.remove(_os.path.join(self._data_root, f))

        return 'Removed \n' + '\n'.join(files)

    def _find_files_with_extension(self, ext):
        return [ f for f in _os.listdir(self._data_root) if f.endswith(ext) ]


if __name__ == '__main__':
    fm = FileManager()
    print fm.list_videos()
    print '======'
    print fm.clear_videos()
    print '+===='
    print fm.list_videos()