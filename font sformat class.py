import tkinter as tk
from tkinter import ttk
from tkinter.font import Font



class FontFormat_Widget:

    def __init__(self, textwidget):
        self.top = tk.Toplevel()
        self.top_frame = tk.Frame(self.top)
        self.top_frame.pack(side='top', fill='x')

        self.font_size_combobox = ttk.Combobox(top_frame, values=[8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
        self.font_size_combobox.pack(side='left', padx=10, pady=10)
        self.font_size_combobox.set("12")  # default value

        # Create a Button to change font size
        self.change_font_button = tk.Button(top_frame, text="Change Font Size", command=change_font)
        self.change_font_button.pack(side='left', padx=10, pady=10)
        self.textwidget = textwidget
        self.change_font(self.textwidget)
        # Create a Text widget
    def change_font(self, textwidget):
            selected_size = font_size_combobox.get()
            new_font = Font(family="Arial", size=int(selected_size))
            textwidget.configure(font=new_font)

      
            change_font_button = tk.Button(top_frame, text="Change Font Size", command=change_font)
            change_font_button.pack(side='left', padx=10, pady=10)

    
