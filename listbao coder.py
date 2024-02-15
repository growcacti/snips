import tkinter as tk

def insert_code():
    """Insert the selected line of code into the text widget."""
    # Get the selected line index
    selected_indices = list_box.curselection()
    if selected_indices:
        # Get the selected line of code
        selected_line = list_box.get(selected_indices[0])
        # Insert the selected line into the text widget
        text_widget.insert(tk.END, f"{selected_line}\n")

# Create the main window
root = tk.Tk()
root.title("Code Insertion Tool")

# Create a ListBox for the lines of code
list_box = tk.Listbox(root)
list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Populate the ListBox with some example lines of code
example_lines_of_code = [
    "print('Hello, world!')",
    "for i in range(5):",
    "    print(i)",
    "def my_function():",
    "    return 'Hello'"
]
for line in example_lines_of_code:
    list_box.insert(tk.END, line)

# Create a Text widget
text_widget = tk.Text(root)
text_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create a button to insert the selected code
insert_button = tk.Button(root, text="Insert Code", command=insert_code)
insert_button.pack()

# Start the Tkinter event loop
root.mainloop()
