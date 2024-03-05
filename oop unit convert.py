import tkinter as tk
from tkinter import ttk, END


class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors

    def convert(self, unit1, unit2, value):
        if unit1 in self.conversion_factors and unit2 in self.conversion_factors[unit1]:
            factor = self.conversion_factors[unit1][unit2]
            converted_value = value * factor
            return converted_value, unit2
        else:
            return None


class LengthUnitConverter(UnitConverter):
    def __init__(self):
        conversion_factors = {
            "cm": {
                "inch": 1 / 2.54,
                "mm": 10,
                "m": 0.01,
                "ft": 1 / 30.48,
                "mi": 1 / 160934.4,
            },
            "inch": {
                "cm": 2.54,
                "mm": 25.4,
                "m": 0.0254,
                "ft": 1 / 12,
                "mi": 1 / 63360,
            },
            "m": {
                "cm": 100,
                "inch": 39.37,
                "mm": 1000,
                "ft": 3.28084,
                "mi": 0.000621371,
            },
            "ft": {"cm": 30.48, "inch": 12, "mm": 304.8, "m": 0.3048, "mi": 1 / 5280},
            "km": {
                "mi": 0.621371,
                "ft": 3280.84,
                "inch": 39370.1,
                "cm": 100000,
                "mm": 1000000,
                "m": 1000,
            },
        }
        super().__init__(conversion_factors)


class LiquidUnitConverter(UnitConverter):
    def __init__(self):
        conversion_factors = {
            "ml": {
                "liters": 0.001,
                "fl oz": 0.033814,
                "cup": 0.00416667,
                "pint": 0.00211338,
                "quart": 0.00105669,
                "gallon": 0.000264172,
            },
            "liters": {
                "ml": 1000,
                "fl oz": 33.814,
                "cup": 4.16667,
                "pint": 2.11338,
                "quart": 1.05669,
                "gallon": 0.264172,
            },
            "fl oz": {
                "ml": 29.5735,
                "liters": 0.0295735,
                "cup": 0.123223,
                "pint": 0.0625,
                "quart": 0.03125,
                "gallon": 0.0078125,
            },
            "cup": {
                "ml": 240,
                "liters": 0.24,
                "fl oz": 8.11537,
                "pint": 0.50721,
                "quart": 0.253605,
                "gallon": 0.0634013,
            },
            "pint": {
                "ml": 473.176,
                "liters": 0.473176,
                "fl oz": 16,
                "cup": 1.97157,
                "quart": 0.5,
                "gallon": 0.125,
            },
            "quart": {
                "ml": 946.353,
                "liters": 0.946353,
                "fl oz": 32,
                "cup": 3.94314,
                "pint": 2,
                "gallon": 0.25,
            },
            "gallon": {
                "ml": 3785.41,
                "liters": 3.78541,
                "fl oz": 128,
                "cup": 15.7725,
                "pint": 7.74597,
                "quart": 4,
            },
        }
        super().__init__(conversion_factors)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unit Converter")
        self.geometry("600x350")

        self.length_converter = LengthUnitConverter()
        self.liquid_converter = LiquidUnitConverter()

        length_units = list(self.length_converter.conversion_factors.keys())
        liquid_units = list(self.liquid_converter.conversion_factors.keys())

        tk.Label(self, text="Length").grid(row=0, column=0)
        tk.Label(self, text="-").grid(row=1, column=0)
        tk.Label(self, text="_").grid(row=2, column=0)
        tk.Label(self, text="_").grid(row=3, column=0)

        self.e1_length = tk.Entry(self, bd=5, bg="seashell")
        self.e1_length.grid(row=0, column=1)

        self.cb1_length = ttk.Combobox(self, values=length_units)
        self.cb1_length.grid(row=0, column=2)

        self.cb2_length = ttk.Combobox(self, values=length_units)
        self.cb2_length.grid(row=2, column=3)

        self.lb1_length = tk.Listbox(self, width=30)
        self.lb1_length.grid(row=5, column=0)

        self.lb2_length = tk.Listbox(self, width=30)
        self.lb2_length.grid(row=5, column=1)

        tk.Label(self, text="Liquid").grid(row=7, column=0)
        tk.Label(self, text="-").grid(row=8, column=0)
        tk.Label(self, text="_").grid(row=9, column=0)
        tk.Label(self, text="_").grid(row=10, column=0)

        self.e1_liquid = tk.Entry(self, bd=5, bg="seashell")
        self.e1_liquid.grid(row=7, column=1)

        self.cb1_liquid = ttk.Combobox(self, values=liquid_units)
        self.cb1_liquid.grid(row=7, column=2)

        self.cb2_liquid = ttk.Combobox(self, values=liquid_units)
        self.cb2_liquid.grid(row=9, column=3)

        self.lb1_liquid = tk.Listbox(self, width=30)
        self.lb1_liquid.grid(row=12, column=0)

        self.lb2_liquid = tk.Listbox(self, width=30)
        self.lb2_liquid.grid(row=12, column=1)

        self.btn_length = tk.Button(
            self,
            text="Calculate Length",
            bd=5,
            bg="light green",
            command=self.convert_length,
        )
        self.btn_length.grid(row=4, column=0)

        self.btn_liquid = tk.Button(
            self,
            text="Calculate Liquid",
            bd=5,
            bg="light green",
            command=self.convert_liquid,
        )
        self.btn_liquid.grid(row=11, column=0)

        self.btn_clear = tk.Button(
            self, text="Clear", bd=5, bg="light blue", command=self.clear
        )
        self.btn_clear.grid(row=4, column=1)

    def convert_length(self):
        try:
            unit1 = self.cb1_length.get()
            unit2 = self.cb2_length.get()
            value = float(self.e1_length.get())

            result = self.length_converter.convert(unit1, unit2, value)
            if result is not None:
                converted_value, converted_unit = result
                self.lb1_length.insert(0, converted_value)
                self.lb2_length.insert(0, converted_unit)

        except ValueError:
            pass

    def convert_liquid(self):
        try:
            unit1 = self.cb1_liquid.get()
            unit2 = self.cb2_liquid.get()
            value = float(self.e1_liquid.get())

            result = self.liquid_converter.convert(unit1, unit2, value)
            if result is not None:
                converted_value, converted_unit = result
                self.lb1_liquid.insert(0, converted_value)
                self.lb2_liquid.insert(0, converted_unit)

        except ValueError:
            pass

    def clear(self):
        self.e1_length.delete(0, END)
        self.e1_liquid.delete(0, END)
        self.lb1_length.delete(0, END)
        self.lb2_length.delete(0, END)
        self.lb1_liquid.delete(0, END)
        self.lb2_liquid.delete(0, END)


app = App()
app.mainloop()
