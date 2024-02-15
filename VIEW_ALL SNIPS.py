import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter.scrolledtext import ScrolledText
import os

class LbTx(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=0, column=0)
        self.f1 = ttk.Frame(self.notebook)
        self.f1.grid(row=0, column=1)

        self.notebook.add(self.f1, text="TAB1")
        self.fram = tk.Frame(self.f1)
        self.fram.grid(row=1, column=0)
       
        self.lb = tk.Listbox(
            self.f1,
            bg="cyan2",
            bd=2,
            width=35,
            height=55,
            exportselection=False,
            selectmode=tk.SINGLE,)
        self.lb.grid(row=1, column=2)
        self.lb.focus()
        self.lb.configure(selectmode="")
        self.lb.bind("<Double-Button-1>", self.listing)
        self.lb.bind("<<ListboxSelect>>", self.showcontent)
        self.lb.bind("<Double-Button-2>", lambda event: self.run(self.path))
        self.lb.bind("<<ListboxSelect>>", lambda event: self.listing(event))
        self.curtxt = None
        self.x = self.lb.curselection()
        self.tx = ScrolledText(
            self.f1,
            bg="white",
            bd=2,
            height=50,
            width=100,
            font="TkFixedFont",
        )
        self.tx.grid(row=1, column=5)

        self.flist2 = []
        self.flist = os.listdir(self.path)
        self.lb.insert(tk.END, self.flist)
        for self.item in self.flist:
            if self.item.endswith(".py"):
                self.flist2.append(self.item)

                self.lb.insert(tk.END, self.item)

                self.lb.focus()

        self.side_frame_btns()

    def listing(self, event=None):
        """
        Handle the event when a list item is double-clicked. Opens and displays the file content.
        """
        try:
            selection_index = self.lb.curselection()[0]  # Get the index of the selected item
            file_relative_path = self.lb.get(selection_index)  # Get the relative path of the selected .py file
            file_path = os.path.join(self.path, file_relative_path)  # Construct the absolute path

            with open(file_path, "r") as file:
                content = file.read()
                self.tx.delete("1.0", tk.END)  # Clear existing content
                self.tx.insert(tk.END, content)  # Display the file content
        except Exception as e:
            print(f"Error opening file: {e}")

    def showcontent(self, x, event=None):
        for i in self.lb.curselection():
            file = self.lb.get(i)
            with open(file, "r") as file:
                file = file.read()
                self.tx.delete("1.0", tk.END)
                self.tx.insert(tk.END, file)

            return

    def run(
        self,
        path,
        event=None,
    ):
        self.path = path
        self.file = self.lb.get(ANCHOR)
        filetorun = self.path + "/" + self.file
        runpy.run_path(filetorun)
        return

    def open(self):
        """Open a file for editing."""
        self.filepath = askopenfilename(filetypes=[("All Files", "*.*")])
        if not self.filepath:
            return
        self.tx.delete(1.0, tk.END)
        with open(self.filepath, "r") as input_file:
            text = input_file.read()
            self.tx.insert(tk.END, text)

    def save(self):
        """Save the current file as a new file."""
        self.filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("All Files", "*.*")],
        )
        for file in self.filepath:
            if not file_(self.path):
                return
        with open(self.filepath, "w") as output_file:
            text = self.tx.get(1.0, tk.END)
            output_file.write(text)

    def clear(self, textwidget):
        self.textwidget = textwidget
        self.textwidget.delete("1.0", tk.END)

 

    def side_frame_btns(self):
        self.fr_btn = tk.Frame(self.fram, bd=1)
        self.fr_btn.grid(row=2, column=0, sticky="ns")
        btn_open = tk.Button(
            self.fr_btn, text="Open", bd=1, command=lambda: self.open()
        )
        btn_save = tk.Button(
            self.fr_btn, text="Save As...", bd=1, command=lambda: self.save()
        )
        btn14 = tk.Button(
            self.fr_btn, text="get dir", bd=1, command=lambda: self.newdirlist()
        )

        btn_open.grid(row=3, column=0)
        btn_save.grid(row=4, column=0)

        btn14.grid(row=5, column=0)
        btn15 = tk.Button(
            self.fr_btn, text="Run", bd=1, command=lambda: self.run(self.path)
        )
        btn15.grid(row=6, column=0)
        btn16 = tk.Button(
            self.fr_btn, text="clear path display", bd=1, command=lambda: self.cleare1()
        )
        btn16.grid(row=7, column=0)

    def binding(self):
        self.lb.bind("<Double-Button-1>", self.listing)
        self.lb.bind("<<ListboxSelect>>", lambda event: self.showcontent(event))
        self.lb.bind("<Double-Button-2>", lambda event: self.run(event))

    def changeBg(self, textwidget):
        (triple, hexstr) = askcolor()
        if hexstr:
            textwidget.config(bg=hexstr)

    def changeFg(self, textwidget):
        (triple, hexstr) = askcolor()
        if hexstr:
            textwidget.config(fg=hexstr)

    def command(self):
        pass

    def open_file(self, textwidget):
        """Open a file for editing."""
        filepath = askopenfilename(filetypes=[("All Files", "*.*")])
        if not filepath:
            return
        textwidget.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            textwidget.insert(tk.END, text)

    def save_file(self, textwidget):
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="py",
            filetypes=[("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = textwidget.get(1.0, tk.END)
            output_file.write(text)

    def fname1(self):
        filepath1 = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        text3.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text2 = input_file.readlines()
            text2.insert(tk.END, text)
            return filepath2

    def fname2(self):
        filepath2 = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        text.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text2 = input_file.readlines()
            text2.insert(tk.END, text)
            return filepath2

    def ggtxt(self, textwidget):
        gettxt = self.tx.get("1.0", tk.END)
        textwidget.insert(tk.END, gettxt)

    def edit2(self, name):
        runpy.run_path(path_name="name")

    def find(self, textwidget, entrywidget):
        # remove tag 'found' from index 1 to END
        textwidget.tag_remove("found", "1.0", END)
        self.entry = entrywidget

        if self.entry:
            idx = "1.0"
            while 1:
                # searches for desired string from index 1
                idx = textwidget.search(self.entry, idx, nocase=1, stopindex=END)

                if not idx:
                    break

                # last index sum of current index and
                # length of text
                lastidx = "% s+% dc" % (idx, len(self.entry))

                # overwrite 'Found' at idx
                textwidget.tag_add("found", idx, lastidx)
                idx = lastidx

        # mark located string as red

        textwidget.tag_config("found", foreground="blue")

    def findNreplace(self, textwidget, entry1, entry2):
        # remove tag 'found' from index 1 to END
        textwidget.tag_remove("found", "1.0", END)

        # returns to widget currently in focus
        self.fin = entry1
        self.repl = entry2

        if self.fin and self.repl:
            idx = "1.0"
            while 1:
                # searches for desired string from index 1
                idx = textwidget.search(self.fin, idx, nocase=1, stopindex=END)
                print(idx)
                if not idx:
                    break

                # last index sum of current index and
                # length of text
                lastidx = "% s+% dc" % (idx, len(self.fin))

                textwidget.delete(idx, lastidx)
                textwidget.insert(idx, self.repl)

                lastidx = "% s+% dc" % (idx, len(self.repl))

                # overwrite 'Found' at idx
                textwidget.tag_add("found", idx, lastidx)
                idx = lastidx

            # mark located string as red
            textwidget.tag_config("found", foreground="green", background="yellow")

    def find_py_files(self, directory):
        """
        Recursively find all .py files in the given directory and its subdirectories.
        Returns a sorted list of their paths.
        """
        py_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))
        return sorted(py_files)

    def newdirlist(self):
        self.path = askdirectory()
        if not self.path:
            return
        self.lb.delete(0, tk.END)
        py_files = self.find_py_files(self.path)
        for file_path in py_files:
            # Extracting relative path from self.path for better readability in Listbox
            relative_path = os.path.relpath(file_path, self.path)
            self.lb.insert(tk.END, relative_path)            

def main():
    parent = tk.Tk()
    app = LbTx(parent)
    parent.mainloop()


if __name__ == "__main__":
    main()
