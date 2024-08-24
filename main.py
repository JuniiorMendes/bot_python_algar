import os

from MicroSIP_lib.MicroSIP import *

def main():
    program_name: str

    for name in getAllTitles():
        if "MicroSIP" in name:
            program_name = name

    microsip = Microsip(program_name)
    microsip.focus()

    width, height = microsip.get_size()
    left, top = microsip.get_position()

    centerx, centery = \
        microsip.program.center.x, \
        microsip.program.center.y

    percent_width = \
        width / microsip.fixed_size[0]

    percent_height = \
        height / microsip.fixed_size[1]

    moveTo(centerx, centery - (5 * 30) * percent_height)
    click()

    typewrite("2681")
    keyDown("enter")

if __name__ == "__main__":
    main()
