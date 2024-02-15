import tkinter as tk

class ScrolledText(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        # Create the scrollbar
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create the Text widget
        self.text_widget = tk.Text(self, wrap=tk.WORD, yscrollcommand=self.scrollbar.set, *args, **kwargs)
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configure the scrollbar to scroll the Text widget
        self.scrollbar.config(command=self.text_widget.yview)

    def insert(self, index, chars, *args):
        self.text_widget.insert(index, chars, *args)

    def delete(self, first, last=None):
        self.text_widget.delete(first, last)

    # You can add more methods if needed to proxy to the Text widget

root = tk.Tk()
root.geometry("300x200")

stext = ScrolledText(root)
stext.pack(fill=tk.BOTH, expand=True)
stext.insert(tk.END, "This is a combined Text and Scrollbar widget.\n" * 20)

root.mainloop()
