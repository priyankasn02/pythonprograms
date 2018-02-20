# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:44:21 2018

@author: SONY
"""

import tkinter
from tkinter import *

def responce():
    print(ivar1.get() + ivar2.get())
    
def responce1():
    print(ivar1.get() - ivar2.get())
    
def responce2():
    print(ivar1.get() * ivar2.get())

def responce3():
    print(ivar1.get() / ivar2.get())    

root=Tk()
root.title("airthmatic operations")

ivar1=IntVar()
ivar2=IntVar()

a=Entry(textvariable=ivar1)
b=Entry(textvariable=ivar2)
add=Button(root,text="add!",command=responce)
sub=Button(root,text="sub!",command=responce1)
mul=Button(root,text="mul!",command=responce2)
div=Button(root,text="div!",command=responce3)

a.pack()
b.pack()
add.pack()
sub.pack()
mul.pack()
div.pack()


root.mainloop()