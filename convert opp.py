




import tkinter as tk
from os import listdir

def update_list():
    list_box.delete(0, tk.END)  # Clear the list box
    path = entry1.get()  # Get the directory path from the first entry
    try:
        files = listdir(path)  # List files in the directory
        for file in files:
            list_box.insert(tk.END, file)  # Add file to the list box
    except FileNotFoundError:
        list_box.insert(tk.END, "Directory not found")

# Create the main window
root = tk.Tk()
root.title("File List Display")

# Create entry widgets
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, columnspan=2, sticky='ew')  # Span across 2 columns

entry2 = tk.Entry(root)
entry2.grid(row=1, column=0, columnspan=2, sticky='ew')  # Span across 2 columns

# Create a button to update the list
button = tk.Button(root, text="Update List", command=update_list)
button.grid(row=2, column=0, columnspan=2, sticky='ew')  # Span across 2 columns

# Create a list box with a scrollbar
list_box = tk.Listbox(root)
list_box.grid(row=3, column=0, sticky='nsew')  # Align to North, South, East, West

# Add a scrollbar
scrollbar = tk.Scrollbar(root, orient="vertical", command=list_box.yview)
scrollbar.grid(row=3, column=1, sticky='ns')  # Align to North, South

list_box.config(yscrollcommand=scrollbar.set)

# Grid configuration
root.grid_rowconfigure(3, weight=1)  # Make the list box row expandable
root.grid_columnconfigure(0, weight=1)  # Make the first column expandable

# Run the main loop
root.mainloop()



directory_path = os.path.dirname(file_path)if file_path:
entry2.insert(f"Selected file: {file_path}")
else:
    entry2.insert("No file selected or dialog canceled")
