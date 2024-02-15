import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import io


def extract_images_from_pdf(file_path):
    doc = fitz.open(file_path)
    images = []

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        img_list = page.get_images(full=True)

        for img_index, img in enumerate(img_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # Convert it to a PIL Image object
            pil_image = Image.open(io.BytesIO(image_bytes))
            images.append(pil_image)

    return images


def select_file_and_display():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    images = extract_images_from_pdf(file_path)

    root = tk.Tk()
    root.title("Images Extracted from PDF")

    canvas = tk.Canvas(root)
    canvas.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    for idx, img in enumerate(images):
        # Save as BMP (or change extension/format for another type)
        img.save(f"image_{idx}.bmp")

        # Alternatively, display image in tkinter Canvas
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(10, 10, anchor=tk.NW, image=photo)
        root.mainloop()


if __name__ == "__main__":
    select_file_and_display()
