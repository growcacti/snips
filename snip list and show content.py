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
