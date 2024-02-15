import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Python 2 to 3 Converter")
        self.geometry("400x150")

        self.label = tk.Label(self, text="Select a Python 2 file to convert")
        self.label.pack(pady=20)

        self.select_button = tk.Button(
            self, text="Select File", command=self.select_file
        )
        self.select_button.pack()

        self.convert_button = tk.Button(
            self, text="Convert", command=self.convert, state=tk.DISABLED
        )
        self.convert_button.pack(pady=20)

        self.filepath = ""

    def select_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if self.filepath:
            self.convert_button.config(state=tk.NORMAL)

    def convert(self):
        if self.filepath:
            try:
                subprocess.run(["2to3", "--write", "--nobackups", self.filepath])
                messagebox.showinfo(
                    "Success",
                    f"File converted successfully!\nSaved at: {self.filepath}",
                )
            except Exception as e:
                messagebox.showerror("Error", f"Error while converting: {e}")
        else:
            messagebox.showwarning(
                "No file selected", "Please select a Python 2 file first."
            )


if __name__ == "__main__":
    app = App()
    app.mainloop()
