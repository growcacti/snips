import tkinter as tk
from tkinter import ttk
from tkinter.ttk import LabelFrame
# Create the main window
root = tk.Tk()
root.title("LabelFrame Example")

# Create a LabelFrame widget
llf = ttk.LabelFrame(root, text="gfhfghfghfg ")
llf.grid(row=0, column=0)
# Add a widget inside the LabelFrame
inside_label = tk.Label(llf, text="--------------------")
inside_label.grid(row=2, column=0)
# Create a LabelFrame widget
lf2 = ttk.LabelFrame(root, text="hgjghjghj")
lf2.grid(row=2, column=1)# Create a LabelFrame widget
lllff2 = tk.Label(lf2, text="fdgdfd").grid(row=3,column=2)
lf3 = ttk.LabelFrame(root, text="465")
lf3.grid(row=4, column=2)# Create a LabelFrame widget
lllff33 = tk.Label(lf3, text="fdgdfd").grid(row=4,column=2)
llf3 = ttk.LabelFrame(root, text="465")
llf4 = ttk.LabelFrame(root, text="53")
llf4.grid(row=3, column=3)]
llf5.grid(row=4, column=5)# Create a LabelFrame widget
llf6 = ttk.LabelFrame(root, text="6")
llf6.grid(row=5, column=6)# Create a LabelFrame widget
llf7 = ttk.LabelFrame(root, text="jhh")
llf7.grid(row=6, column=8)# Create a LabelFrame widget
llf8 = ttk.LabelFrame(root, text="jghh")
llf8.grid(row=8, column=9)# Create a LabelFrame widget
llf9 = ttk.LabelFrame(root, text="ghj")
llf9.grid(row=9, column=0)
# Start the GUI event loop
root.mainloop()
