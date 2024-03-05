import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 1131
        height = 661
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_6 = tk.Listbox(root)
        GListBox_6["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_6["font"] = ft
        GListBox_6["fg"] = "#333333"
        GListBox_6["justify"] = "center"
        GListBox_6.place(x=0, y=50, width=138, height=188)

        GListBox_11 = tk.Listbox(root)
        GListBox_11["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_11["font"] = ft
        GListBox_11["fg"] = "#333333"
        GListBox_11["justify"] = "center"
        GListBox_11.place(x=160, y=50, width=140, height=197)

        GListBox_906 = tk.Listbox(root)
        GListBox_906["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_906["font"] = ft
        GListBox_906["fg"] = "#333333"
        GListBox_906["justify"] = "center"
        GListBox_906.place(x=310, y=50, width=142, height=196)

        GLineEdit_753 = tk.Entry(root)
        GLineEdit_753["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_753["font"] = ft
        GLineEdit_753["fg"] = "#333333"
        GLineEdit_753["justify"] = "center"
        GLineEdit_753["text"] = "Entry"
        GLineEdit_753.place(x=30, y=10, width=70, height=25)

        GLineEdit_98 = tk.Entry(root)
        GLineEdit_98["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_98["font"] = ft
        GLineEdit_98["fg"] = "#333333"
        GLineEdit_98["justify"] = "center"
        GLineEdit_98["text"] = "Entry"
        GLineEdit_98.place(x=200, y=10, width=70, height=25)

        GLineEdit_365 = tk.Entry(root)
        GLineEdit_365["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_365["font"] = ft
        GLineEdit_365["fg"] = "#333333"
        GLineEdit_365["justify"] = "center"
        GLineEdit_365["text"] = "Entry"
        GLineEdit_365.place(x=350, y=10, width=70, height=25)

        GLabel_272 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_272["font"] = ft
        GLabel_272["fg"] = "#333333"
        GLabel_272["justify"] = "center"
        GLabel_272["text"] = "label"
        GLabel_272.place(x=30, y=250, width=70, height=25)

        GLabel_73 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_73["font"] = ft
        GLabel_73["fg"] = "#333333"
        GLabel_73["justify"] = "center"
        GLabel_73["text"] = "label"
        GLabel_73.place(x=200, y=250, width=70, height=25)

        GLabel_811 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_811["font"] = ft
        GLabel_811["fg"] = "#333333"
        GLabel_811["justify"] = "center"
        GLabel_811["text"] = "label"
        GLabel_811.place(x=350, y=250, width=70, height=25)

        GMessage_577 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_577["font"] = ft
        GMessage_577["fg"] = "#333333"
        GMessage_577["justify"] = "center"
        GMessage_577["text"] = "Message"
        GMessage_577.place(x=490, y=50, width=89, height=88)

        GButton_28 = tk.Button(root)
        GButton_28["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_28["font"] = ft
        GButton_28["fg"] = "#273134"
        GButton_28["justify"] = "center"
        GButton_28["text"] = "Button"
        GButton_28.place(x=30, y=300, width=70, height=25)
        GButton_28["command"] = self.GButton_28_command

        GButton_893 = tk.Button(root)
        GButton_893["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_893["font"] = ft
        GButton_893["fg"] = "#273134"
        GButton_893["justify"] = "center"
        GButton_893["text"] = "Button"
        GButton_893.place(x=200, y=300, width=70, height=25)
        GButton_893["command"] = self.GButton_893_command

        GButton_958 = tk.Button(root)
        GButton_958["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_958["font"] = ft
        GButton_958["fg"] = "#273134"
        GButton_958["justify"] = "center"
        GButton_958["text"] = "Button"
        GButton_958.place(x=200, y=330, width=70, height=25)
        GButton_958["command"] = self.GButton_958_command

        GButton_733 = tk.Button(root)
        GButton_733["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_733["font"] = ft
        GButton_733["fg"] = "#273134"
        GButton_733["justify"] = "center"
        GButton_733["text"] = "Button"
        GButton_733.place(x=200, y=360, width=70, height=25)
        GButton_733["command"] = self.GButton_733_command

        GButton_398 = tk.Button(root)
        GButton_398["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_398["font"] = ft
        GButton_398["fg"] = "#273134"
        GButton_398["justify"] = "center"
        GButton_398["text"] = "Button"
        GButton_398.place(x=350, y=300, width=70, height=25)
        GButton_398["command"] = self.GButton_398_command

        GButton_495 = tk.Button(root)
        GButton_495["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_495["font"] = ft
        GButton_495["fg"] = "#273134"
        GButton_495["justify"] = "center"
        GButton_495["text"] = "Button"
        GButton_495.place(x=30, y=330, width=70, height=25)
        GButton_495["command"] = self.GButton_495_command

        GButton_855 = tk.Button(root)
        GButton_855["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_855["font"] = ft
        GButton_855["fg"] = "#273134"
        GButton_855["justify"] = "center"
        GButton_855["text"] = "Button"
        GButton_855.place(x=30, y=360, width=70, height=25)
        GButton_855["command"] = self.GButton_855_command

        GButton_986 = tk.Button(root)
        GButton_986["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_986["font"] = ft
        GButton_986["fg"] = "#273134"
        GButton_986["justify"] = "center"
        GButton_986["text"] = "Button"
        GButton_986.place(x=350, y=330, width=70, height=25)
        GButton_986["command"] = self.GButton_986_command

        GButton_164 = tk.Button(root)
        GButton_164["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_164["font"] = ft
        GButton_164["fg"] = "#273134"
        GButton_164["justify"] = "center"
        GButton_164["text"] = "Button"
        GButton_164.place(x=350, y=360, width=70, height=25)
        GButton_164["command"] = self.GButton_164_command

        GButton_638 = tk.Button(root)
        GButton_638["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_638["font"] = ft
        GButton_638["fg"] = "#273134"
        GButton_638["justify"] = "center"
        GButton_638["text"] = "Button"
        GButton_638.place(x=30, y=390, width=70, height=25)
        GButton_638["command"] = self.GButton_638_command

        GButton_511 = tk.Button(root)
        GButton_511["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_511["font"] = ft
        GButton_511["fg"] = "#273134"
        GButton_511["justify"] = "center"
        GButton_511["text"] = "Button"
        GButton_511.place(x=200, y=390, width=70, height=25)
        GButton_511["command"] = self.GButton_511_command

        GButton_128 = tk.Button(root)
        GButton_128["bg"] = "#f7f7f7"
        ft = tkFont.Font(family="Times", size=10)
        GButton_128["font"] = ft
        GButton_128["fg"] = "#273134"
        GButton_128["justify"] = "center"
        GButton_128["text"] = "Button"
        GButton_128.place(x=350, y=390, width=70, height=25)
        GButton_128["command"] = self.GButton_128_command

        GRadio_857 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_857["font"] = ft
        GRadio_857["fg"] = "#333333"
        GRadio_857["justify"] = "center"
        GRadio_857["text"] = "RadioButton"
        GRadio_857.place(x=490, y=230, width=85, height=25)
        GRadio_857["command"] = self.GRadio_857_command

        GRadio_377 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_377["font"] = ft
        GRadio_377["fg"] = "#333333"
        GRadio_377["justify"] = "center"
        GRadio_377["text"] = "RadioButton"
        GRadio_377.place(x=490, y=250, width=85, height=25)
        GRadio_377["command"] = self.GRadio_377_command

        GRadio_77 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_77["font"] = ft
        GRadio_77["fg"] = "#333333"
        GRadio_77["justify"] = "center"
        GRadio_77["text"] = "RadioButton"
        GRadio_77.place(x=490, y=270, width=85, height=25)
        GRadio_77["command"] = self.GRadio_77_command

        GRadio_983 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_983["font"] = ft
        GRadio_983["fg"] = "#333333"
        GRadio_983["justify"] = "center"
        GRadio_983["text"] = "RadioButton"
        GRadio_983.place(x=490, y=290, width=85, height=25)
        GRadio_983["command"] = self.GRadio_983_command

        GRadio_680 = tk.Radiobutton(root)
        ft = tkFont.Font(family="Times", size=10)
        GRadio_680["font"] = ft
        GRadio_680["fg"] = "#333333"
        GRadio_680["justify"] = "center"
        GRadio_680["text"] = "RadioButton"
        GRadio_680.place(x=490, y=310, width=85, height=25)
        GRadio_680["command"] = self.GRadio_680_command

        GMessage_194 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_194["font"] = ft
        GMessage_194["fg"] = "#333333"
        GMessage_194["justify"] = "center"
        GMessage_194["text"] = "Message"
        GMessage_194.place(x=20, y=440, width=80, height=25)

        GMessage_723 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_723["font"] = ft
        GMessage_723["fg"] = "#333333"
        GMessage_723["justify"] = "center"
        GMessage_723["text"] = "Message"
        GMessage_723.place(x=200, y=440, width=80, height=25)

        GMessage_278 = tk.Message(root)
        ft = tkFont.Font(family="Times", size=10)
        GMessage_278["font"] = ft
        GMessage_278["fg"] = "#333333"
        GMessage_278["justify"] = "center"
        GMessage_278["text"] = "Message"
        GMessage_278.place(x=350, y=440, width=80, height=25)

        GLineEdit_551 = tk.Entry(root)
        GLineEdit_551["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_551["font"] = ft
        GLineEdit_551["fg"] = "#333333"
        GLineEdit_551["justify"] = "center"
        GLineEdit_551["text"] = "Entry"
        GLineEdit_551.place(x=730, y=90, width=323, height=85)

        GLabel_707 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_707["font"] = ft
        GLabel_707["fg"] = "#333333"
        GLabel_707["justify"] = "center"
        GLabel_707["text"] = "label"
        GLabel_707.place(x=860, y=40, width=70, height=25)

        GLabel_124 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_124["font"] = ft
        GLabel_124["fg"] = "#333333"
        GLabel_124["justify"] = "center"
        GLabel_124["text"] = "label"
        GLabel_124.place(x=500, y=190, width=70, height=25)

        GLineEdit_398 = tk.Entry(root)
        GLineEdit_398["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GLineEdit_398["font"] = ft
        GLineEdit_398["fg"] = "#333333"
        GLineEdit_398["justify"] = "center"
        GLineEdit_398["text"] = "Entry"
        GLineEdit_398.place(x=620, y=190, width=498, height=444)

    def GButton_28_command(self):
        print("command")

    def GButton_893_command(self):
        print("command")

    def GButton_958_command(self):
        print("command")

    def GButton_733_command(self):
        print("command")

    def GButton_398_command(self):
        print("command")

    def GButton_495_command(self):
        print("command")

    def GButton_855_command(self):
        print("command")

    def GButton_986_command(self):
        print("command")

    def GButton_164_command(self):
        print("command")

    def GButton_638_command(self):
        print("command")

    def GButton_511_command(self):
        print("command")

    def GButton_128_command(self):
        print("command")

    def GRadio_857_command(self):
        print("command")

    def GRadio_377_command(self):
        print("command")

    def GRadio_77_command(self):
        print("command")

    def GRadio_983_command(self):
        print("command")

    def GRadio_680_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
