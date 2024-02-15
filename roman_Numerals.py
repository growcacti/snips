import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import re

class RomanConverter:
    romanNumeralMap = (
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1),
    )
    
    romanNumeralPattern = re.compile("""
        ^                   # beginning of string
        M{0,4}              # thousands
        (CM|CD|D?C{0,3})    # hundreds
        (XC|XL|L?X{0,3})    # tens
        (IX|IV|V?I{0,3})    # ones
        $                   # end of string
    """, re.VERBOSE)
    
    def toRoman(self, n):
        if not (0 < n and n < 5000):
            raise OutOfRangeError("number out of range (must be 1..4999)")
        if int(n) != n:
            raise NotIntegerError("decimals can not be converted")

        result = ""
        for numeral, integer in self.romanNumeralMap:
            while n >= integer:
                result += numeral
                n -= integer
        return result

    def fromRoman(self, s):
        if not s:
            raise InvalidRomanNumeralError("Input can not be blank")
        if not self.romanNumeralPattern.search(s):
            raise InvalidRomanNumeralError(f"Invalid Roman numeral: {s}")

        result = 0
        index = 0
        for numeral, integer in self.romanNumeralMap:
            while s[index : index + len(numeral)] == numeral:
                result += integer
                index += len(numeral)
        return result


class RomanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Convert Integer to Roman Numeral")
        self.geometry("500x500")
        self.resizable(True, True)

        self.converter = RomanConverter()

        self.init_widgets()

    def init_widgets(self):
        self.lb = tk.Listbox(self)
        self.lb.grid(row=3, column=0)

        self.p = tk.StringVar()
        self.sp = tk.Entry(self, textvariable=self.p)
        self.sp.grid(row=1, column=0)

        self.bnt = tk.Button(
            self,
            text="get Roman Number",
            bg="light green",
            command=self.display_roman
        )
        self.bnt.grid(row=2, column=0)
        self.bnt2 = tk.Button(self, text="clear", bg="light blue", command=self.clearlist)
        self.bnt2.grid(row=4, column=0)

    def display_roman(self):
        try:
            roman = self.converter.toRoman(int(self.sp.get()))
            self.lb.insert(tk.END, roman)
        except Exception as e:
            showinfo("Error", str(e))

    def clearlist(self):
        self.lb.delete(0, tk.END)


if __name__ == "__main__":
    app = RomanApp()
    app.mainloop()
