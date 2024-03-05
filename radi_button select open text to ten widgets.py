def select_open(ss):
    
    filepath = askopenfilename(filetypes=[('Text Files', '*.txt'), ('Python', 'py'), ('All Files', '*.*')])
    if not filepath:
        return
    text.delete(1.0, tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
    if ss == 1:
        text = text1.insert('1.0', tk.END)
    elif ss == 2:
        text = text2.insert('1.0', tk.END)
    elif ss == 3:
        text = text3.insert('1.0', tk.END) 
    elif ss == 4:
        text = text4.insert('1.0', tk.END)
    elif ss == 5:
        text = text5.insert('1.0' ,tk.END)
    elif ss == 6:
        text = text6.insert('1.0', tk.END)
    elif ss == 7:
        text = text7.insert('1.0', tk.END)
    elif ss == 8:
        text = text8.insert('1.0', tk.END)
    elif ss == 9:
        text = text9.insert('1.0', tk.END)
    elif ss == 10:
        text = text10.insert('1.0', tk.END)
    elif ss == 11:
        text = text10.insert('1.0', tk.END)

  

