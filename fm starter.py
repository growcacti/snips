import tkinter as tk
from tkinter import ttk
import os

def fill_tree(path):
    for i in tree.get_children():
        tree.delete(i)
    for p in os.listdir(path):
        abs_path = os.path.join(path, p)
        oid = tree.insert('', 'end', text=p, open=False)
        if os.path.isdir(abs_path):
            tree.insert(oid, 'end')

def item_opened(event):
    oid = tree.focus()
    if tree.get_children(oid):
        # This directory has already been expanded, do nothing.
        return
    path = tree.item(oid, 'text')
    abs_path = os.path.join(cur_path.get(), path)
    fill_tree(abs_path)
    cur_path.set(abs_path)

root = tk.Tk()
root.title('Simple File Manager')

cur_path = tk.StringVar()

tree = ttk.Treeview(root)
tree.pack(fill='both', expand=True)
tree.bind('<<TreeviewOpen>>', item_opened)

cur_path.set(os.path.abspath('.'))
fill_tree(cur_path.get())

root.mainloop()
