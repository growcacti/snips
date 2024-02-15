
        self.add_cascade(label="format", menu=self.format_menu)
        self.format_menu.add_command(
            label="indent",
            accelerator="Ctrl+A",
            compound="left",
            underline=0,
            command=lambda: self.indent(self.textwidget),
        )
        self.format_menu.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            compound="left",
            underline=0,
            command=lambda: self.textwidget.event_generate("<<Cut>>"),
        )
        self.format_menu.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            compound="left",
            underline=0,
            command=lambda: self.textwidget.event_generate("<<Copy>>"),
        )
        self.format_menu.add_command(
            label="Paste",
            accelerator="Ctrl+V",
            compound="left",
            underline=0,
            command=lambda: self.textwidget.event_generate("<<Paste>>"),
        )
        self.format_menu.add_command(
            label="Undo",
            accelerator="Ctrl+Z",
            compound="left",
            underline=0,
            command=lambda: self.undo(),
        )
        self.format_menu.add_command(
            label="Redo",
            accelerator="Ctrl+Y",
            compound="left",
            underline=0,
            command=lambda: self.redo(),
        )
        self.format_menu.add_command(
            label="Find",
            accelerator="Ctrl+F",
            compound="left",
            underline=0,
            command=lambda: self.find(),
        )
        self.format_menu.add_command(
            label="Replace",
            accelerator="Ctrl+R",
            compound="left",
            underline=0,
            command=lambda: self.replace(),
        )
        self.format_menu.add_command(
            label="cleartags",
            accelerator="Ctrl+G",
            compound="left",
            underline=0,
            command=lambda: self.cleartags(),
        )
    def indent2(self, event=None):
        # Get the current line and its content
        index = self.textwidget.index("insert linestart")
        line = self.textwidget.get(index, index + "lineend")

        # Check if the line starts with specific keywords
        keywords = ["if", "elif", "else", "while", "for", "def", "class"]
        if any(line.startswith(keyword) for keyword in keywords):
            # Insert four spaces at the start of the new line
            self.textwidget.insert("insert", " " * 4)


        # get leading whitespace from current line

    def apply_indent_dedent():
        sel_start, sel_end = text.tag_ranges(tk.SEL)
        if sel_start and sel_end:
            text.tag_add("indent", sel_start, sel_end)
            self.textwidget.get("insert linestart", "insert")
            match = re.match(r"^(\s+)", line)
            whitespace = match.group(0) if match else ""

            # insert the newline and the whitespace
            self.textwidget.insert("insert", f"\n{whitespace}")

        # return "break" to inhibit default insertion of newline
        return "break"

    def indent_text(self):
        text.tag_configure("indent", lmargin1=30)

    def dedent_text(self):
        text.tag_configure("indent", lmargin1=0)

    def change_indent_spaces(self):
        spaces = int(indent_spaces.get())
        text.tag_configure("indent", lmargin1=spaces * 7)

    def indent(self, textwidget):
        selected_text = textwidget.get("sel.first", "sel.last")
        if selected_text:
            # Add four spaces to the beginning of each line
            indented_text = "\n".join(
                f"    {line}" for line in selected_text.split("\n")
            )
            textwidget.replace("sel.first", "sel.last", indented_text)

    def dedent(self):
        selected_text = textwidget.get("sel.first", "sel.last")
        if selected_text:
            # Remove four spaces from the beginning of each line if present
            dedented_text = "\n".join(
                line[4:] if line.startswith("    ") else line
                for line in selected_text.split("\n")
            )
            textwidget.replace("sel.first", "sel.last", dedented_text)

    def highlight(self, textwidget):
        selected_text = textwidget.get("sel.first", "sel.last")
        if selected_text:
            textwidget.tag_add("highlight", "sel.first", "sel.last")

    def apply_indent_dedent(self):
        sel_start, sel_end = text.tag_ranges(tk.SEL)
        if sel_start and sel_end:
            text.tag_add("indent", sel_start, sel_end)

    def insert_self(self, textwidget):
        self.textwidget = textwidget
        start_index = self.textwidget.index("sel.first")
        end_index = self.textwidget.index("sel.last")

        selected_text = self.textwidget.get(start_index, end_index)
        modified_text = "\n".join(
            [
                "self." + line if line.strip() else line
                for line in selected_text.split("\n")
            ]
        )

        self.textwidget.delete(start_index, end_index)
        self.textwidget.insert(start_index, modified_text)

    def insert_selfs(self, textwidget):
        self.textwidget = textwidget

        start_index = self.textwidget.index("sel.first")
        end_index = self.textwidget.index("sel.last")

        selected_text = self.textwidget.get(start_index, end_index)
        modified_lines = [
            "self." + line.strip() if line.strip() else line
            for line in selected_text.split("\n")
        ]
        modified_text = "\n".join(modified_lines)

        self.textwidget.delete(start_index, end_index)
        self.textwidget.insert(start_index, modified_text)

    def insert_self_in_parentheses(self, textwidget):
        start_index = textwidget.index("sel.first")
        end_index = textwidget.index("sel.last")

        selected_text = textwidget.get(start_index, end_index)
        modified_lines = []

        for line in selected_text.split("\n"):
            if line.strip():
                modified_line = line.replace("()", "(self)")  # Replace () with (self)
            else:
                modified_line = line
            modified_lines.append(modified_line)

        modified_text = "\n".join(modified_lines)
        textwidget.delete(start_index, end_index)
        textwidget.insert(start_index, modified_text)

    def bindings(self):
        self.textwidget.bind("<Return>", self.auto_indent)
        self.textwidget.bind("<Key>", self.update_info)
        self.textwidget.bind("<<Selection>>", self.update_info)
