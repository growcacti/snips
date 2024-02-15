import tkinter as tk
from tkinter import ttk, filedialog
import random

def generate_random_tuples():
    n = int(num_tuples_entry.get())
    tuple_size = int(tuple_size_entry.get())
    start_range = int(start_range_entry.get())
    end_range = int(end_range_entry.get())

    result = [tuple(random.randint(start_range, end_range) for _ in range(tuple_size)) for _ in range(n)]

    # Clear the Listbox and insert new tuples
    tuple_listbox.delete(0, tk.END)
    for t in result:
        tuple_listbox.insert(tk.END, str(t))

    return result

def save_to_file():
    tuples = [eval(tuple_listbox.get(i)) for i in range(tuple_listbox.size())]
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, 'w') as f:
            for t in tuples:
                f.write(str(t) + "\n")

app = tk.Tk()
app.title("Random Tuple Generator")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# ... [The rest of your UI code]

# Listbox to display the tuples
tuple_listbox = tk.Listbox(frame, height=10, width=50)
tuple_listbox.grid(column=0, row=7, columnspan=2, pady=5, sticky=(tk.W, tk.E))

# Attach a scrollbar to the Listbox
scrollbar = ttk.Scrollbar(frame, command=tuple_listbox.yview)
scrollbar.grid(column=2, row=7, pady=5, sticky=(tk.N, tk.S))
tuple_listbox.configure(yscrollcommand=scrollbar.set)

app.mainloop()
