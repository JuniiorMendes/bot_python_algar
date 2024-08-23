import os

from MicroSIP_lib.MicroSIP import *

def main():
    micro = Microsip()
    micro.focus()

    btn1_left, btn1_top, _, _ = micro.locate("img/captura01.PNG")

    micro \
        .move_mouse(btn1_left, btn1_top) \
        .move_mouse(btn1_left, btn1_top - 25, mouse_click=True)

    typewrite("2688", interval = 0.1)

    try:
        btn2_left, btn2_top, _, _ = micro.localization("img/captura02.PNG")
        micro.move_mouse(btn2_left, btn2_top, mouse_click=False)
    except Exception() as err:
        pass

if __name__ == "__main__":
    main()

