import tkinter as ui
from tkinter import ttk
import os
import time
import pygame
from threading import Thread

def music():
    pygame.mixer.music.load("1.wav")
    pygame.mixer.music.play(-1)

def stop():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        mt = Thread(target=music)
        mt.start()

def dcm():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    menum.destroy()
    os.system("python Digital_Clock.py")

def acm():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    menum.destroy()
    os.system("python Analogue_Clock.py")

menum=ui.Tk()
menum.geometry("600x600")
menum.title("Clock App")
pygame.mixer.init()
mt=Thread(target=music)
mt.start()
label=ui.Label(menum, text="Choose the type of clock that you desire:",anchor='center', justify='center')
label.pack(pady=50)
b1 = ttk.Button(menum, text="Digital Clock", command=dcm)
b1.pack(pady=15)
b2 = ttk.Button(menum, text="Analogue Clock", command=acm)
b2.pack(pady=15)
muteb=ttk.Button(menum,text="Mute/Unmute",command=stop).pack(padx=20)
menum.mainloop()