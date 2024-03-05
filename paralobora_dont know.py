import tkinter as tk
from tkinter import Tk

# Adding a Tk window
root = tk.Tk()
root.geometry("640x480")  # Configuring the resolution

# Adding the canvas to put the graph on it


canvas_width = 1800
canvas_height = 900
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=0, column=0)


def draw_axis(
    canvas_object,
):  # a function in order to draw the horizontal and vertical lines and setting the scroll
    canvas_object.update()
    x_origin = canvas_object.winfo_width() // 2
    y_origin = canvas_object.winfo_height() // 2
    canvas_object.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas_object.create_line(x_origin, 0, -x_origin, 0)
    canvas_object.create_line(0, y_origin, 0, -y_origin)


def parabola(number, size):  # Calculating the parabola
    result = number * number // size
    return result


def plot(canvas_object, size, color):  # The grand function to do the plotting process
    y_location = []
    x_location = []
    for each in range(-size, size + 1):
        y_location.append(parabola(each, size))
        x_location.append(each)
    for each_of in range(0, size * 2 + 2):
        if each_of <= size * 2 - 1:
            canvas_object.create_line(
                x_location[each_of],
                -y_location[each_of],
                x_location[each_of + 1],
                -y_location[each_of + 1],
                fill=str(color),
            )
            print(
                "A line from X location of {} and Y location of {} to the X location of {} and Y location of {} was"
                " drawn, Color = {}".format(
                    x_location[each_of],
                    y_location[each_of],
                    x_location[each_of + 1],
                    y_location[each_of + 1],
                    color,
                )
            )
        else:
            break


def checkered(canvas, line_distance):
    # vertical lines at an interval of "line_distance" pixel
    for x in range(line_distance, canvas_width, line_distance):
        canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    # horizontal lines at an interval of "line_distance" pixel
    for y in range(line_distance, canvas_height, line_distance):
        canvas.create_line(0, y, canvas_width, y, fill="#476042")

        canvas.create_line(10, 450, 1800, 450, fill="black", width=4)
    canvas.create_line(900, 10, 900, 900, fill="black", width=4)
    ##########################################################

    canvas.create_line(50, 440, 50, 460, fill="blue", width=4)
    canvas.create_line(100, 440, 100, 460, fill="blue", width=4)
    canvas.create_line(150, 440, 150, 460, fill="blue", width=4)
    canvas.create_line(200, 440, 200, 460, fill="blue", width=4)
    canvas.create_line(250, 440, 250, 460, fill="blue", width=4)
    canvas.create_line(300, 440, 300, 460, fill="blue", width=4)
    canvas.create_line(350, 440, 350, 460, fill="blue", width=4)
    canvas.create_line(400, 440, 400, 460, fill="blue", width=4)
    canvas.create_line(450, 440, 450, 460, fill="blue", width=4)
    canvas.create_line(500, 440, 500, 460, fill="blue", width=4)
    canvas.create_line(550, 440, 550, 460, fill="blue", width=4)
    canvas.create_line(600, 440, 600, 460, fill="blue", width=4)
    canvas.create_line(650, 440, 650, 460, fill="blue", width=4)
    canvas.create_line(700, 440, 700, 460, fill="blue", width=4)
    canvas.create_line(750, 440, 750, 460, fill="blue", width=4)
    canvas.create_line(800, 440, 800, 460, fill="blue", width=4)
    canvas.create_line(850, 440, 850, 460, fill="blue", width=4)
    canvas.create_line(900, 440, 900, 460, fill="blue", width=4)
    canvas.create_line(950, 440, 950, 460, fill="blue", width=4)
    canvas.create_line(1000, 440, 1000, 460, fill="blue", width=4)
    canvas.create_line(1050, 440, 1050, 460, fill="blue", width=4)
    canvas.create_line(1100, 440, 1100, 460, fill="blue", width=4)
    canvas.create_line(1150, 440, 1150, 460, fill="blue", width=4)
    canvas.create_line(1200, 440, 1200, 460, fill="blue", width=4)
    canvas.create_line(1250, 440, 1250, 460, fill="blue", width=4)
    canvas.create_line(1300, 440, 1300, 460, fill="blue", width=4)
    canvas.create_line(1350, 440, 1350, 460, fill="blue", width=4)
    canvas.create_line(1400, 440, 1400, 460, fill="blue", width=4)
    canvas.create_line(1450, 440, 1450, 460, fill="blue", width=4)
    canvas.create_line(1500, 440, 1500, 460, fill="blue", width=4)
    canvas.create_line(1550, 440, 1550, 460, fill="blue", width=4)
    canvas.create_line(1600, 440, 1600, 460, fill="blue", width=4)
    canvas.create_line(1650, 440, 1650, 460, fill="blue", width=4)
    canvas.create_line(1700, 440, 1700, 460, fill="blue", width=4)
    canvas.create_line(1750, 440, 1750, 460, fill="blue", width=4)
    canvas.create_line(1800, 440, 1800, 460, fill="blue", width=4)

    ##########################################################
    canvas.create_line(890, 20, 910, 20, fill="blue", width=4)
    canvas.create_line(890, 30, 910, 30, fill="blue", width=4)
    canvas.create_line(890, 50, 910, 50, fill="blue", width=4)
    canvas.create_line(890, 100, 910, 100, fill="blue", width=4)
    canvas.create_line(890, 150, 910, 150, fill="blue", width=4)
    canvas.create_line(890, 200, 910, 200, fill="blue", width=4)
    canvas.create_line(890, 250, 910, 250, fill="blue", width=4)
    canvas.create_line(890, 300, 910, 300, fill="blue", width=4)
    canvas.create_line(890, 350, 910, 350, fill="blue", width=4)
    canvas.create_line(890, 400, 910, 400, fill="blue", width=4)
    canvas.create_line(890, 450, 910, 450, fill="blue", width=4)
    canvas.create_line(890, 500, 910, 500, fill="blue", width=4)
    canvas.create_line(890, 550, 910, 550, fill="blue", width=4)
    canvas.create_line(890, 600, 910, 600, fill="blue", width=4)
    canvas.create_line(890, 650, 910, 650, fill="blue", width=4)
    canvas.create_line(890, 700, 910, 700, fill="blue", width=4)
    canvas.create_line(890, 750, 910, 750, fill="blue", width=4)
    canvas.create_line(890, 800, 910, 800, fill="blue", width=4)
    canvas.create_line(890, 850, 910, 850, fill="blue", width=4)
    canvas.create_line(890, 900, 910, 900, fill="blue", width=4)
    canvas.create_line(890, 950, 910, 950, fill="blue", width=4)
    canvas.create_line(900, 1000, 910, 1000, fill="blue", width=4)


if __name__ == "__main__":
    checkered(canvas, 10)

    draw_axis(canvas)
    plot(canvas, 500, "red")
    root.mainloop()  # running the window
