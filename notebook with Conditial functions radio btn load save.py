import tkinter as tk
from tkinter import *
from tkinter import ttk
import os, sys, subprocess
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()
root.geometry("500x500")
notebook = ttk.Notebook(root)

notebook.grid(row=0, column=0)
frame1 = ttk.Frame(notebook)

##def open_file():
##    '''Open a file for editing.'''
##    filepath = askopenfilename(
##        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
##    )
##    if not filepath:
##        return
##    text1.delete(1.0, tk.END)
##    with open(filepath, 'r') as input_file:
##        text = input_file.read()
##        text1.insert(tk.END, text)
##
##
##
##
##
##def save_file():
##
##    filepath = asksaveasfilename(defaultextension='txt',
##                                 filetypes=[('Text Files', '*.txt'), ('Python', 'py'), ('All Files', '*.*')]),
##    if not filepath:
##        return
##    with open(filepath, 'w') as output_file:
##        text = text1.get(1.0, tk.END)
##        output_file.write(text)
##
##

frame1.rowconfigure(0, minsize=800, weight=1)
frame1.columnconfigure(1, minsize=800, weight=1)

##fr_buttons = tk.Frame(frame1, relief=tk.RAISED, bd=2)
##btn_open = tk.Button(fr_buttons, text='Open', command=open_file)
##btn_save = tk.Button(fr_buttons, text='Save As...', command=save_file)
##
##btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
##btn_save.grid(row=1, column=0, sticky='ew', padx=5)
##
##fr_buttons.grid(row=0, column=0, sticky='ns')
text1 = tk.Text(frame1)
text1.grid(row=0, column=1, sticky="nsew")
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text="1")
notebook.add(frame2, text="2")

##fr_buttons2 = tk.Frame(frame2, relief=tk.RAISED, bd=2)
##fr_buttons2.grid(row=0, column=0, sticky='ns')
##btn_save = tk.Button(fr_buttons2, text='Save As...', command=save_file)
##btn_open = tk.Button(fr_buttons2, text='Open others', command=op)
##btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
##btn_save.grid(row=1, column=0, sticky='ew', padx=5)

frame2.rowconfigure(0, minsize=800, weight=1)
frame2.columnconfigure(1, minsize=800, weight=1)

text2 = tk.Text(frame2)
text2.grid(row=0, column=1, sticky="nsew")

f3 = ttk.Frame(notebook)
notebook.add(f3, text="3")


text3 = tk.Text(f3, height=250, width=100, bg="wheat")
text3.insert("1.0", tk.END)
text3.grid(row=0, column=4, rowspan=25, columnspan=10)
f4 = ttk.Frame(notebook)
notebook.add(f4, text="4")
f5 = ttk.Frame(notebook)


notebook.add(f5, text="5")
f6 = ttk.Frame(notebook)
notebook.add(f6, text="6")
f7 = ttk.Frame(notebook)
notebook.add(f7, text="7")
f8 = ttk.Frame(notebook)
notebook.add(f8, text="8")
f9 = ttk.Frame(notebook)
notebook.add(f9, text="9")
f10 = ttk.Frame(notebook)
notebook.add(f10, text="10")
f11 = ttk.Frame(notebook)
notebook.add(f11, text="11")
text10 = tk.Text(f10, height=250, width=100, bg="wheat")
text10.insert("1.0", tk.END)
text10.grid(row=0, column=4, rowspan=25, columnspan=10)
text11 = tk.Text(f11, height=250, width=100, bg="wheat")
text11.insert("1.0", tk.END)
text11.grid(row=0, column=4, rowspan=25, columnspan=10)
text4 = tk.Text(f4, height=250, width=300, bg="orange")
text4.insert("1.0", tk.END)

text4.grid(row=0, column=4, rowspan=25, columnspan=10)
text5 = tk.Text(f5, height=250, width=300, bg="white")
text5.insert("1.0", tk.END)
text5.grid(row=0, column=4, rowspan=25, columnspan=10)
text6 = tk.Text(f6, height=250, width=100, bg="white")
text6.insert("1.0", tk.END)
text6.grid(row=0, column=4, rowspan=25, columnspan=10)
text7 = tk.Text(f7, height=250, width=100, bg="light blue")
text7.insert("1.0", tk.END)
text7.grid(row=0, column=4, rowspan=25, columnspan=10)
text8 = tk.Text(f8, height=250, width=100, bg="pink")
text8.insert("1.0", tk.END)
text8.grid(row=0, column=4, rowspan=25, columnspan=10)
text9 = tk.Text(f9, height=250, width=100, bg="light green")
text9.insert("1.0", tk.END)
text9.grid(row=0, column=4, rowspan=25, columnspan=10)

# disables the tab
# notebook.tab(0, state = 'disabled')
# entering and displaying multiple lines with the text widget

top = tk.Toplevel()
top.geometry("600x400")
fr1 = tk.Frame(top)
fr1.grid(row=1, column=0, rowspan=20, columnspan=7)


