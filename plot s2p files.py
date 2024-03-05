import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import numpy as np


def get_filename():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    filename = filedialog.askopenfilename(
        title="Select an S2P file",
        filetypes=[("S2P files", "*.s2p"), ("All files", "*.*")],
    )
    return filename


def read_s2p(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    frequencies = []
    s11 = []
    s21 = []
    s12 = []
    s22 = []

    for line in lines:
        if not line.startswith("!") and not line.startswith("#"):
            data = line.split()
            frequencies.append(float(data[0]))
            s11.append(complex(float(data[1]), float(data[2])))
            s21.append(complex(float(data[3]), float(data[4])))
            s12.append(complex(float(data[5]), float(data[6])))
            s22.append(complex(float(data[7]), float(data[8])))

    return frequencies, s11, s21, s12, s22


# Use the dialog to get the filename
filename = get_filename()

# Make sure a file was selected
if filename:
    # Read the data
    frequencies, s11, s21, s12, s22 = read_s2p(filename)

    # Plot magnitude of S21
    plt.figure()
    plt.plot(frequencies, [abs(s) for s in s21], label="|S21|")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title("S21 Magnitude vs. Frequency")
    plt.legend()
    plt.grid(True)
    plt.show()
