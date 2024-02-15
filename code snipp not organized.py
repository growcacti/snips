import tkinter as tk
from tkinter import ttk



class MainApplication(tk.Tk):
    def __init__(self):

        super().__init__()

        self.title("Example")
        self.geometry("300x300")
        self.notebook = ttk.Notebook(self)
        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)
        self.notebook.add(self.Frame1, text="Frame1")

class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        self.labelA = ttk.Label(self, text="This is on Frame One")
        self.labelA.grid(column=1, row=1)


def quit():
    if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):
        root.destroy()


def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0, END)


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title("{} - {}".format(os.path.basename(file_name), PROGRAM_NAME))
        content_text.delete(1.0, END)
        with open(file_name) as f:
            content_text.insert(1.0, f.read())


def save_file(event=None):
    global file_name
    if not file_name:
        save_as_file()
    else:
        write_to_file(file_name)
    return "break"


def save_as_file(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title("{} - {}".format(os.path.basename(file_name), PROGRAM_NAME))
    return "break"


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, "end")
        with open(file_name, "w") as the_file:
            the_file.write(content)
    except IOError:
        pass


def cut():
    content_text.event_generate("<<Cut>>")


def copy():
    content_text.event_generate("<<Copy>>")


def paste():
    content_text.event_generate("<<Paste>>")


def undo():
    content_text.event_generate("<<Undo>>")


def redo(event=None):
    content_text.event_generate("<<Redo>>")
    return "break"


def find(event=None):
    search_top_level = Toplevel(root)
    search_top_level.title("Find Text")
    search_top_level.transient(root)
    Label(search_top_level, text="Find All:").grid(row=0, column=0, sticky="e")
    search_entry_widget = Entry(search_top_level, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky="we")
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_top_level, text="Ignore Case", variable=ignore_case_value).grid(
        row=1, column=1, sticky="e", padx=2, pady=2
    )


    def on_content_changed(event=None):
        update_line_numbers()
        update_cursor_info_bar()


def show_cursor_info_bar():
    show_cursor_info_checked = shorootbar.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand="no", fill=None, side="right", anchor="se")
    else:
        cursor_info_bar.pack_forget()



def about():
    tkinter.messagebox.shorootfo(
        "About",
        "{}{}".format(
            PROGRAM_NAME,
            "\nThis is a Text Editor application still in development JH APPS 2021",
        ),
    )


imagelist = []

def insertImage():
    select_image = filedialog.askopenfilename(
        title="Select your image",
        filetypes=[("Image Files", "*.png"), ("Image Files", "*.jpg")],
    )
    if select_image:
        imagelist.append(ImageTk.PhotoImage(file=select_image))
        content_text.image_create(END, image=imagelist[-1])

def clear_textbox():
    text_box.delete(1.0, "end")
def help():
    tkinter.messagebox.shorootfo("Help", "")


def show_info_bar():
    val = shorootbar.get()
    if val:
        line_number_bar.pack(expand=NO, fill=None, side=RIGHT, anchor="se")
    elif not val:
        "<<ListboxSelect>>", line_number_bar.pack_forget()


def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0, "end")
    content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)


def undo_highlight():
    content_text.tag_remove("active_line", 1.0, "end")

self.lb = tk.Listbox(self.root, bg=(0,255,255),bd=12,width=55,height=45,exportselection=False,selectmode=tk.MUILPLE)
self.lb = tk.Listbox(self.fram,bg="cyan2",bd=12,width=55,height=45,exportselection=False,selectmode=tk.SINGLE)
self.lb.grid(row=1, column=1, rowspan=2, padx=(0, 1), pady=20, sticky="nw")
self.lb.columnconfigure(1, weight=0, minsize=55)
self.lb = tk.Listbox(self.fram, bg="cyan2",bd=12,width=55,height=45,exportselection=False,selectmode=tk.MULTIPLE,)
self.lb.grid(row=1, column=1, rowspan=2, padx=(0, 1), pady=20, sticky="nw")
self.lb.columnconfigure(1, weight=0, minsize=55)
self.lb.grid(row=1, column=1, rowspan=2, padx=(0, 1), pady=20, sticky="nw")
self.lb.columnconfigure(1, weight=0, minsize=55)
self.ent1 = tk.Entry(root, bg="seashell", bd=15)



self.ent1.grid(row=1, column=1)
self.tx = ScrolledText(self.textfr, bg="white", bd=12, height=44, width=100)
self.dirbtn = tk.Button(root, text="---",bd=2,command=None)
self.tx.grid(row=1, column=0, padx=(0, 4))

def toggle_highlight(event=None):
    val = hltln.get()
    undo_highlight() if not val else highlight_line()
v = ttk.Treeview(root)
tv["columns"] = ("WTF", "Name", "Whatever")
tv.column("#0", width=0, stretch=NO)
tv.column("WTF", anchor=CENTER, width=80)
tv.column("Name", anchor=CENTER, width=80)
tv.column("Whatever", anchor=CENTER, width=80)

tv.heading("#0", text="", anchor=CENTER)
tv.heading("WTF", text="Id", anchor=CENTER)
tv.heading("Name", text="WTF", anchor=CENTER)
tv.heading("Whatever", text="Whatever", anchor=CENTER)

tv.insert(parent="", index=0, iid=0, text="", values=("1", "Vineet", "Alpha"))
tv.insert(parent="", index=1, iid=1, text="", values=("2", "Anil", "Bravo"))
tv.insert(parent="", index=2, iid=2, text="", values=("3", "Vinod", "Charlie"))
tv.insert(parent="", index=3, iid=3, text="", values=("4", "Vimal", "Delta"))
tv.insert(parent="", index=4, iid=4, text="", values=("5", "Manjeet", "Echo"))
tv.pack()
for self.item in self.flist:
     if self.item.endswith(".py" or ".txt"):
         self.lb.insert(tk.END, self.item)
