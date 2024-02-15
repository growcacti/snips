# ... [previous code]


# Custom scroll function to synchronize both listboxes
def sync_scroll(*args):
    result_list.yview_moveto(args[0])
    step_list.yview_moveto(args[0])


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
scrollbar.grid(row=3, column=4, sticky="ns")

result_list.config(yscrollcommand=scrollbar.set)
step_list.config(yscrollcommand=scrollbar.set)

# ... [rest of the code]
