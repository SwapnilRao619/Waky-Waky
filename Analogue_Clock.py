import tkinter as ui
import time 
import math
from tkinter import ttk
import os

window = ui.Tk()
window.geometry("600x600")
window.title("Analogue Clock")
def clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    s_x = (shl * math.sin(math.radians(seconds * 6))) + cx
    s_y = (-1 * shl * math.cos(math.radians(seconds * 6))) + cy
    canvas.coords(sh, cx, cy, s_x, s_y)
    
    m_x = (mhl*math.sin(math.radians(minutes*6))) +cx
    m_y = (-1*mhl*math.cos(math.radians(minutes*6))) +cy 
    canvas.coords(mh,cx,cy,m_x,m_y)

    h_x = (hhl*math.sin(math.radians(hours*30))) +cx
    h_y = (-1*hhl*math.cos(math.radians(hours*30))) +cy 
    canvas.coords(hh,cx,cy,h_x,h_y)
    window.after(1000, clock)

canvas = ui.Canvas(window, width=400, height=400, bg="white")
canvas.pack(expand=True, fill='both')
bg = ui.PhotoImage(file='ac.png')
canvas.create_image(300, 300, image=bg)
cx = 300
cy = 300
shl = 130
mhl = 110
hhl = 65
sh = canvas.create_line(300, 300, 300 + shl, 300+shl, width=2, fill='red')
mh = canvas.create_line(300, 300, 300 + mhl, 300+mhl, width=2.5, fill="black")
hh = canvas.create_line(300, 300, 300 + hhl, 300+hhl, width=3, fill="blue")

def menu():
    window.destroy()
    os.system("python Clock_App.py")

ttk.Button(window, text="Menu Window", command=menu).pack(pady=5)


clock()
window.mainloop()