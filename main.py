from pyautogui import *
from pygetwindow import *

programsName = getAllTitles()

program = None

for name in programsName :
    if "MicroSIP" in name :
        program = getWindowsWithTitle(name)[0]

# left, top, _,_ = locateOnScreen("img/seta.png")
# moveTo(left, top, duration = 2)
# click()

program.activate()
hotkey("ctrl", "p")