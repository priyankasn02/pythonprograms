# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:23:32 2018

@author: SONY
"""

import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("messagebox tkinter-7")

def showinfobox():
    messagebox.showinfo("Intell-eyes","showinfo from PythonGuru")
    
def showwarning():
    messagebox.showwarning("Intell-eyes","showwarning from pythonguru")
    
def showerrorbox():
    messagebox.showerror("Intell-eyes","showerror from pythonguru")
    
def askquestionbox():
    result=messagebox.askquestion("Intell-eyes","Delete")
    if result=="yes":
        print("Deleted")
    else:
        print("I'm Not Deleted yet")
        
def askokcancelbox():
    result=messagebox.askyesno("Intell-eyes","can you program in c/c++?")
    if result==True:
        print("That's Great!")
    else:
        print("Try to Learn c/c++!")
        
def askyesnobox():
    result=messagebox.askyesno("Intell-eyes","Are you Learning Python?")
    if result==True:
        print("Then you are good engouh to undestanding this program")
    else:
        print("Improve your fundamentals of python, then you can undestand this python well!")
        
        
def askretrycancelbox():
    result=messagebox.askretrycancel("Intell-eyes","Your facebook password is wrong!")
    if result==true:
        print("Retrying enter your password here!")
    else:
        print("Don't you use password")
        
ba=Button(root,text="showinfo!",command=showinfobox)
ba.pack()
bb=Button(root,text="showWarning!",command=showwarningbox)
bb.pack()
bc=Button(root,text="ShowError!",command=showerrorbox)
bc.pack()
bd=Button(root,text="askquestion!",command=showquestionbox)
bd.pack()
be=Button(root,text="askokcancel!",command=askokcancelbox)
be.pack()
bf=Button(root,text="askyesno!",command=askyesnobox)
bf.pack()
bg=Button(root,text="askretrycancel!",command=askretrycancelbox)
bg.pack()

root.mainloop()