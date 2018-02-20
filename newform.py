# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:48:46 2018

@author: SONY
"""

import tkinter
from tkinter import *

    
def display():
    print("firstname:",a.get() ,'\n',"lastname:", b.get(),'\n' ,"age:",c.get(),'\n',"marks:", d.get())
    
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


e=Button(root, text="check details",command=display)
f=Button(root, text="submit",command=form)
#g=Button(root, text="age",command=responce2)
#h=Button(root, text="marks",command=responce3)
#m=Button(root,text="submit",command=display)
a.pack()
b.pack()
c.pack()
d.pack()
e.pack()
f.pack()


root.mainloop()

