import tkinter as tk
from tkinter import ttk
import os

class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.columnconfigure(0, weight=1)  # Make the column expandable

        # Initialize Notebook
        self.notebook = ttk.Notebook(self.parent)
        self.frm1 = ttk.Frame(self.notebook, width=50, height=40)
        self.notebook.add(self.frm1, text='Tab 1')  # Add tab to notebook
        self.notebook.grid(row=4, column=0, sticky='nesw')  # Place notebook in GUI

        # Menu setup
        self.file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=None)
        # ... Add other menu items ...

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter App")
        self.geometry("400x300")  # Set window size

        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    app = App()
    app.mainloop()
