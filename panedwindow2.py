from tkinter import *
from tkinter import *
from tkinter import ttk
import math
import numpy as np
import matplotlib as plt
from decimal import *
import tkinter

# Top level window
window = Tk()

window.title("Great Circle Route")
window.geometry('800x600')

# Create a panedwindow
pane = PanedWindow(window, orient=VERTICAL)
pane.pack()

root = Label(pane, text="Distance of Great Circle", bg="blue")
pane.add(root)

def get_sum(event):
    
    num = float(numEntry.get())
    φ = num
    φ1 = φ*np.pi/180
    r = 6371
    g= (2*φ1+(math.cos(φ1)-1)*np.pi)*r    
    sum = g    
    sumEntry.insert(0, sum)
    
numEntry = Entry(root)
numEntry.pack(side=LEFT)

Label(root, text="distance").pack(side=LEFT)

equalButton = Button(root, text="=")
equalButton.bind("<Button-1>", get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root = Label(pane, text="Distance of Great Circle", bg="blue")
pane.add(root)

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

root = Label(pane, text="Vertex Longitude", bg="red")
pane.add(root)

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



root = Label(pane, text="Row 3", bg="orange")
pane.add(root)

window.mainloop()