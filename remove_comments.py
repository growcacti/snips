import tkinter as tk

def remove_comments():
    try:
        # Get the highlighted text
        input_code = input_text.get(tk.SEL_FIRST, tk.SEL_LAST).splitlines()
    except tk.TclError:
        # If nothing is highlighted, get all text
        input_code = input_text.get("1.0", tk.END).splitlines()

    cleaned_code = [line for line in input_code if not line.strip().startswith('#')]

    # To replace only the highlighted area, delete it first then insert cleaned code
    try:
        input_text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        input_text.insert(tk.SEL_FIRST, "\n".join(cleaned_code))
    except tk.TclError:
        # If nothing was highlighted, replace all text
        input_text.delete("1.0", tk.END)
        input_text.insert("1.0", "\n".join(cleaned_code))

# Set up the main window
root = tk.Tk()
root.title("Remove Python Comments")

# Configure the grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create the input text area with grid
input_text = tk.Text(root, height=15, width=50)
input_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create the button to remove comments
remove_button = tk.Button(root, text="Remove Comments", command=remove_comments)
remove_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

root.mainloop()

