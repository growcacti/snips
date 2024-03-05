import tkinter as tk
from tkinter import ttk
import math

def calculate():
    num = float(entry_num.get())
    start = float(entry_start.get())
    stop = float(entry_stop.get())
    step = float(entry_step.get())
    
    operation = combo_operation.get()
    
    result_list.delete(0, tk.END)
    step_list.delete(0, tk.END)
    
    for i in range(int((stop - start)/step) + 1):
        current_val = start + i * step
        step_list.insert(tk.END, current_val)
        
        if operation == "Add":
            result_list.insert(tk.END, num + current_val)
        elif operation == "Subtract":
            result_list.insert(tk.END, num - current_val)
        elif operation == "Multiply":
            result_list.insert(tk.END, num * current_val)
        elif operation == "Divide":
            if current_val != 0:
                result_list.insert(tk.END, num / current_val)
            else:
                result_list.insert(tk.END, "DIV by ZERO")

        elif operation == "Power of":
                result_list.delete(i)
                result_list.insert(i, num ** current_val)
         
        elif operation == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_val))



    if activate_additional.get():
        additional_num = float(entry_additional_num.get())
        additional_op = combo_additional_op.get()
        
        for i in range(result_list.size()):
            current_result = float(result_list.get(i))
            
            if additional_op == "Add":
                result_list.delete(i)
                result_list.insert(i, current_result + additional_num)
            elif additional_op == "Subtract":
                result_list.delete(i)
                result_list.insert(i, current_result - additional_num)
            elif additional_op == "Multiply":
                result_list.delete(i)
                result_list.insert(i, current_result * additional_num)
            elif additional_op == "Divide":
                result_list.delete(i)
                if additional_num != 0:
                    result_list.insert(i, current_result / additional_num)
    
                else:
                    result_list.insert("end", "Can not be Zero")


            elif additional_op == "Power of":
                result_list.delete(i)
                result_list.insert(i, current_result ** additional_num)


            elif additional_op == "SQRT of":
                result_list.delete(i)
                result_list.insert(i, math.sqrt(current_result))

#------------------------------------------------------------------


                    
def sync_scroll(*args):
    result_list.yview_moveto(args[0])
    step_list.yview_moveto(args[0])


app = tk.Tk()
app.title("Arithmetic Operations")

# Number Entry
lbl_num = tk.Label(app, text="Number")
lbl_num.grid(row=0, column=0)
entry_num = tk.Entry(app)
entry_num.grid(row=0, column=1)

# Operation ComboBox
lbl_operation = tk.Label(app, text="Operation")
lbl_operation.grid(row=1, column=0)
combo_operation = ttk.Combobox(app, values=["Add", "Subtract", "Multiply", "Divide","Power of", "SQRT of"])
combo_operation.grid(row=1, column=1)
combo_operation.set("Add")

# Range Entries
lbl_range = tk.Label(app, text="Start-Stop-Step Range")
lbl_range.grid(row=2, column=0)
entry_start = tk.Entry(app, width=5)
entry_start.grid(row=2, column=1)
entry_stop = tk.Entry(app, width=5)
entry_stop.grid(row=2, column=2)
entry_step = tk.Entry(app, width=5)
entry_step.grid(row=2, column=3)

# Result and Steps Listbox
lbl_result = tk.Label(app, text="Results")
lbl_result.grid(row=3, column=0)
result_list = tk.Listbox(app, width=20, height=10, yscrollcommand=sync_scroll)
result_list.grid(row=3, column=1)
lbl_step = tk.Label(app, text="Steps")
lbl_step.grid(row=3, column=2)
step_list = tk.Listbox(app, width=20, height=10, yscrollcommand=sync_scroll)
step_list.grid(row=3, column=3)

# Scrollbar for the listboxes
scrollbar = tk.Scrollbar(app, command=sync_scroll)
scrollbar.grid(row=3, column=4, sticky='ns')

result_list.config(yscrollcommand=scrollbar.set)
step_list.config(yscrollcommand=scrollbar.set)


# Additional Operations and Number
activate_additional = tk.IntVar()
chk_additional = tk.Checkbutton(app, text="Activate Additional Operation", variable=activate_additional)
chk_additional.grid(row=4, column=0)
combo_additional_op = ttk.Combobox(app, values=["Add", "Subtract", "Multiply", "Divide", "Power of", "SQRT of"])
combo_additional_op.grid(row=4, column=1)
entry_additional_num = tk.Entry(app)
entry_additional_num.grid(row=4, column=2)

# Calculate Button
btn_calculate = tk.Button(app, text="Calculate", command=calculate)
btn_calculate.grid(row=5, column=0, columnspan=4)

app.mainloop()
