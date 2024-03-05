import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog, messagebox
import tkinter.scrolledtext as st
import os

root = tk.Tk()
# root.iconbitmap('icons/favicon.ico')

PROGRAM_NAME = "TextEditor"
root.title(PROGRAM_NAME)
file_name = None
root.geometry("1600x800")

# all codes goes here


# FILE MENU
def cmd():
    pass


def main_menu(event=None):

    file_name = None

    def new_file(event=None):
        root.title("JH APPS")

        nonlocal file_name
        file_name = None
        text.delete(1.0, END)
        on_content_changed()

    def open_file(event=None):
        input_file_name = tk.filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ("All Files", "*.*"),
                ("Text Documents", "*.txt"),
                ("Python Scripts", "*.py"),
                ("HTML", "*.html"),
                ("CSS", "*.css"),
                ("JavaScript", "*.js"),
            ],
        )
        if input_file_name:
            nonlocal file_name
            file_name = input_file_name
            root.title("{} - {}".format(os.path.basename(file_name), PROGRAM_NAME))
            text.delete(1.0, END)
            with open(file_name) as _file:
                text.insert(1.0, _file.read())

        on_content_changed()

    def write_to_file(file_name):
        try:
            content = text.get(1.0, "end")
            with open(file_name, "w") as the_file:
                the_file.write(content)
        except IOError:
            pass

    def save_as(event=None):
        input_file_name = tk.filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("All Files", "*.*"),
                ("Text Documents", "*.txt"),
                ("HTML", "*.html"),
                ("CSS", "*.css"),
                ("JavaScript", "*.js"),
            ],
        )
        if input_file_name:
            nonlocal file_name
            file_name = input_file_name
            write_to_file(file_name)
            root.title("{} - {}".format(os.path.basename(file_name), PROGRAM_NAME))
        return "break"

    def save(event=None):
        nonlocal file_name
        if not file_name:
            save_as()
        else:
            write_to_file(file_name)
        return "break"

    # EDIT MENU
    def cut():
        text.event_generate("<<Cut>>")
        on_content_changed()
        return "break"

    def copy():
        text.event_generate("<<Copy>>")
        on_content_changed()
        return "break"

    def paste():
        text.event_generate("<<Paste>>")
        on_content_changed()
        return "break"

    def undo():
        text.event_generate("<<Undo>>")
        on_content_changed()
        return "break"

    def redo(event=None):
        text.event_generate("<<Redo>>")
        on_content_changed()
        return "break"

    def selectall(event=None):
        text.tag_add("sel", "1.0", "end")
        return "break"

    def find_text(event=None):
        search_toplevel = Toplevel(root)
        search_toplevel.title("Find Text")
        search_toplevel.transient(root)
        search_toplevel.resizable(False, False)
        Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky="e")
        search_entry_widget = Entry(search_toplevel, width=25)
        search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky="we")
        search_entry_widget.focus_set()
        ignore_case_value = IntVar()
        Checkbutton(
            search_toplevel, text="Ignore Case", variable=ignore_case_value
        ).grid(row=1, column=1, sticky="e", padx=2, pady=2)
        Button(
            search_toplevel,
            text="Find All",
            underline=0,
            command=lambda: search_output(
                search_entry_widget.get(),
                ignore_case_value.get(),
                text,
                search_toplevel,
                search_entry_widget,
            ),
        ).grid(row=0, column=2, sticky="e" + "w", padx=2, pady=2)

        def close_search_window():
            text.tag_remove("match", "1.0", END)
            search_toplevel.destroy()

        search_toplevel.protocol("WM_DELETE_WINDOW", close_search_window)
        return "break"

    def search_output(needle, if_ignore_case, text, search_toplevel, search_box):
        text.tag_remove("match", "1.0", END)
        matches_found = 0
        if needle:
            start_pos = "1.0"
            while True:
                start_pos = text.search(
                    needle, start_pos, nocase=if_ignore_case, stopindex=END
                )
                if not start_pos:
                    break

                end_pos = "{} + {}c".format(start_pos, len(needle))
                text.tag_add("match", start_pos, end_pos)
                matches_found += 1
                start_pos = end_pos
            text.tag_config("match", background="yellow", foreground="blue")
        search_box.focus_set()
        search_toplevel.title("{} matches found".format(matches_found))

    # ABOUT MENU

    def display_about(event=None):
        tk.messagebox.showinfo(
            "About", PROGRAM_NAME + "Simple Text Editor made in Python"
        )

    def display_help(event=None):
        tk.messagebox.showinfo(
            "Help",
            "This Text Editor works similar to any other editors.",
            icon="question",
        )

    def exit_editor(event=None):
        if tk.messagebox.askokcancel("Exit", "Are you sure you want to Quit?"):
            root.destroy()

    # adding Line Numbers Functionality
    def get_line_numbers():
        output = ""
        if show_line_number.get():
            row, col = text.index("end").split(".")
            for i in range(1, int(row)):
                output += str(i) + "\n"
        return output

    def on_content_changed(event=None):
        update_line_numbers()
        update_cursor()

    def update_line_numbers(event=None):
        line_numbers = get_line_numbers()
        line_number_bar.config(state="normal")
        line_number_bar.delete("1.0", "end")
        line_number_bar.insert("1.0", line_numbers)
        line_number_bar.config(state="normal")

    # Adding Cursor Functionality
    def show_cursor():
        show_cursor_info_checked = show_cursor_info.get()
        if show_cursor_info_checked:
            cursor_info_bar.grid(row=1, column=4)

    def update_cursor(event=None):
        row, col = text.index(INSERT).split(".")
        line_num, col_num = str(int(row)), str(int(col) + 1)  # col starts at 0
        infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
        cursor_info_bar.config(text=infotext)

    # Adding Text Highlight Functionality
    def highlight_line(interval=100):

        text.tag_add("active_line", "insert linestart", "insert lineend+1c")
        text.after(interval, toggle_highlight)

    def undo_highlight():
        text.tag_remove("active_line", 1.0, "end")

    def toggle_highlight(event=None):
        if to_highlight_line.get():
            highlight_line()
        else:
            undo_highlight()

    # Adding Change Theme Functionality
    def change_theme(event=None):
        selected_theme = theme_choice.get()
        fg_bg_colors = color_schemes.get(selected_theme)
        foreground_color, background_color = fg_bg_colors.split(".")
        text.config(background=background_color, fg=foreground_color)

    # pop-up menu
    def show_popup_menu(event):
        popup_menu.tk_popup(event.x_root, event.y_root)

    ### ICONS for the compound menu
    ##new_file_icon = PhotoImage(file='icons/new_file.gif')
    ##open_file_icon = PhotoImage(file='icons/open_file.gif')
    ##save_file_icon = PhotoImage(file='icons/save.gif')
    ##cut_icon = PhotoImage(file='icons/cut.gif')
    ##copy_icon = PhotoImage(file='icons/copy.gif')
    ##paste_icon = PhotoImage(file='icons/paste.gif')
    ##undo_icon = PhotoImage(file='icons/undo.gif')
    ##redo_icon = PhotoImage(file='icons/redo.gif')
    ##find_icon = PhotoImage(file='icons/find_text.gif')

    # MENU CODES GOES HERE
    menu_bar = Menu(root)  # menu begins
    ##file_menu = Menu(menu_bar, tearoff=0)
    ##file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', image=new_file_icon, underline=0, command=new_file)
    ##file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', image=open_file_icon, underline=0, command=open_file)
    ##file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left', image=save_file_icon, underline=0, command=save)
    ##file_menu.add_command(label="Save As", accelerator='Ctrl+Shift+S', compound='left', underline=0, command = save_as)
    ##file_menu.add_separator()
    ##file_menu.add_command(label="Exit", accelerator='Alt+F4', compound='left', underline=0, command=exit_editor)
    ##menu_bar.add_cascade(label='File', menu=file_menu)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(
        label="New",
        accelerator="Ctrl+N",
        compound="left",
        underline=0,
        command=new_file,
    )
    file_menu.add_command(
        label="Open",
        accelerator="Ctrl+O",
        compound="left",
        underline=0,
        command=open_file,
    )
    file_menu.add_command(
        label="Save", accelerator="Ctrl+S", compound="left", underline=0, command=save
    )
    file_menu.add_command(
        label="Save As",
        accelerator="Ctrl+Shift+S",
        compound="left",
        underline=0,
        command=save_as,
    )
    file_menu.add_separator()
    file_menu.add_command(
        label="Exit",
        accelerator="Alt+F4",
        compound="left",
        underline=0,
        command=exit_editor,
    )
    menu_bar.add_cascade(label="File", menu=file_menu)
    # end of File Menu
    ##edit_menu = Menu(menu_bar, tearoff=0)
    ##edit_menu.add_command(label='Undo', accelerator='Ctrl + Z', compound='left', image=undo_icon, underline=0, command=undo)
    ##edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=redo_icon, underline=0, command=redo)
    ##edit_menu.add_separator()
    ##edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left',  image=cut_icon, underline=0, command=cut)
    ##edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=copy_icon, underline=0, command=copy)
    ##edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left',  image=paste_icon, underline=0, command=paste)
    ##edit_menu.add_separator()
    ##edit_menu.add_command(label='Find', accelerator='Ctrl+F', compound='left',  image=find_icon, underline=0, command=find_text)
    ##edit_menu.add_separator()
    ##edit_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=0, command=selectall)
    ##menu_bar.add_cascade(label='Edit', menu=edit_menu)
    ###end of Edit Menu

    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(
        label="Undo", accelerator="Ctrl + Z", compound="left", underline=0, command=undo
    )
    edit_menu.add_command(
        label="Redo", accelerator="Ctrl+Y", compound="left", underline=0, command=redo
    )
    edit_menu.add_separator()
    edit_menu.add_command(
        label="Cut", accelerator="Ctrl+X", compound="left", underline=0, command=cut
    )
    edit_menu.add_command(
        label="Copy", accelerator="Ctrl+C", compound="left", underline=0, command=copy
    )
    edit_menu.add_command(
        label="Paste", accelerator="Ctrl+V", compound="left", underline=0, command=paste
    )
    edit_menu.add_separator()
    edit_menu.add_command(
        label="Find",
        accelerator="Ctrl+F",
        compound="left",
        underline=0,
        command=find_text,
    )
    edit_menu.add_separator()
    edit_menu.add_command(
        label="Select All",
        accelerator="Ctrl+A",
        compound="left",
        underline=0,
        command=selectall,
    )
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    # end of Edit Menu

    view_menu = Menu(menu_bar, tearoff=0)
    show_line_number = IntVar()
    show_line_number.set(1)
    view_menu.add_checkbutton(label="Show Line Number", variable=show_line_number)
    show_cursor_info = IntVar()
    show_cursor_info.set(1)
    view_menu.add_checkbutton(
        label="Show Cursor Location at Bottom",
        variable=show_cursor_info,
        command=show_cursor,
    )
    to_highlight_line = IntVar()
    view_menu.add_checkbutton(
        label="Highlight Current Line",
        variable=to_highlight_line,
        onvalue=1,
        offvalue=0,
        command=toggle_highlight,
    )
    themes_menu = Menu(menu_bar, tearoff=0)
    view_menu.add_cascade(label="Themes", menu=themes_menu, command=change_theme)

    """ THEMES OPTIONS"""
    color_schemes = {
        "Default": "#000000.#FFFFFF",
        "Greygarious": "#83406A.#D1D4D1",
        "Aquamarine": "#5B8340.#D1E7E0",
        "Bold Beige": "#4B4620.#FFF0E1",
        "Cobalt Blue": "#ffffBB.#3333aa",
        "Olive Green": "#D1E7E0.#5B8340",
        "Night Mode": "#FFFFFF.#000000",
    }

    theme_choice = StringVar()
    theme_choice.set("Default")
    for k in sorted(color_schemes):
        themes_menu.add_radiobutton(
            label=k, variable=theme_choice, command=change_theme
        )

    menu_bar.add_cascade(label="View", menu=view_menu)

    # start of About Menu
    about_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="About", menu=about_menu)
    about_menu.add_command(label="About", underline=0, command=display_about)
    about_menu.add_command(label="Help", underline=0, command=display_help)
    # end of About Menu
    root.config(menu=menu_bar)
    # setting up the pop-up menu
    popup_menu = Menu(text)
    for i in ("cut", "copy", "paste", "undo", "redo"):

        popup_menu.add_command(label=i, compound="left", command=cmd)
    popup_menu.add_separator()
    popup_menu.add_command(label="Select All", underline=7, command=selectall)
    text.bind("<Control-N>", new_file)
    text.bind("<Control-n>", new_file)
    text.bind("<Control-O>", open_file)
    text.bind("<Control-o>", open_file)
    text.bind("<Control-S>", save)
    text.bind("<Control-s>", save)

    text.bind("<Control-Y>", redo)
    text.bind("<Control-y>", redo)
    text.bind("<Control-A>", selectall)
    text.bind("<Control-a>", selectall)
    text.bind("<Control-F>", find_text)
    text.bind("<Control-f>", find_text)

    text.bind("<KeyPress-F1>", display_help)

    text.bind("<Any-KeyPress>", on_content_changed)
    text.tag_configure("active_line", background="ivory2")

    text.bind("<Button-3>", show_popup_menu)
    text.focus_set()
    text.bind("<Button-3>", show_popup_menu)
    root.protocol("WM_DELETE_WINDOW", exit_editor)


