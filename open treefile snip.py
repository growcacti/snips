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


def on_tree_select(event):
    for selected_item in tree.selection():
        # Get the text of the selected item
        item_text = tree.item(selected_item, 'text')
        # Build the absolute path to the selected item
        abs_path = os.path.join(cur_path.get(), item_text)
        # Check if the selected item is a file and has a .txt extension
        if os.path.isfile(abs_path) and item_text.endswith('.py'):
            # Open and read the contents of the file
            with open(abs_path, 'r') as file:
                file_contents = file.read()
                # Display the contents in the text widget
                text_widget.delete('1.0', tk.END)
                text_widget.insert(tk.END, file_contents)


  

root = tk.Tk()
root.title('Simple File Manager')

# Set up the current path variable
cur_path = tk.StringVar()

# Set up the Treeview widget
tree = ttk.Treeview(root)
tree.pack(side='left', fill='both', expand=True)
tree.bind('<<TreeviewSelect>>', on_tree_select)

# Set up the Text widget for displaying file contents
text_widget = tk.Text(root, wrap='word')
text_widget.pack(side='right', fill='both', expand=True)

# Fill the tree with the current directory's content
cur_path.set(os.path.abspath('.'))
fill_tree(cur_path.get())

root.mainloop()
