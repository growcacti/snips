    def open_file(self, textwidget):
        
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.self.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        textwidget.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            textwidget.insert(tk.END, text)

    def save_file(self, textwidget):
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="self.txt",
            filetypes=[("Text Files", "*.self.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = textwidget.get(1.0, tk.END)
            output_file.write(text)

