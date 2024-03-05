import tkinter
from tkinter import *
from functools import partial
win = Tk()

def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text="sum is : %d " %sum)
    return

l1 = Label(win,text="First Value")
l1.grid(row=1,column=0)
l2 = Label(win,text="Second Value")
l2.grid(row=2,column=0)
label = Label(win)
label.grid(row=6,column=3)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win,textvariable=x1,width=20)
e1.grid(row=1,column=3)
e2 = Entry(win,textvariable=x2,width=20)
e2.grid(row=2,column=3)

sum = partial(sum,label,x1,x2)
button = Button(win,text="Calculate",command=sum,bg="blue")
button.grid(row=4,column=0)

win.mainloop()
