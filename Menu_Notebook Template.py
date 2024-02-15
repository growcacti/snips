import tkinter as tk
from tkinter import ttk, INSERT,END,font,Toplevel
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter.scrolledtext import ScrolledText
import sys
import os









class TestEquipmentMenu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.bar_frm = tk.Frame(self.parent, width=80, height=50)
        self.bar_frm.grid(row=0, column=0, sticky="ew")
        self.parent.columnconfigure(0, weight=1)  # This makes the column expandable
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=4, column=0)
        self.frm1 = ttk.Frame(self.notebook, width=80, height=40)
        self.notebook.add(self.frm1, text="----")
        self.txtfrm = tk.Frame(self.frm1, width=80, height=40)
        self.txtfrm.grid(row=0, column=2)
        self.tx = ScrolledText(self.txtfrm, bg="white", bd=12, height=35,width=50,)
        self.tx.grid(row=0, column=2,sticky="w")
        self.textwidget = self.tx
          
        self.path = os.getcwd()
        self.lbfrm = tk.Frame(self.frm1, width=5, height=30)
        self.lbfrm.grid(row=0, column=1)
        self.lb = tk.Listbox(self.lbfrm, bg="azure", bd=12, width=35, height=35, exportselection=False, selectmode=tk.MULTIPLE,)
        self.lb.grid(row=0, column=0)
        self.lb.focus()
       

        self.fr_buttons = tk.Frame(self.frm1, relief=tk.RAISED)
        self.fr_buttons.grid(row=0,column=0,sticky="ns")
        self.btn_1 = tk.Button(self.fr_buttons, text="---", bd=3,command=None)
        self.btn_1.grid(row=1, column=0)
        self.btn_2 = tk.Button(self.fr_buttons,text="---",bd=3,command=None)
        self.btn_2.grid(row=2, column=0)
        self.btn_3 = tk.Button(self.fr_buttons, text="---",bd=3, command=None)
        self.btn_3.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        self.btn_grab = tk.Button(self.fr_buttons, text="-",bd=6, command=None)
        self.btn_grab.grid(row=4, column=0)
        self.btn_grab2 = tk.Button(self.fr_buttons, text="----", bd=6,command=None)
        self.btn_grab2.grid(row=6,column=0)
        self.dirpath = tk.Entry(self.fr_buttons, bd=10, width=40)
        self.dirpath.grid(row=7,column=0)
        self.dirpath.insert(0, self.path)
        self.frm2 = ttk.Frame(self.notebook, width=80, height=1000)
        self.notebook.add(self.frm2, text="")
        self.frm3 = ttk.Frame(self.notebook, width=80, height=108)
        self.notebook.add(self.frm3, text="---")
        self.frm4 = ttk.Frame(self.notebook, width=80, height=60)
        self.notebook.add(self.frm4, text="----")

        self.frm5 = ttk.Frame(self.notebook, width=80, height=60)
        self.notebook.add(self.frm5, text="------")
      
        self.frm6 = ttk.Frame(self.notebook, width=80, height=60)
        self.notebook.add(self.frm6, text="-------")
       
        self.frm7 = ttk.Frame(self.notebook, width=80, height=60)
        self.notebook.add(self.frm7, text="7")

        self.frm8 = ttk.Frame(self.notebook, width=80, height=60)
        self.notebook.add(self.frm8, text="8")
        self.frm9 = ttk.Frame(self.notebook, width=80, height=60)
        self.notebook.add(self.frm9, text="9")
       
        

        self.frm4 = ttk.Frame(self.notebook, width=80, height=36)
        self.notebook.add(self.frm4, text="---")
       
        
        self.menubar = tk.Menu(self.parent, tearoff=False)
        
        self.file_menu = tk.Menu(self.menubar)
        self.edit_menu = tk.Menu(self.menubar)
        self.view_menu = tk.Menu(self.menubar)
        self.cursor_menu = tk.Menu(self.menubar)
        self.format_menu = tk.Menu(self.menubar)
        self.tool_menu = tk.Menu(self.menubar)

    
        
        self.text = self.textwidget.get("1.0", "end-1c")
        self.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(
            label="New", underline=1, command=lambda: self.clear()
        )
        self.file_menu.add_command(
            label="Open", underline=1, command=lambda: self.open_file()
        )
        self.file_menu.add_command(
            label="Save", underline=1, command=lambda: self.save_file()
        )
        self.file_menu.add_command(
            label="readlines", underline=1, command=lambda: self.readlines()
        )
        self.file_menu.add_command(label="-----", underline=1, command=self.quit)
        self.file_menu.add_command(label="-------", underline=1, command=self.quit)
        self.file_menu.add_command(label="Exit", underline=1, command=None)

        self.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(
            label="Select All",
            accelerator="Ctrl+A",
            compound="left",
            underline=0,
            command=lambda: self.textwidget.event_generate("<<SelectAll>>"),
        )
        self.edit_menu.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            compound="left",
            underline=0,
            command=lambda: self.textwidget.event_generate("<<Cut>>"),
        )
        self.edit_menu.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            compound="left",
            underline=0,
            command=lambda: self.textwidget.event_generate("<<Copy>>"),
        )
        self.edit_menu.add_command(
            label="Paste",
            accelerator="Ctrl+V",
            compound="left",
            underline=0,
            command=lambda: self.textwidget.event_generate("<<Paste>>"),
        )
      
        self.edit_menu.add_command(
            label="Find",
            accelerator="Ctrl+F",
            compound="left",
            underline=0,
            command=lambda: self.find(),
        )
        self.edit_menu.add_command(
            label="Replace",
            accelerator="Ctrl+R",
            compound="left",
            underline=0,
            command=lambda: self.replace())




    def select_all(self, event=None):
        self.textwidget.tag_add("sel", "1.0", tk.END)
        return "break"

    def copy(self, event=None):
        self.clipboard_clear()
        text = self.textwidget.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def cut(self, event):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event):
        text = self.selection_get(selection="CLIPBOARD")
        self.insert("insert", text)

    def quit(self):
        sys.exit(0)

    def clear(self):
        self.textwidget.delete("1.0", tk.END)

    def cleare1(self):
        self.e1.delete(0, END)

    def change_bg(self):
        (triple, hexstr) = askcolor()
        if hexstr:
            self.textwidget.config(bg=hexstr)

    def command(self):
        pass

    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[
                ("Python Scripts", "*.py"),
                ("Text Files", "*.txt"),
                ("All Files", "*.*"),
            ]
        )
        if not filepath:
            return
        self.textwidget.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.textwidget.insert(tk.END, text)
            return filepath      
    def save_file(self):
        filepath = asksaveasfilename(
            defaultextension="py",
            filetypes=[("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.textwidget.get(1.0, tk.END)
            output_file.write(text)
            return filepath
    def find(self):
        top = Toplevel()
        label1 = tk.Label(top, text="Find").grid(row=1, column=1)
        entry1 = tk.Entry(top, width=15, bd=12, bg="cornsilk")
        entry1.grid(row=2, column=1)

        def finder():
            # remove tag 'found' from index 1 to END
            self.textwidget.tag_remove("found", "1.0", END)
            entry = entry1.get()

            if entry1:
                idx = "1.0"
                while 1:
                    # searches for desired string from index 1
                    idx = self.textwidget.search(entry, idx, nocase=1, stopindex=END)

                    if not idx:
                        break

                    # last index sum of current index and
                    # length of text
                    lastidx = "% s+% dc" % (idx, len(entry))

                    # overwrite 'Found' at idx
                    self.textwidget.tag_add("found", idx, lastidx)
                    idx = lastidx

                # mark located string as red

                self.textwidget.tag_config(
                    "found", background="purple", foreground="yellow"
                )

        self.find_btn = tk.Button(top, text="Find", bd=8, command=finder)
        self.find_btn.grid(row=8, column=1)
        entry1.focus_set()

    def replace(self):
        top = Toplevel()
        label1 = tk.Label(top, text="Find").grid(row=1, column=1)
        entry1 = tk.Entry(top, width=15, bd=12, bg="cornsilk")
        entry1.grid(row=2, column=1)
        label2 = tk.Label(top, text="Replace With ").grid(row=3, column=1)
        entry2 = tk.Entry(top, width=15, bd=12, bg="seashell")
        entry2.grid(row=5, column=1)

        def replacer():
            # remove tag 'found' from index 1 to END
            self.textwidget.tag_remove("found", "1.0", END)

            # returns to widget currently in focus
            self.fin = entry1.get()
            self.repl = entry2.get()

            if self.fin and self.repl:
                idx = "1.0"
                while 1:
                    # searches for desired string from index 1
                    idx = self.textwidget.search(self.fin, idx, nocase=1, stopindex=END)
                    print(idx)
                    if not idx:
                        break

                    # last index sum of current index and
                    # length of text
                    lastidx = "% s+% dc" % (idx, len(self.fin))

                    self.textwidget.delete(idx, lastidx)
                    self.textwidget.insert(idx, self.repl)

                    lastidx = "% s+% dc" % (idx, len(self.repl))

                    # overwrite 'Found' at idx
                    self.textwidget.tag_add("found", idx, lastidx)
                    idx = lastidx

            
            self.textwidget.tag_config("found", foreground="green", background="yellow")

        self.replace_btn = tk.Button(top, text="Find & Replace", bd=8, command=replacer)
        self.replace_btn.grid(row=8, column=1)
        entry1.focus_set()

   

    def toggle_highlight(self, event=None):
        val = hltln.get()

        undo_highlight() if not val else highlight_line()

    def undo_highlight(self):
        self.self.textwidget.tag_remove("active_line", "1.0", tk.END)

    def format_file(self, file_path, original=False):
        try:
            with open(file_path, 'r') as file:
                original_code = file.read()

            formatted_code = autopep8.fix_code(original_code, options={'aggressive': 1})

            if original:
                base, ext = os.path.splitext(file_path)
                new_file_path = f"{base}_formatted{ext}"
                with open(new_file_path, 'w') as file:
                    file.write(formatted_code)
                self.output(f"Formatted and saved as new file: {os.path.basename(new_file_path)}")
            else:
                with open(file_path, 'w') as file:
                    file.write(formatted_code)
                self.output(f"Formatted: {os.path.basename(file_path)}")

        except Exception as e:
           mb.showerror("Error", f"An error occurred while formatting: {e}")

    def output(self, message):
        self.textwidget.insert(tk.END, message + '\n')
        self.textwidget.insert(tk.END)




    def highlight_line(self, event=None):
        start = str(self.textwidget.index(tk.INSERT)) + " linestart"
        end = str(self.textwidget.index(tk.INSERT)) + " lineend"
        self.textwidget.tag_add("sel", start, end)

        return "break"

    def highlight_word(self, event=None):
        word_pos = str(self.textwidget.index(tk.INSERT))
        start = word_pos + " wordstart"
        end = word_pos + " wordend"
        self.textwidget.tag_add("sel", start, end)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        testeq = TestEquipmentMenu(self)
        self.config(menu=testeq)


if __name__ == "__main__":
    app = App()
    app.mainloop()

    
    
