import os

from pyautogui import *
from pygetwindow import *

class Microsip:
    def __init__(self):
        self.program: Win32Window = getWindowsWithTitle("MicroSIP")[0]
    
    def get_size(self):
        return (self.program.size.width, self.program.size.height)

    def get_position(self):
        return (self.program.top, self.program.left)

    def mouseMove(self):
        moveTo(20,10, duration=3)

    def localization(self, imgDir):
        return locateOnScreen(imgDir)

def main():
    micro = Microsip()
    micro.program.activate()
    local1 = micro.localization("img/captura01.PNG")
    moveTo(local1[0], local1[1], duration = 1)
    moveTo(local1[0], local1[1] - 25)
    click()
    typewrite("2688", interval = 0.5)

    try:
        local2 = micro.localization("img/captura02.PNG")
        moveTo(local2[0], local2[1], duration = 1)
        click()
    except Exception() as err:
        pass


if __name__ == "__main__":
    main()

