import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
class Font_Size

    def __init__(self):
        self.top = tk.Toplevel()
        self.top_frame = tk.Frame(self.top)
        self.top_frame.pack(side='top', fill='x')

        self.font_size_combobox = ttk.Combobox(top_frame, values=[8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
        self.font_size_combobox.pack(side='left', padx=10, pady=10)
        self.font_size_combobox.set("12")  # default value

# Create a Button to change font size
change_font_button = tk.Button(top_frame, text="Change Font Size", command=change_font)
change_font_button.pack(side='left', padx=10, pady=10)

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack(expand=True, fill='both')
        
def change_font():
    selected_size = font_size_combobox.get()
    new_font = Font(family="Arial", size=int(selected_size))
    text_widget.configure(font=new_font)

# Create the main window
root = tk.Tk()
root.title("Font Size Selector")

# Create a frame for the ComboBox and Button
top_frame = tk.Frame(root)
top_frame.pack(side='top', fill='x')

# Create a ComboBox for font sizes
font_size_combobox = ttk.Combobox(top_frame, values=[8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
font_size_combobox.pack(side='left', padx=10, pady=10)
font_size_combobox.set("12")  # default value

# Create a Button to change font size
change_font_button = tk.Button(top_frame, text="Change Font Size", command=change_font)
change_font_button.pack(side='left', padx=10, pady=10)

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack(expand=True, fill='both')

# Run the main loop
root.mainloop()
