import tkinter as tk
from tkinter import ttk
from tkinter.font import Font, families

def change_font():
    selected_font_family = font_type_combobox.get()
    selected_size = font_size_combobox.get()
    new_font = Font(family=selected_font_family, size=int(selected_size))
    text_widget.configure(font=new_font)

# Create the main window
root = tk.Tk()
root.title("Font Selector")

# Create a frame for the ComboBoxes and Button
top_frame = tk.Frame(root)
top_frame.pack(side='top', fill='x')

# Create a ComboBox for font sizes
font_size_combobox = ttk.Combobox(top_frame, values=[8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
font_size_combobox.pack(side='left', padx=10, pady=10)
font_size_combobox.set("12")  # default value

# Create a ComboBox for font types
font_type_combobox = ttk.Combobox(top_frame, values=families())
font_type_combobox.pack(side='left', padx=10, pady=10)
font_type_combobox.set("Arial")  # default value

# Create a Button to change font
change_font_button = tk.Button(top_frame, text="Apply Font", command=change_font)
change_font_button.pack(side='left', padx=10, pady=10)

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack(expand=True, fill='both')

# Run the main loop
root.mainloop()