def select_save(ss):

    if ss == 1:
        text = text1.get("1.0", tk.END)
    elif ss == 2:
        text = text2.get("1.0", tk.END)
    elif ss == 3:
        text = text3.get("1.0", tk.END)
    elif ss == 4:
        text = text4.get("1.0", tk.END)
    elif ss == 5:
        text = text5.get("1.0", tk.END)
    elif ss == 6:
        text = text6.get("1.0", tk.END)
    elif ss == 7:
        text = text7.get("1.0", tk.END)
    elif ss == 8:
        text = text8.get("1.0", tk.END)
    elif ss == 9:
        text = text9.get("1.0", tk.END)
    elif ss == 10:
        text = text10.get("1.0", tk.END)
    elif ss == 11:
        text = text10.get("1.0", tk.END)

    text11.insert("1.0", text)
    filepath = asksaveasfilename(
        defaultextension="py",
        filetypes=[("Text Files", "*.txt"), ("Python", "py"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as f:
        f.write(text)


r1 = ttk.Radiobutton(fr1, text="save1", variable=1, value="Text Tab 1")
r1.config(command=lambda: select_save(1))
r2 = ttk.Radiobutton(fr1, text="save2", variable=2, value="Text Tab 1")
r2.config(command=lambda: select_save(2))
r3 = ttk.Radiobutton(fr1, text="save3", variable=3, value="Text Tab 2")
r3.config(command=lambda: select_save(3))
r4 = ttk.Radiobutton(fr1, text="save4", variable=4, value="Text Tab 3")
r4.config(command=lambda: select_save(4))
r5 = ttk.Radiobutton(fr1, text="save5", variable=5, value="Text Tab 4")
r5.config(command=lambda: select_save(5))
r6 = ttk.Radiobutton(fr1, text="save6", variable=6, value="Text Tab 5")
r6.config(command=lambda: select_save(6))
r7 = ttk.Radiobutton(fr1, text="save7", variable=7, value="Text Tab 6")
r7.config(command=lambda: select_save(7))
r8 = ttk.Radiobutton(fr1, text="save8", variable=8, value="Text Tab 7")
r8.config(command=lambda: select_save(8))
r9 = ttk.Radiobutton(fr1, text="save9", variable=9, value="Text Tab 8")
r9.config(command=lambda: select_save(9))
r10 = ttk.Radiobutton(fr1, text="save10", variable=10, value="Text Tab 9")
r10.config(command=lambda: select_save(10))
r11 = ttk.Radiobutton(fr1, text="save11", variable=11, value="Text Tab 10")
r11.config(command=lambda: select_save(11))
r1.grid(row=1, column=3)
r2.grid(row=2, column=3)
r3.grid(row=3, column=3)
r4.grid(row=4, column=3)
r5.grid(row=5, column=3)
r6.grid(row=6, column=3)
r7.grid(row=7, column=3)
r8.grid(row=8, column=3)
r9.grid(row=9, column=3)
r10.grid(row=10, column=3)
r11.grid(row=11, column=3)


def select_open(ss):

    if ss == 1:
        text = text1
    elif ss == 2:
        text = text2
    elif ss == 3:
        text = text3
    elif ss == 4:
        text = text4
    elif ss == 5:
        text = text5
    elif ss == 6:
        text = text6
    elif ss == 7:
        text = text7
    elif ss == 8:
        text = text8
    elif ss == 9:
        text = text9
    elif ss == 10:
        text = text10
    elif ss == 11:
        text = text10

    filepath = askopenfilename(
        defaultextension="py",
        filetypes=[("Text Files", "*.txt"), ("Python", "py"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    text.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text.insert("1.0", content)


r11 = ttk.Radiobutton(fr1, text="open1", variable=1, value="Text Tab 1")
r11.config(command=lambda: select_open(1))
r12 = ttk.Radiobutton(fr1, text="open2", variable=2, value="Text Tab 1")
r12.config(command=lambda: select_open(2))
r13 = ttk.Radiobutton(fr1, text="open3", variable=3, value="Text Tab 2")
r13.config(command=lambda: select_open(3))
r14 = ttk.Radiobutton(fr1, text="open4", variable=4, value="Text Tab 3")
r14.config(command=lambda: select_open(4))
r15 = ttk.Radiobutton(fr1, text="open5", variable=5, value="Text Tab 4")
r15.config(command=lambda: select_open(5))
r16 = ttk.Radiobutton(fr1, text="open6", variable=6, value="Text Tab 5")
r16.config(command=lambda: select_open(6))
r17 = ttk.Radiobutton(fr1, text="open7", variable=7, value="Text Tab 6")
r17.config(command=lambda: select_open(7))
r18 = ttk.Radiobutton(fr1, text="open8", variable=8, value="Text Tab 7")
r18.config(command=lambda: select_open(8))
r19 = ttk.Radiobutton(fr1, text="open9", variable=9, value="Text Tab 8")
r19.config(command=lambda: select_open(9))
r20 = ttk.Radiobutton(fr1, text="open10", variable=10, value="Text Tab 9")
r20.config(command=lambda: select_open(10))
r21 = ttk.Radiobutton(fr1, text="open11", variable=11, value="Text Tab 10")
r21.config(command=lambda: select_open(11))
r11.grid(row=1, column=1)
r12.grid(row=2, column=1)
r13.grid(row=3, column=1)
r14.grid(row=4, column=1)
r15.grid(row=5, column=1)
r16.grid(row=6, column=1)
r17.grid(row=7, column=1)
r18.grid(row=8, column=1)
r19.grid(row=9, column=1)
r20.grid(row=10, column=1)
r20.grid(row=11, column=1)


root.mainloop()
