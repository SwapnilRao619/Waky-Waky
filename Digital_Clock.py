import tkinter as ui
import time
import os
from tkinter import ttk

window = ui.Tk()
window.geometry("600x600")
window.title("Digital Clock")
def clock():
    hours=time.strftime("%I")
    minutes=time.strftime("%M")
    seconds=time.strftime("%S")
    ampm=time.strftime("%p")
    timetxt=f"{hours}:{minutes}:{seconds}:{ampm}"
    dc_label.config(text=timetxt)
    dc_label.after(1000, clock)
dc_label=ui.Label(window, text="00:00:00", font="Helvetica 50 bold")
dc_label.pack(pady=225)
def menu():
    window.destroy()
    os.system("python Clock_App.py")
def alarm():
    window.destroy()
    os.system("python Alarm.py")

ttk.Button(window, text="Menu Window",command=menu).pack()
ttk.Button(window, text="Set Alarm", command=alarm).pack()

clock()

window.mainloop()