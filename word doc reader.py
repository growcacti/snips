import docx
import tkinter as tk
from tkinter import filedialog, Text, scrolledtext

def read_word_file(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word documents", "*.docx"), ("All files", "*.*")])
    if file_path:
        content = read_word_file(file_path)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, content)

# Create the main window
app = tk.Tk()
app.title("Word Document Reader")

# Add a button to load the Word document
load_button = tk.Button(app, text="Load Word Document", command=load_file)
load_button.pack(pady=20)

# Add a scrolled text widget to display the content
text_box = scrolledtext.ScrolledText(app, wrap=tk.WORD)
text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

app.mainloop()
