import tkinter as ui
import time 
import datetime
import os
from tkinter import ttk
from tkinter import messagebox
import pygame

window=None
def alarm():
    global v1,v2,v3,window
    window = ui.Tk()
    window.geometry("300x300")
    window.title("Set Alarm")
    
    hl=ui.Label(window, text="Set Hour: [Militiary Format]")
    hl.pack()
    v1=ui.Entry(window)
    v1.pack()
    ml=ui.Label(window,text="Set Minutes: [Militiary Format]")
    ml.pack()
    v2=ui.Entry(window)
    v2.pack()
    mess=ui.Label(window, text="Reminder Message:")
    mess.pack()
    v3=ui.Entry(window)
    v3.pack()
    submit=ui.Button(window,text="START",command=alarmstart)
    submit.pack(pady=20)
    menub=ui.Button(window,text="Menu Window",command=menu).pack(pady=5)

    window.mainloop()

def menu():
    window.destroy()
    os.system("python Clock_App.py")

def alarmstart():
    global v1,v2,v3
    h=v1.get()    
    m=v2.get()
    message=v3.get()
    while(1):
        if(int(h)==datetime.datetime.now().hour and int(m)==datetime.datetime.now().minute):
            music()
            messagebox.showinfo("ALERT","Time's Up!\n{}".format(message))
            break

def music():
    pygame.mixer.init()
    pygame.mixer.music.load("2.mp3")
    pygame.mixer.music.play(-1)

alarm()