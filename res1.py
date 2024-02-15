import tkinter as tk
import itertools
import math

class ResistanceCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Parallel Resistance Calculator")

        self.series_var = tk.StringVar(self.root)
        self.series_var.set('E12')  # default option
        self.tolerance_var = tk.DoubleVar(self.root)
        self.tolerance_var.set(0.05)  # default tolerance
        self.var_multiple_resistors = tk.IntVar()

        self.create_widgets()
    
    def create_widgets(self):
        # Create and place widgets
        self.entry_label = tk.Label(self.root, text="Enter Desired Resistance (Ω):")
        self.entry_label.grid(row=0, column=0, padx=10, pady=10)
        
        # ... rest of your widget creation code ...
    
    def on_submit(self):
        # Implementation of the on_submit event
        # ...

    def clear_text_area(self):
        # Implementation to clear the text area
        # ...

    def toggle_resistor_entry(self):
        # Implementation to toggle the resistor entry state
        # ...

    # Other methods like calculate_standard_values, parallel_resistance, etc.
    # ...

# Main script
if __name__ == "__main__":
    root = tk.Tk()
    app = ResistanceCalculatorApp(root)
    root.mainloop()
