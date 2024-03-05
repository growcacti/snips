import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def on_tree_select(event):
    for selected_item in tree.selection():
        item_text = tree.item(selected_item, 'text')
        abs_path = os.path.join(cur_path.get(), item_text)
        
        # Check if the selected item is a file and an image
        if os.path.isfile(abs_path) and item_text.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image file with PIL
            image = Image.open(abs_path)
            # Resize image to fit within a predefined size while keeping aspect ratio
            image.thumbnail((250, 250))
            # Convert the PIL image to a format that tkinter understands
            photo = ImageTk.PhotoImage(image)
            # Update the image of the label
            image_label.config(image=photo)
            # Keep a reference to avoid garbage collection
            image_label.image = photo
        elif os.path.isfile(abs_path) and item_text.endswith('.txt'):
            # Handle text file display as before
            # ...

def fill_tree(path):
    for i in tree.get_children():
        tree.delete(i)
    for p in os.listdir(path):
        abs_path = os.path.join(path, p)
        oid = tree.insert('', 'end', text=p, open=False)
        if os.path.isdir(abs_path):
            tree.insert(oid, 'end')

root = tk.Tk()
root.title('Simple File Manager')

cur_path = tk.StringVar()

tree = ttk.Treeview(root)
tree.pack(side='left', fill='both', expand=True)
tree.bind('<<TreeviewSelect>>', on_tree_select)

# Create a Label to display images
image_label = tk.Label(root)
image_label.pack(side='right', fill='both', expand=True)

cur_path.set(os.path.abspath('.'))
fill_tree(cur_path.get())

root.mainloop()
