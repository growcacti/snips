import tkinter as tk
from tkinter import ttk, filedialog

def generate_unicode():
    start_hex = start_entry.get()
    end_hex = end_entry.get()

    # Convert hex strings to integers
    start_int = int(start_hex, 16)
    end_int = int(end_hex, 16)

    # Clear the listbox
    output_listbox.delete(0, tk.END)

    # Add characters to the listbox
    for code_point in range(start_int, end_int + 1):
        char = chr(code_point)
        hex_value = f"{code_point:04X}"
        output_listbox.insert(tk.END, f"U+{hex_value}: {char}")
def save_to_file():
    # Choose where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text files", "*.txt"),
                                                         ("All files", "*.*")])
    if not file_path:  # if the user cancels the save
        return

    with open(file_path, 'w', encoding='utf-8') as file:
        for item in output_listbox.get(0, tk.END):
            file.write(item + ','+ '\n')
def clear():
     output_listbox.delete(0, tk.END)


# Create main window
app = tk.Tk()
app.title("Unicode List Generator")

# Create and place labels, entries, and button
start_label = ttk.Label(app, text="Start (hex):")
start_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

end_label = ttk.Label(app, text="End (hex):")
end_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

start_entry = ttk.Entry(app, width=10)
start_entry.grid(row=0, column=1, padx=10, pady=5)

end_entry = ttk.Entry(app, width=10)
end_entry.grid(row=1, column=1, padx=10, pady=5)

generate_button = ttk.Button(app, text="Generate", command=generate_unicode)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)
save_button = ttk.Button(app, text="Save to File", command=save_to_file)
save_button.grid(row=2, column=4)
clear_button = ttk.Button(app, text="Clear list", command=clear)
clear_button.grid(row=2, column=6, pady=10)

# Create and place listbox for output
output_listbox = tk.Listbox(app, width=20, height=15)
output_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

app.mainloop()
