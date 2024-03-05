import tkinter as tk
import math

class MathApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x300')
        self.root.title("JH Math APPS")

        self.lboxx3 = tk.Listbox(root, width=20)
        self.lboxx3.grid(row=10, column=4)
        self.lboxx4 = tk.Listbox(root, width=20)
        self.lboxx4.grid(row=10, column=5)
        self.hex_table = {hex(i)[2:]: i for i in range(16)}  # Use [:2] to strip off the leading '0x'

        self.values = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f",
        }

        self.en1 = tk.Entry(root, bg="wheat")
        self.en1.grid(row=1, column=1)
        self.en2 = tk.Entry(root, bg="wheat")
        self.en2.grid(row=1, column=3)
        self.en3 = tk.Entry(root, bg="wheat")
        self.en3.grid(row=1, column=4)
        self.en4 = tk.Entry(root, bg="wheat")
        self.en4.grid(row=1, column=5)

        self.label1 = tk.Label(root, text=" HEX")
        self.label1.grid(row=1, column=2)
        tk.Label(root, text="Hex").grid(row=5, column=2)
        tk.Label(root, text=" Oct").grid(row=5, column=3)
        tk.Label(root, text="Decimal").grid(row=5, column=4)
        tk.Label(root, text="Bin").grid(row=5, column=5)

        self.en5 = tk.Entry(root, bg="wheat")
        self.en5.grid(row=18, column=1)
        self.sp = tk.Spinbox(root, from_=2, to=36, increment=1, font=('sans-serif', 10))
        self.sp.grid(row=18, column=2)

        self.lboxx1 = tk.Listbox(root)
        self.lboxx1.grid(row=10, column=2)

        # Add button to perform the conversion
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_number)
        self.convert_button.grid(row=18, column=3)

        # Add button to clear the lists
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_lists)
        self.clear_button.grid(row=19, column=3)

    def convert_number(self):
        num = self.en1.get()
        hex_num = self.en2.get()
        oct_num = self.en3.get()
        bin_num = self.en4.get()
        base = int(self.sp.get())

        if num:
            self.hex_to_decimal(num)
            self.hex_to_bin(num)

        if hex_num:
            self.hex_to_decimal(hex_num)

        if oct_num:
            self.oct_to_decimal(oct_num)

        if bin_num:
            self.bin_to_decimal(bin_num)
            self.bin_to_octal(bin_num)

    def hex_to_decimal(self, hex_string):
        # Implementation of the hex_to_decimal function

    def hex_to_bin(self, hex_num):
        # Implementation of the hex_to_bin function

    def oct_to_decimal(self, oct_string):
        # Implementation of the oct_to_decimal function

    def bin_to_decimal(self, bin_string):
        # Implementation of the bin_to_decimal function

    def bin_to_octal(self, bin_string):
        # Implementation of the bin_to_octal function

    def clear_lists(self):
        self.lboxx1.delete(0, tk.END)
        self.lboxx3.delete(0, tk.END)
        self.lboxx4.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = MathApp(root)
    root.mainloop()
