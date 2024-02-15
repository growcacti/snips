import tkinter as tk
from tkinter import filedialog, messagebox
import json

def remove_duplicates(d):
    inverse = {}
    for k, v in d.items():
        # Convert all values to strings (surrounded by double quotes)
        v = str(v)
        if v not in inverse:
            inverse[v] = k
            
    return {v: k for k, v in inverse.items()}

def remove_duplicates_from_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    cleaned_data = remove_duplicates(data)
    with open(filename, 'w') as f:
        json.dump(cleaned_data, f, indent=4)

def open_file_dialog():
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if filename:
        try:
            remove_duplicates_from_file(filename)
            messagebox.showinfo("Success", "Duplicates removed and values double-quoted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the GUI
root = tk.Tk()
root.title("Process JSON")
root.geometry("350x100")

label = tk.Label(root, text="Select a JSON file to process")
label.pack(pady=10)

button = tk.Button(root, text="Select File", command=open_file_dialog)
button.pack(pady=10)

root.mainloop()
