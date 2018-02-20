# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:38:31 2018

@author: SONY
"""

import tkinter
from tkinter import *

def responce():
    print(ivar1.get() + ivar2.get())

root=Tk()
root.title("sum of two numbers")

ivar1=IntVar()
ivar2=IntVar()

a=Entry(textvariable=ivar1)
b=Entry(textvariable=ivar2)
add=Button(root,text="Get Result!",command=responce)

a.pack()
b.pack()
add.pack()

root.mainloop()