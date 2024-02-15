import tkinter as tk

def get_selected_items():
    selected_indices = lbox.curselection()
    selected_items = [lbox.get(i) for i in selected_indices]
    print("Selected items:", selected_items)

# Create the main window
root = tk.Tk()

# Create a lbox with multiple select mode
lbox = tk.lbox(root, selectmode='multiple')
lbox.pack()

# Add some items to the lbox
for i in range(1, 11):
    lbox.insert(tk.END, "Item " + str(i))

# Button to get selected items
button = tk.Button(root, text="Get Selected Items", command=get_selected_items)
button.pack()

root.mainloop()
