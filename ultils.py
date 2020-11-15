"""
Any utility functions that will be used everywhere
"""
import os
import sys


class Utils:
    @staticmethod
    def get_home_dir():
        platform = sys.platform
        path = os.getcwd()
        if platform.startswith('win'):
            folders = path.split('\\')
        else:
            folders = path.split('/')

        folders = folders[:folders.index('bostonhacks2020-21') + 1]
        return '/'.join(folders)

