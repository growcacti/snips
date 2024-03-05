import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("150x75")

panedwindow = tk.PanedWindow(showhandle=True,sashrelief=tk.SUNKEN)

leftLabel = tk.Label(panedwindow, text="Left Label")
panedwindow.add(leftLabel)

rightLabel = tk.Label(panedwindow, text="Right Pane")
panedwindow.add(rightLabel)

panedwindow.pack(fill=tk.BOTH, expand=True)

app.mainloop()
