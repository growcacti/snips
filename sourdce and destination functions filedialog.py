from tkinter import filedialog





def source():
    

    source = filedialog.askopenfile(
    mode='r',
    title='Select  imagefile',
    filetypes=[('jpg', '*.png *bmp')])


def destination():
    destination = filedialog.asksaveasfile(
    mode='w',
    title='Select a destination file',
    defaultextension='.csv',
    filetypes=[('png', '*.jpg *.bmp')])






def openwriteclose():
    destination.write(source.read())
    source.close()
    destination.close()

