# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 10:55:47 2018

@author: SONY
"""
import tkinter
from tkinter import *


f=open("student.txt")
def responce():
    print(a.get())

def responce1():
    print(b.get())
    
    
def responce2():
    print(c.get())
    
def responce3():
    print(d.get())
    
def display():
    print(a.get() ,'\n', b.get(),'\n' ,c.get(),'\n', d.get())
    
def form():
    with open('form.txt','w') as f:
        f.writelines('\n'+'firstname:'+str(a.get())+'\n'+'lastname:'+str(b.get())+'\n'+'age:'+str(c.get())+'\n'+'marks:'+str(d.get()))
        f.close()
    
root = Tk()
root.title("student details")

svar1=StringVar()
svar2=StringVar()
ivar1=IntVar()
ivar2=IntVar()

a=Entry(textvariable=svar1)
b=Entry(textvariable=svar2)
c=Entry(textvariable=ivar1)
d=Entry(textvariable=ivar2)


e=Button(root, text="firstname",command=responce)
f=Button(root, text="lastname",command=responce1)
g=Button(root, text="age",command=responce2)
h=Button(root, text="marks",command=responce3)
m=Button(root,text="submit",command=display)
a.pack()
b.pack()
c.pack()
d.pack()
e.pack()
f.pack()
g.pack()
h.pack()
m.pack()


root.mainloop()

