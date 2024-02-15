import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class Fileloader:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the root window
        self.filepaths = []  # List to hold selected file paths

    def load_files(self):
        while True:
            filepath = filedialog.askopenfilename(
                title="Select file", filetypes=[("All files", "*.*")]
            )
            if filepath:
                self.filepaths.append(filepath)
                user_response = messagebox.askyesno(
                    "Question", "Do you want to add more files?"
                )
                if not user_response:
                    break
            else:
                break  # User cancelled the file dialog

        # Now self.filepaths contains the paths of all selected files

    def process_files(self):
        for filepath in self.filepaths:
            print(filepath)
            # doc = fitz.open(filepath)
            # ... do something with the document ...


loader = Fileloader()
loader.load_files()
loader.process_files()
