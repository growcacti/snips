import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scrollable Notebook")

# Create a frame for the notebook and scrollbar
notebook_frame = tk.Frame(root)
notebook_frame.grid(row=0, column=0, sticky="nsew")

# Configure the grid to expand the frame
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a canvas within the frame
canvas = tk.Canvas(notebook_frame)
canvas.grid(row=0, column=0, sticky="nsew")

# Add a scrollbar to the frame
scrollbar = ttk.Scrollbar(notebook_frame, orient="horizontal", command=canvas.xview)
scrollbar.grid(row=1, column=0, sticky="ew")
canvas.configure(xscrollcommand=scrollbar.set)

# Configure the notebook frame grid
notebook_frame.grid_rowconfigure(0, weight=1)
notebook_frame.grid_columnconfigure(0, weight=1)

# Create a frame inside the canvas to hold the notebook
notebook_frame_inside = tk.Frame(canvas)
canvas.create_window((0, 0), window=notebook_frame_inside, anchor='nw')

# Create the notebook
notebook = ttk.Notebook(notebook_frame_inside)
notebook.grid(row=0, column=0, sticky="nsew")

# Adding tabs
for i in range(20):
    frame = ttk.Frame(notebook, width=400, height=280)
    notebook.add(frame, text=f'Tab {i+1}')

def on_configure(event):
    # Update the scroll region to encompass the inner frame
    canvas.configure(scrollregion=canvas.bbox("all"))

notebook_frame_inside.bind('<Configure>', on_configure)

root.mainloop()
