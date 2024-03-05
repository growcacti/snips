import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_13=tk.Listbox(root)
        GListBox_13["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_13["font"] = ft
        GListBox_13["fg"] = "#0b0c1b"
        GListBox_13["justify"] = "center"
        GListBox_13.place(x=90,y=80,width=104,height=283)

        GListBox_144=tk.Listbox(root)
        GListBox_144["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_144["font"] = ft
        GListBox_144["fg"] = "#0b0c1b"
        GListBox_144["justify"] = "center"
        GListBox_144.place(x=210,y=80,width=70,height=282)

        GListBox_688=tk.Listbox(root)
        GListBox_688["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_688["font"] = ft
        GListBox_688["fg"] = "#0b0c1b"
        GListBox_688["justify"] = "center"
        GListBox_688.place(x=300,y=80,width=60,height=283)

        GLineEdit_39=tk.Entry(root)
        GLineEdit_39["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_39["font"] = ft
        GLineEdit_39["fg"] = "#0b0c1b"
        GLineEdit_39["justify"] = "center"
        GLineEdit_39["text"] = "Entry"
        GLineEdit_39.place(x=80,y=390,width=370,height=25)

        GButton_1=tk.Button(root)
        GButton_1["bg"] = "#f6f5f4"
        ft = tkFont.Font(family='Times',size=10)
        GButton_1["font"] = ft
        GButton_1["fg"] = "#2e3436"
        GButton_1["justify"] = "center"
        GButton_1["text"] = "Execute"
        GButton_1.place(x=230,y=450,width=70,height=25)
        GButton_1["command"] = self.GButton_1_command

        GButton_300=tk.Button(root)
        GButton_300["bg"] = "#f6f5f4"
        ft = tkFont.Font(family='Times',size=10)
        GButton_300["font"] = ft
        GButton_300["fg"] = "#2e3436"
        GButton_300["justify"] = "center"
        GButton_300["text"] = "Quit"
        GButton_300.place(x=150,y=450,width=70,height=25)
        GButton_300["command"] = self.GButton_300_command

        GButton_377=tk.Button(root)
        GButton_377["bg"] = "#f6f5f4"
        ft = tkFont.Font(family='Times',size=10)
        GButton_377["font"] = ft
        GButton_377["fg"] = "#2e3436"
        GButton_377["justify"] = "center"
        GButton_377["text"] = "Reset"
        GButton_377.place(x=310,y=450,width=70,height=25)
        GButton_377["command"] = self.GButton_377_command

    def GButton_1_command(self):
        print("command")


    def GButton_300_command(self):
        print("command")


    def GButton_377_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
