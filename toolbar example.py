import tkinter as tk
from tkinter import messagebox

def my_function():
    messagebox.showinfo("Info", "Function Called")

app = tk.Tk()
app.title("Menu Bar Example")

# Creating a menu bar
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

# Adding items to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=app.quit)

# Creating a toolbar
toolbar = tk.Frame(app, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Adding a button to the toolbar
icon = tk.PhotoImage(file="icon.png")  # Replace with your icon file path
icon_button = tk.Button(toolbar, image=icon, command=my_function)
icon_button.pack(side=tk.LEFT, padx=2, pady=2)

app.mainloop()
