import PyPDF2
import tkinter as tk
from tkinter import filedialog, ttk


def extract_pdf_text(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page_text = reader.getPage(page_num).extractText()
            # Do some minimal reformatting here
            formatted_text = page_text.replace("\n", " ").replace(". ", ".\n")
            text += formatted_text
    return text


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    extracted_text = extract_pdf_text(file_path)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, extracted_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PDF Text Extractor")

    text_widget = tk.Text(root, wrap=tk.WORD, font=("Courier New", 12))
    text_widget.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    btn_select_file = ttk.Button(root, text="Select PDF", command=select_file)
    btn_select_file.pack(pady=10)

    root.mainloop()
