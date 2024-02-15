import tkinter as tk
from tkinter import messagebox

# Include your conversion functions here
# ...

# Event handler for the conversion button
def on_convert():
    try:
        base = int(base_entry.get())
        input_data = input_entry.get()
        
        if conversion_var.get() == 'To Number':
            digits = [int(digit) for digit in input_data.split(',')]
            result = convert_from_digits(digits, base)
        elif conversion_var.get() == 'To Digits':
            number = int(input_data)
            result = convert_to_digits(number, base)
        else:
            result = "Conversion type not selected"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Main window
root = tk.Tk()
root.title("Base Conversion Tool")

# Widgets
input_label = tk.Label(root, text="Enter Data:")
input_label.grid(row=0, column=0)

input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1)

base_label = tk.Label(root, text="Base:")
base_label.grid(row=1, column=0)

base_entry = tk.Entry(root)
base_entry.grid(row=1, column=1)

conversion_var = tk.StringVar()
conversion_choices = ['To Number', 'To Digits']
conversion_var.set(conversion_choices[0])  # default value

conversion_menu = tk.OptionMenu(root, conversion_var, *conversion_choices)
conversion_menu.grid(row=2, column=0, columnspan=2)

convert_button = tk.Button(root, text="Convert", command=on_convert)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

# Start the application
root.mainloop()
