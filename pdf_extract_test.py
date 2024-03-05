
import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDrawimport PyPDF2
import tkinter as tk




def extract_pdf_text(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

def select_file_and_display():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    extracted_text = extract_pdf_text(file_path)

    # Uncomment this to print the extracted text to the console:
    # print(extracted_text)

    # Display the extracted text in a tkinter Text widget
    root = tk.Tk()
    root.title("PDF Text Extracted")
    text_widget = tk.Text(root, wrap=tk.WORD)
    text_widget.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    text_widget.insert(tk.END, extracted_text)
    root.mainloop()

if __name__ == "__main__":
    select_file_and_display()
