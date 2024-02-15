
def auto_indent(self, event):
    if auto_indent_var.get():  # Check if auto-indent is enabled
        line = self.textwidget.get("insert linestart", "insert lineend")
        if line.strip().endswith(":"):
            self.textwidget.insert("insert", "\n" + " " * 4)
            return "break"  # Prevents the default newline behavior
auto_indent_var = tk.BooleanVar(value=True)  # Auto-indent is enabled by default
auto_indent_checkbox = tk.Checkbutton(root, text="Enable Auto-Indent", var=auto_indent_var, command=toggle_auto_indent)
auto_indent_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")

def auto_indent(self, event):
    if self.auto_indent_var.get():  # Check if auto-indent is enabled
        line = self.textwidget.get("insert linestart", "insert lineend")
        if line.strip().endswith(":"):
            self.textwidget.insert("insert", "\n" + " " * 4)
            return "break"  # Prevents the default newline behavior

def toggle_auto_indent(self.):
    # Change settings or update UI based on the auto-indent feature's state
    if self.auto_indent_var.get():
        # Auto-indent is enabled
        self.textwidget.config(bg="alice blue")  # Set background
        print("Auto-indent enabled")  # Or update a status label in the UI
    else:
        # Auto-indent is disabled
        self.textwidget.config(bg="white")  # Set background to a ate disabled state
        print("Auto-indent disabled")  # Or update a status label in the UI

# Set up the main window
root = tk.Tk()
root.title("Python Auto-Indent")

# Configure the grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create the input text area with grid
self.textwidget = tk.Text(root, height=15, width=50)
self.textwidget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
self.textwidget.bind("<Return>", auto_indent)  # Bind the Return key to the auto_indent function

# Auto-indent toggle checkbox
self.auto_indent_var = tk.BooleanVar(value=True)  # Auto-indent is enabled by default
self.auto_indent_checkbox = tk.Checkbutton(root, text="Enable Auto-Indent", var=auto_indent_var, command=toggle_auto_indent)
self.auto_indent_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")

self.toggle_auto_indent()  # Call to set initial UI state based on the auto-indent feature's state

root.mainloop()
