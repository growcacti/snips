import tkinter as tk

class Sorted_Listbox:
    def __init__(self, root):
        self.root = root
        self.items = []
        self.dict_items = []

        # Create a Listbox
        self.lb = tk.Listbox(self.root, height=35)
        self.lb.grid(row=3, column=5, sticky='nsew')

        # Create a Scrollbar and set its command to the Listbox's yview
        self.scrollbar = tk.Scrollbar(self.root, orient='vertical', command=self.lb.yview)
        self.scrollbar.grid(row=3, column=6, sticky='ns')

        # Set the Listbox's yscrollcommand to the Scrollbar's set
        self.lb.config(yscrollcommand=self.scrollbar.set)

        self.sort_bnt = tk.Button(self.root, text="Sort", command=self.sort_lb)
        self.sort_bnt.grid(row=2, column=1)
        self.clear_btn = tk.Button(self.root, text="clear", command=self.clear)
        self.clear_btn.grid(row=2, column=2)

    def sort_lb(self):
        # Retrieve and sort the lb items
        items = list(self.lb.get(0, tk.END))
        items.sort()

        # Update the lb with sorted items
        self.lb.delete(0, tk.END)  # Clear current items
        for item in items:
            self.lb.insert(tk.END, item)

    def clear(self):
        self.lb.delete(0, tk.END)

# Usage
root = tk.Tk()
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(5, weight=1)
lb = Sorted_Listbox(root)
root.mainloop()
