import tkinter as tk
from tkinter import ttk 

class ScrollableNotebook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scrollable Notebook")

        # Create a frame for the notebook and scrollbar
        notebook_frame = tk.Frame(self, width=200,height=45)
        notebook_frame.grid(row=0, column=0, sticky="nsew")

        # Configure the grid to expand the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create a canvas within the frame
        self.canvas = tk.Canvas(notebook_frame)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Add a scrollbar to the frame
        scrollbar = ttk.Scrollbar(notebook_frame, orient="horizontal", command=self.canvas.xview)
        scrollbar.grid(row=1, column=0, sticky="ew")
        self.canvas.configure(xscrollcommand=scrollbar.set)

        # Configure the notebook frame grid
        notebook_frame.grid_rowconfigure(0, weight=1)
        notebook_frame.grid_columnconfigure(0, weight=1)

        # Create a frame inside the canvas to hold the notebook
        notebook_frame_inside = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=notebook_frame_inside, anchor='nw')

        # Create the notebook
        self.notebook = ttk.Notebook(notebook_frame_inside)
        self.notebook.grid(row=0, column=0, sticky="nsew")
        notebook_frame_inside.bind('<Configure>', self.on_configure)
       

    
    def on_configure(self, event):

         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

       
    def add_LABEL_TAB(self, title, **kwargs):
        frame = ttk.Frame(self.notebook, **kwargs)
        self.notebook.add(frame, text=title)
        return frame 
        """
        Add a new LABEL_TAB to the notebook.

        :param frame: The frame (or any widget) to be used as the content of the LABEL_TAB.
        :param title: The title of the LABEL_TAB.
        """
        self.notebook.add(frame, text=title)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


app = ScrollableNotebook()





def make_LABEL_TABs():
    f1 = app.add_LABEL_TAB("LABEL_TAB1label")
    ttk.Label(f1, text="Content of the new LABEL_TAB").pack()
    f2 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f2, text="Content of the new LABEL_TAB").pack()
    f3 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f3, text="Content of the new LABEL_TAB").pack()
    f4 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f4, text="Content of the new LABEL_TAB").pack()
    f5 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f5, text="Content of the new LABEL_TAB").pack()
    f6 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f6, text="Content of the new LABEL_TAB").pack()
    f7 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f7, text="Content of the new LABEL_TAB").pack()
    f8 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f8, text="Content of the new LABEL_TAB").pack()
    f9 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f9, text="Content of the new LABEL_TAB").pack()
    f10 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f10, text="Content of the new LABEL_TAB").pack()
    f11 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f11, text="Content of the new LABEL_TAB").pack()
    f12 = app.add_LABEL_TAB("LABEL_TAB1")
    ttk.Label(f12, text="Content of the new LABEL_TAB").pack()
    f13 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f13, text="Content of the new LABEL_TAB").pack()
    f14 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f14, text="Content of the new LABEL_TAB").pack()
    f15 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f15, text="Content of the new LABEL_TAB").pack()
    f16 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f16, text="Content of the new LABEL_TAB").pack()
    f17 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f17, text="Content of the new LABEL_TAB").pack()
    f18 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f18, text="Content of the new LABEL_TAB").pack()
    f19 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f19, text="Content of the new LABEL_TAB").pack()
    f20 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f20, text="Content of the new LABEL_TAB").pack()
    f21 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f21, text="Content of the new LABEL_TAB").pack()
    f22 = app.add_LABEL_TAB("LABEL_TAB")
    ttk.Label(f22, text="Content of the new LABEL_TAB").pack()



make_LABEL_TABs()



# Add the new LABEL_TAB to the notebook

app.mainloop()

