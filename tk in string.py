

import tkinter
from tkinter import *


def clicked():
    input=entry1.get()
    filename=str("filename" + input + ".txt")
    textfiel=open(filename,"W")
    
    
root=Tk()
root.title("student details")

entry1=Entry(root)
button1=Button(root,text="press to create text", command=clicked)
entry1.pack()
button1.pack()




root.mainloop()

