import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x150")

scale = tk.Scale()
scale.pack()

scale = tk.Scale(orient=tk.HORIZONTAL)
scale.pack()

app.mainloop()
