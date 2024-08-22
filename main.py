import os

from pyautogui import *
from pygetwindow import *

class Microsip:
    def __init__(self):
        self._program: Win32Window = getWindowsWithTitle("MicroSIP")[0]
    
    def get_size(self):
        return (self._program.size.width, self._program.size.height)

    def get_position(self):
        return (self._program.top, self._program.left)


def main() -> None:
    return None

if __name__ == "__main__":
    main()