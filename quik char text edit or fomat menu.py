import tkinter as tk
from tkinter.font import Font

def apply_left_justify():
    text_widget.tag_add('left_justify', '1.0', 'end')

def apply_right_justify():
    text_widget.tag_add('right_justify', '1.0', 'end')

def apply_center_justify():
    text_widget.tag_add('center_justify', '1.0', 'end')

def apply_large_font():
    text_widget.tag_add('large_font', '1.0', 'end')

def apply_bold_italic():
    text_widget.tag_add('bold_italic', '1.0', 'end')

# Create the main window
root = tk.Tk()
root.title("Text Formatting Example")

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack(expand=True, fill='both')

# Configure tags for formatting
text_widget.tag_configure('left_justify', justify='left')
text_widget.tag_configure('right_justify', justify='right')
text_widget.tag_configure('center_justify', justify='center')

large_font = Font(family="Arial", size=20)
bold_italic_font = Font(family="Arial", size=12, weight="bold", slant="italic")

text_widget.tag_configure('large_font', font=large_font)
text_widget.tag_configure('bold_italic', font=bold_italic_font)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a format menu
format_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Format", menu=format_menu)

# Add menu items
format_menu.add_command(label="Left Justify", command=apply_left_justify)
format_menu.add_command(label="Right Justify", command=apply_right_justify)
format_menu.add_command(label="Center Justify", command=apply_center_justify)
format_menu.add_separator()
format_menu.add_command(label="Large Font", command=apply_large_font)
format_menu.add_command(label="Bold & Italic", command=apply_bold_italic)

# Run the main loop
root.mainloop()
