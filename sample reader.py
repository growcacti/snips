import tkinter as tk
from tkinter import filedialog


class EbookReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Ebook Reader")

        # Menu bar for opening files
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.load_file)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Text widget for displaying content
        self.text_widget = tk.Text(self.root, wrap=tk.WORD, bg="light gray")
        self.text_widget.pack(expand=1, fill=tk.BOTH)

    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Open ebook",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )

        if not file_path:
            return

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, content)


if __name__ == "__main__":
    root = tk.Tk()
    app = EbookReader(root)
    root.mainloop()
