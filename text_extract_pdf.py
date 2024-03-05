import PyPDF2

import tkinter as tk
from tkinter import filedialog


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text


def load_pdf_into_text_widget():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        extracted_text = extract_text_from_pdf(file_path)
        text_widget.insert(tk.END, extracted_text)


# Create the main window
root = tk.Tk()
root.title("PDF Text Extractor")

# Create a Text widget
text_widget = tk.Text(root, wrap=tk.WORD, width=80, height=20)
text_widget.pack(padx=10, pady=10)

# Create a button to load the PDF
load_button = tk.Button(root, text="Load PDF", command=load_pdf_into_text_widget)
load_button.pack(pady=10)

root.mainloop()
