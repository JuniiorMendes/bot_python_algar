from tkinter import *
from tkinter import ttk
from MicroSIP_lib.MicroSIP import *
from time import sleep

import re

number_pattern = r"^\d{1,12}$"

def main():
    root = Tk()

    ramal = StringVar()

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Entre com o ramal ou numero de telefone: ").grid(column=0, row=0)
    dadosEntry = ttk.Entry(frm, textvariable=ramal)
    dadosEntry.grid(column=1, row=0)
    ttk.Button(frm, text="Start", command = root.destroy).grid(column=2, row=0)
    root.mainloop()

    ramal.set(str(re.findall(number_pattern, str(ramal.get()))[0]))

    if(len(str(ramal.get())) == 0):
        print("exitting...")
        exit()

    press("super")
    sleep(2)
    typewrite("microsip", interval=0.5)
    press("enter")
    sleep(2)

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

    moveTo(centerx, centery - (5 * 30) * percent_height, duration=1)
    click()

    hotkey("ctrl", "a")
    press("delete")

    if(len(str(ramal.get())) == 11):
        ramal.set("09" + str(ramal.get()))

    typewrite(str(ramal.get()), interval=0.5)

    press("enter")

if __name__ == "__main__":
    main()

