import tkinter as tk

def on_return(event):
    # Get the current line number
    line_num = text_widget.index(tk.INSERT).split('.')[0]
    
    # Get the previous line's content
    prev_line = text_widget.get(f"{int(line_num)-1}.0", f"{line_num}-1.end")
    
    # Count the leading spaces (indentation)
    count_spaces = len(prev_line) - len(prev_line.lstrip())
    
    # Insert the same amount of spaces on the new line
    text_widget.insert(tk.INSERT, ' ' * count_spaces)

def on_tab(event):
    # Insert a single space
    text_widget.insert(tk.INSERT, ' ')
    
    # Return 'break' to prevent the default behavior
    return "break"

root = tk.Tk()
root.title("Simple Indenting Text Editor")

text_widget = tk.Text(root, wrap=tk.WORD, undo=True, width=50, height=20)
text_widget.pack(padx=10, pady=10)

# Bind the Return and Tab key
text_widget.bind("<Return>", on_return)
text_widget.bind("<Tab>", on_tab)



def on_return(event):
    # Get the current line number
    line_num = text_widget.index(tk.INSERT).split('.')[0]
    
    # Get the previous line's content
    prev_line = text_widget.get(f"{int(line_num)-1}.0", f"{line_num}-1.end")
    
    # Count the leading spaces (indentation)
    count_spaces = len(prev_line) - len(prev_line.lstrip())
    
    # Insert the same amount of spaces on the new line
    text_widget.insert(tk.INSERT, ' ' * count_spaces)

def on_tab(event):
    # Insert 4 spaces (you can customize this value)
    text_widget.insert(tk.INSERT, ' ' * 4)
    
    # Return 'break' to prevent the default behavior
    return "break"

root = tk.Tk()
root.title("Simple Indenting Text Editor")

text_widget = tk.Text(root, wrap=tk.WORD, undo=True, width=50, height=20)
text_widget.pack(padx=10, pady=10)

# Bind the Return and Tab key
text_widget.bind("<Return>", on_return)
text_widget.bind("<Tab>", on_tab)

root.mainloop()
