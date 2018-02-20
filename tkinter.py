# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:32:34 2018

@author: SONY
"""

import tkinter
from tkinter import *

def responce():
    print(x.get())
    
root=Tk()
root.title("hello world")

l=Label(root,text="python")
l.pack()

b=Button(root, text="click me!")
b.pack()

c=Button(root, text="print INDIA", command=responce)
c.pack()

x=StringVar()

e=Entry(root, textvariable=x)
e.pack()


root.mainloop()
