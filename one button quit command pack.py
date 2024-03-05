import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

def quitCommand():
    quit()

button = tk.Button(text="Quit", command=quitCommand)
button.pack()

app.mainloop()
