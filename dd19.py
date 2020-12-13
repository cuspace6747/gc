# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:33:41 2020

@author: cuspa
"""

from tkinter import *
from tkinter import ttk
import math
import numpy as np
import matplotlib as plt
from decimal import *
import tkinter

window=tkinter.Tk()
window.title("Great Circle")
window.geometry("640x400+100+100")
window.resizable(False, False)

def window(main):
    main.title('Distance of Great circle')
    main.update_idletasks()
    width = 800
    height = 800
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}'.format(width, height))

def get_sum(event):
    
    num1 = float(num1Entry.get())
    num2 = float(num2Entry.get())
    num3 = float(num3Entry.get())
    num4 = float(num4Entry.get())
    
    a = num1
    b = num2
    c = num3
    d = num4
    
    pa1 = 90-a
    pb1 = 90-c
    p1 = b-d
    r = 6371
    pa = np.radians(pa1)
    pb = np.radians(pb1)
    p = np.radians(p1)

    g= (math.cos(pa)*math.cos(pb)+math.sin(pa)*math.sin(pb)*math.cos(p))
            
    f=np.arccos(g)
    
    f1 = f*r
    
    sum = f1
    
    sumEntry.insert(0, sum)
    
root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

num3Entry = Entry(root)
num3Entry.pack(side=LEFT)

num4Entry = Entry(root)
num4Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

window(root)
root.mainloop()

window=tkinter.Tk()
window.title("Great Circle")
window.geometry("640x400+100+100")
window.resizable(False, False)

def window(main):
    main.title('Difference between Latitude circle and Great circle')
    main.update_idletasks()
    width = 800
    height = 800
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}'.format(width, height))

def get_sum(event):
    
    num1 = float(num1Entry.get())
    
    φ = num1
    φ1 = φ*np.pi/180
    r = 6371

    g= (2*φ1+(math.cos(φ1)-1)*np.pi)*r
    
    sum = g
    
    sumEntry.insert(0, sum)
    
root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="distance").pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

window(root)
root.mainloop()

window=tkinter.Tk()
window.title("Final direction")
window.geometry("640x400+100+100")
window.resizable(False, False)

def window(main):
    main.title('Final direction')
    main.update_idletasks()
    width = 800
    height = 800
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}'.format(width, height))

def get_sum(event):
    
    num1 = float(num1Entry.get())
    num2 = float(num2Entry.get())
    num3 = float(num3Entry.get())
    num4 = float(num4Entry.get())
    
    a = num1
    b = num2
    c = num3
    d = num4
    
    pa1 = 90-a
    pb1 = 90-c
    p1 = b-d
    r = 6371
    pa = np.radians(pa1)
    pb = np.radians(pb1)
    p = np.radians(p1)

    g= (math.cos(pa)*math.cos(pb)+math.sin(pa)*math.sin(pb)*math.cos(p))
    f=np.arccos(g)
    h=math.acos((math.cos(pa)-math.cos(pb)*math.cos(f))/math.sin(f)*math.sin(pb))
    h1 = h*180/np.pi
    h2 = 180-h1

    sum = h2
    
    sumEntry.insert(0, sum)
    
root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

num3Entry = Entry(root)
num3Entry.pack(side=LEFT)

num4Entry = Entry(root)
num4Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

window(root)
root.mainloop()

window=tkinter.Tk()
window.title("Starting direction")
window.geometry("640x400+100+100")
window.resizable(False, False)

def window(main):
    main.title('Starting direction')
    main.update_idletasks()
    width = 800
    height = 800
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}'.format(width, height))

def get_sum(event):
    
    num1 = float(num1Entry.get())
    num2 = float(num2Entry.get())
    num3 = float(num3Entry.get())
    num4 = float(num4Entry.get())
    
    a = num1
    b = num2
    c = num3
    d = num4
    
    pa1 = 90-a
    pb1 = 90-c
    p1 = b-d
    r = 6371
    pa = np.radians(pa1)
    pb = np.radians(pb1)
    p = np.radians(p1)

    g= (math.cos(pa)*math.cos(pb)+math.sin(pa)*math.sin(pb)*math.cos(p))
    f=np.arccos(g)
    h=math.acos((math.cos(pb)-math.cos(pa)*math.cos(f))/math.sin(f)*math.sin(pa))
    h1 = h*180/np.pi

    sum = h1
    
    sumEntry.insert(0, sum)
    
root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

num3Entry = Entry(root)
num3Entry.pack(side=LEFT)

num4Entry = Entry(root)
num4Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

window(root)
root.mainloop()

window=tkinter.Tk()
window.title("Vertex Latitude")
window.geometry("640x400+100+100")
window.resizable(False, False)

def window(main):
    main.title('Vertex Latitude')
    main.update_idletasks()
    width = 800
    height = 800
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}'.format(width, height))

def get_sum(event):
    
    num1 = float(num1Entry.get())
    num2 = float(num2Entry.get())
    num3 = float(num3Entry.get())
    num4 = float(num4Entry.get())
    
    a = num1
    b = num2
    c = num3
    d = num4
    
    pa1 = 90-a
    pb1 = 90-c
    p1 = b-d
    r = 6371
    pa = np.radians(pa1)
    pb = np.radians(pb1)
    p = np.radians(p1)

    g= (math.cos(pa)*math.cos(pb)+math.sin(pa)*math.sin(pb)*math.cos(p))
    f=np.arccos(g)
    h=math.acos((math.cos(pb)-math.cos(pa)*math.cos(f))/math.sin(f)*math.sin(pa))
    
    i = math.asin(math.cos(np.pi/2-pa)*math.cos(np.pi/2-h))
    
    j = 90 - i*180/np.pi

    sum = j
    
    sumEntry.insert(0, sum)
    
root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

num3Entry = Entry(root)
num3Entry.pack(side=LEFT)

num4Entry = Entry(root)
num4Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

window(root)
root.mainloop()

window=tkinter.Tk()
window.title("Vertex Longitude")
window.geometry("640x400+100+100")
window.resizable(False, False)

def window(main):
    main.title('Vertex Longitude')
    main.update_idletasks()
    width = 800
    height = 800
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}'.format(width, height))

def get_sum(event):
    
    num1 = float(num1Entry.get())
    num2 = float(num2Entry.get())
    num3 = float(num3Entry.get())
    num4 = float(num4Entry.get())
    
    a = num1
    b = num2
    c = num3
    d = num4
    
    pa1 = 90-a
    pb1 = 90-c
    p1 = b-d
    r = 6371
    pa = np.radians(pa1)
    pb = np.radians(pb1)
    p = np.radians(p1)

    g= (math.cos(pa)*math.cos(pb)+math.sin(pa)*math.sin(pb)*math.cos(p))
    f=np.arccos(g)
    h=math.acos((math.cos(pb)-math.cos(pa)*math.cos(f))/math.sin(f)*math.sin(pa))
    
    i = math.asin(math.cos(np.pi/2-pa)*math.cos(np.pi/2-h))
    
    j = math.atan(math.sin(np.pi/2-pa)*math.tan(np.pi/2-h))
    j1 = j*180/np.pi
    j2 = 90 - j1
    j3 = b + j2

    sum = j3
    
    sumEntry.insert(0, sum)
    
root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

num3Entry = Entry(root)
num3Entry.pack(side=LEFT)

num4Entry = Entry(root)
num4Entry.pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

window(root)
root.mainloop()