shortcutbar = ttk.Frame(root, height=2, width=30)
shortcutbar.grid(row=0, column=1, columnspan=6, sticky="nswe")
btn1 = Button(shortcutbar, text="1", command=None)
btn1.grid(row=0, column=1)
btn2 = Button(shortcutbar, text="2", command=None)
btn2.grid(row=0, column=2)
btn3 = Button(shortcutbar, text="3", command=None)
btn3.grid(row=0, column=3)
btn4 = Button(shortcutbar, text="4", command=None)
btn4.grid(row=0, column=4)
btn5 = Button(shortcutbar, text="5", command=cmd)
btn5.grid(row=0, column=5)
btn6 = Button(shortcutbar, text="6", command=cmd)
btn6.grid(row=0, column=6)
btn7 = Button(shortcutbar, text="7", command=cmd)
btn7.grid(row=0, column=7)
btn8 = Button(shortcutbar, text="8", command=cmd)
btn8.grid(row=0, column=8)
btn9 = Button(shortcutbar, text="9", command=cmd)
btn9.grid(row=0, column=9)
btna = Button(shortcutbar, text="10", command=cmd)
btna.grid(row=0, column=10)
btnb = Button(shortcutbar, text="11", command=cmd)
btnb.grid(row=0, column=11)
btnc = Button(shortcutbar, text="12", command=cmd)
btnc.grid(row=0, column=12)
btnd = Button(shortcutbar, text="13", command=cmd)
btnd.grid(row=0, column=13)
btne = Button(shortcutbar, text="14", command=cmd)
btne.grid(row=0, column=14)
btnf = Button(shortcutbar, text="15", command=cmd)
btnf.grid(row=0, column=15)
btng = Button(shortcutbar, text="16", command=cmd)
btng.grid(row=0, column=16)
btnh = Button(shortcutbar, text="17", command=cmd)
btnh.grid(row=0, column=17)
btni = Button(shortcutbar, text="18", command=cmd)
btni.grid(row=0, column=18)
btnj = Button(shortcutbar, text="19", command=cmd)
btnj.grid(row=0, column=19)
btnk = Button(shortcutbar, text="20", command=cmd)
btnk.grid(row=0, column=20)


line_number_bar = st.ScrolledText(
    root,
    height=48,
    width=4,
    padx=3,
    takefocus=0,
    fg="purple",
    border=8,
    background="gold",
    state="disabled",
    wrap="none",
)
line_number_bar.grid(row=2, column=0, rowspan=4, sticky="w")

# adding the main context Text widget and Scrollbar Widget
##frm = ttk.Frame(root, width=100, height=48)
##frm.grid(row=2, column=1, rowspan=10, columnspan=10)

text = st.ScrolledText(root, wrap="word", bg="cyan", height=48, width=150)
text.grid(row=2, column=1, columnspan=7, rowspan=8)


cursor_info_bar = Label(root, text="Line: 1 | Column: 1")
cursor_info_bar.grid(row=39, column=2, sticky="w")


# handling binding


# END OF MENU
if __name__ == "__main__":
    main_menu()

    root.mainloop()
