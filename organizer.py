import os
import shutil
import tkinter
from tkinter import *


def organizer():
    val = name.get()
    if val:
        files = os.listdir(val)

        for i in files:
            filename, extension = os.path.splitext(i)
            extension = extension[1:]
            if os.path.exists(val + "/" + extension):
                shutil.move(val + "/" + i, val + "/" + extension + "/" + i)
            else:
                os.makedirs(val + "/" + extension)
                shutil.move(val + "/" + i, val + "/" + extension + "/" + i)


# GUI
window = Tk()
window.geometry("350x250")
name = tkinter.Entry(window)
tkinter.Label(window, text="Directory").grid(row=0, column=0)
name.grid(row=0, column=1)
tkinter.Button(window, text="Submit", command=organizer).grid(row=0, column=0)
window.mainloop()
