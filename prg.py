# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 09:45:08 2018

@author: SONY
"""

import tkinter
from tkinter import *

def responce():
    print("priya")

root=Tk()
root.title("Label Tkinker - 1")

l=Label(root,text="python")
l.pack()

b=Button(root, text="click me!")
b.pack()

c=Button(root, text="print INDIA", command=responce)
c.pack()
root.mainloop()

