def fname1(self):
    filepath1 = askopenfilename(
        filetypes=[("Text Files", "*.self.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text3.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text2 = input_file.readlines()
        text2.insert(tk.END, text)
        return filepath2

def fname2(self):
    filepath2 = askopenfilename(
        filetypes=[("Text Files", "*.self.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text2 = input_file.readlines()
        text2.insert(tk.END, text)
        return filepath2
