import tkinter as tk
from tkinter.filedialog import askopenfilename

def get_filepath():
    filepath = askopenfilename(filetypes=[("Comma Separated Values", "*.csv"), ("All Files", "*.*")])
    if not filepath:
        return 
    return filepath

def read_file_and_remove_duplicates(variable):
    filepath = get_filepath()
    if not filepath:
        return []

    with open(filepath, 'r') as file:
        lines = file.readlines()

    cleaned_lines = [line.strip() for line in lines if line.strip()]
    unique_lines = list(set(cleaned_lines))

    # Create a list with formatted items
    formatted_items = [f"{item}" for item in unique_lines]
    

    # Displaying the formatted items
    print(formatted_items)
    return formatted_items

def on_submit():
    variable = entry.get()
    formatted_list = read_file_and_remove_duplicates(variable)
    newlist = f"{formatted_list}"
    print(newlist)
    # You can further process the formatted_list as needed

# Tkinter GUI setup
root = tk.Tk()
root.title("List Generation Program")

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Generate List", command=on_submit)
submit_button.pack()

root.mainloop()
