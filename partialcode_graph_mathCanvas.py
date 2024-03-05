f8 = ttk.Frame(notebook)
f8.grid(row=0, column=0)

notebook.add(f8, text="2")


def grid1(canvas, line_distance):
    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")


canvas_width = 1800
canvas_height = 900
boo = Canvas(f8, width=canvas_width, height=canvas_height)
boo.grid(row=0, column=0)
boo.create_line(10, 450, 1800, 450, fill="black", width=4)
boo.create_line(900, 10, 900, 900, fill="black", width=4)

grid1(boo, 10)
##########################################################

boo.create_line(50, 440, 50, 460, fill="blue", width=4)
boo.create_line(100, 440, 100, 460, fill="blue", width=4)
boo.create_line(150, 440, 150, 460, fill="blue", width=4)
boo.create_line(200, 440, 200, 460, fill="blue", width=4)
boo.create_line(250, 440, 250, 460, fill="blue", width=4)
boo.create_line(300, 440, 300, 460, fill="blue", width=4)
boo.create_line(350, 440, 350, 460, fill="blue", width=4)
boo.create_line(400, 440, 400, 460, fill="blue", width=4)
boo.create_line(450, 440, 450, 460, fill="blue", width=4)
boo.create_line(500, 440, 500, 460, fill="blue", width=4)
boo.create_line(550, 440, 550, 460, fill="blue", width=4)
boo.create_line(600, 440, 600, 460, fill="blue", width=4)
boo.create_line(650, 440, 650, 460, fill="blue", width=4)
boo.create_line(700, 440, 700, 460, fill="blue", width=4)
boo.create_line(750, 440, 750, 460, fill="blue", width=4)
boo.create_line(800, 440, 800, 460, fill="blue", width=4)
boo.create_line(850, 440, 850, 460, fill="blue", width=4)
boo.create_line(900, 440, 900, 460, fill="blue", width=4)
boo.create_line(950, 440, 950, 460, fill="blue", width=4)
boo.create_line(1000, 440, 1000, 460, fill="blue", width=4)
boo.create_line(1050, 440, 1050, 460, fill="blue", width=4)
boo.create_line(1100, 440, 1100, 460, fill="blue", width=4)
boo.create_line(1150, 440, 1150, 460, fill="blue", width=4)
boo.create_line(1200, 440, 1200, 460, fill="blue", width=4)
boo.create_line(1250, 440, 1250, 460, fill="blue", width=4)
boo.create_line(1300, 440, 1300, 460, fill="blue", width=4)
boo.create_line(1350, 440, 1350, 460, fill="blue", width=4)
boo.create_line(1400, 440, 1400, 460, fill="blue", width=4)
boo.create_line(1450, 440, 1450, 460, fill="blue", width=4)
boo.create_line(1500, 440, 1500, 460, fill="blue", width=4)
boo.create_line(1550, 440, 1550, 460, fill="blue", width=4)
boo.create_line(1600, 440, 1600, 460, fill="blue", width=4)
boo.create_line(1650, 440, 1650, 460, fill="blue", width=4)
boo.create_line(1700, 440, 1700, 460, fill="blue", width=4)
boo.create_line(1750, 440, 1750, 460, fill="blue", width=4)
boo.create_line(1800, 440, 1800, 460, fill="blue", width=4)

##########################################################
boo.create_line(890, 20, 910, 20, fill="blue", width=4)
boo.create_line(890, 30, 910, 30, fill="blue", width=4)
boo.create_line(890, 50, 910, 50, fill="blue", width=4)
boo.create_line(890, 100, 910, 100, fill="blue", width=4)
boo.create_line(890, 150, 910, 150, fill="blue", width=4)
boo.create_line(890, 200, 910, 200, fill="blue", width=4)
boo.create_line(890, 250, 910, 250, fill="blue", width=4)
boo.create_line(890, 300, 910, 300, fill="blue", width=4)
boo.create_line(890, 350, 910, 350, fill="blue", width=4)
boo.create_line(890, 400, 910, 400, fill="blue", width=4)
boo.create_line(890, 450, 910, 450, fill="blue", width=4)
boo.create_line(890, 500, 910, 500, fill="blue", width=4)
boo.create_line(890, 550, 910, 550, fill="blue", width=4)
boo.create_line(890, 600, 910, 600, fill="blue", width=4)
boo.create_line(890, 650, 910, 650, fill="blue", width=4)
boo.create_line(890, 700, 910, 700, fill="blue", width=4)
boo.create_line(890, 750, 910, 750, fill="blue", width=4)
boo.create_line(890, 800, 910, 800, fill="blue", width=4)
boo.create_line(890, 850, 910, 850, fill="blue", width=4)
boo.create_line(890, 900, 910, 900, fill="blue", width=4)
boo.create_line(890, 950, 910, 950, fill="blue", width=4)
boo.create_line(900, 1000, 910, 1000, fill="blue", width=4)

#####################################################################################
boo.create_text(300, 50, text="300x50", fill="black", font=("URW Chancery L", 15))
boo.create_text(300, 450, text="300x450", fill="black", font=("URW Chancery L", 15))
boo.create_text(50, 450, text="50x450", fill="black", font=("URW Chancery L", 15))
boo.create_text(800, 800, text="800x800", fill="black", font=("URW Chancery L", 15))
boo.create_text(400, 600, text="400x600", fill="black", font=("URW Chancery L", 15))
boo.create_text(200, 150, text="200x150", fill="black", font=("URW Chancery L", 15))
boo.create_text(1300, 500, text="1300x500", fill="black", font=("URW Chancery L", 15))
boo.create_text(1700, 800, text="1700x800", fill="black", font=("URW Chancery L", 15))
boo.create_text(1600, 250, text="1600x250", fill="black", font=("URW Chancery L", 15))
boo.create_text(1500, 150, text="1500x150", fill="black", font=("URW Chancery L", 15))
boo.create_text(1400, 650, text="1400x650", fill="black", font=("URW Chancery L", 15))

boo.create_text(1200, 700, text="1200x700", fill="black", font=("URW Chancery L", 15))
boo.create_text(1100, 900, text="1100x900", fill="black", font=("URW Chancery L", 15))
boo.create_text(1000, 50, text="1000x50", fill="black", font=("URW Chancery L", 15))
boo.create_text(900, 750, text="900x750", fill="black", font=("URW Chancery L", 15))
