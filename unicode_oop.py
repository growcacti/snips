import tkinter as tk
from tkinter import ttk, filedialog

class UnicodeListGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Unicode List Generator")
        
        # Create and place labels, entries, and button
        start_label = ttk.Label(self.master, text="Start (hex):")
        start_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        end_label = ttk.Label(self.master, text="End (hex):")
        end_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

        self.start_entry = ttk.Entry(self.master, width=10)
        self.start_entry.grid(row=0, column=1, padx=10, pady=5)

        self.end_entry = ttk.Entry(self.master, width=10)
        self.end_entry.grid(row=1, column=1, padx=10, pady=5)

        generate_button = ttk.Button(self.master, text="Generate", command=self.generate_unicode)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        save_button = ttk.Button(self.master, text="Save to File", command=self.save_to_file)
        save_button.grid(row=2, column=4)

        clear_button = ttk.Button(self.master, text="Clear list", command=self.clear)
        clear_button.grid(row=2, column=6, pady=10)

        # Create and place listbox for output
        self.output_listbox = tk.Listbox(self.master, width=20, height=15)
        self.output_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def generate_unicode(self):
        start_hex = self.start_entry.get()
        end_hex = self.end_entry.get()

        # Convert hex strings to integers
        start_int = int(start_hex, 16)
        end_int = int(end_hex, 16)

        # Clear the listbox
        self.output_listbox.delete(0, tk.END)

        # Add characters to the listbox
        for code_point in range(start_int, end_int + 1):
            char = chr(code_point)
            hex_value = f"{code_point:04X}"
            self.output_listbox.insert(tk.END, f"U+{hex_value}: {char}")

    def save_to_file(self):
        # Choose where to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Text files", "*.txt"),
                                                             ("All files", "*.*")])
        if not file_path:  # if the user cancels the save
            return

        with open(file_path, 'w', encoding='utf-8') as file:
            for item in self.output_listbox.get(0, tk.END):
                file.write(item + ',' + '\n')

    def clear(self):
        self.output_listbox.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = UnicodeListGeneratorApp(root)
    root.mainloop()
