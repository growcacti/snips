import tkinter as tk
from tkinter.font import Font

# Create the main window
root = tk.Tk()

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack()

# Configure tags
text_widget.tag_configure('left_justify', justify='left')
text_widget.tag_configure('right_justify', justify='right')
text_widget.tag_configure('center_justify', justify='center')

# Font size and style tags
large_font = Font(family="Arial", size=20)
bold_italic_font = Font(family="Arial", size=12, weight="bold", slant="italic")

text_widget.tag_configure('large_font', font=large_font)
text_widget.tag_configure('bold_italic', font=bold_italic_font)

# Example text
text_widget.insert('end', "Left-aligned text\n", 'left_justify')
text_widget.insert('end', "Right-aligned text\n", 'right_justify')
text_widget.insert('end', "Center-aligned text\n", 'center_justify')
text_widget.insert('end', "Large font size text\n", 'large_font')
text_widget.insert('end', "Bold and Italic text\n", 'bold_italic')

# Run the main loop
root.mainloop()
