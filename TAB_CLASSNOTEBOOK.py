import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Notebook with Class Tabs")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

        # Adding tabs
        self.tab1 = Tab1(self.notebook)
        self.tab2 = Tab2(self.notebook)

        self.notebook.add(self.tab1.frame, text="Tab 1")
        self.notebook.add(self.tab2.frame, text="Tab 2")


class Tab1:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.label = ttk.Label(self.frame, text="This is Tab 1")
        self.label.pack(pady=20, padx=20)


class Tab2:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.label = ttk.Label(self.frame, text="This is Tab 2")
        self.label.pack(pady=20, padx=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
