import tkinter as tk


from tkinter import *

from tkinter import ttk

from tkinter import filedialog as fd

from tkinter import messagebox as mb

import os

import subprocess

import shutil


root = tk.Tk()

root.geometry("1920x1080")


frm = Frame(root, height=1000, width=1900)

frm.grid(row=0, rowspan=5, column=0, columnspan=5)

canvas = Canvas(frm, height=500, width=600)


canvas.grid(row=0, rowspan=10, column=0, columnspan=10)

line = canvas.create_line(80, 70, 110, 70, fill="black", width=4)


line = canvas.create_line(110, 70, 130, 90, fill="black", width=4)


line2 = canvas.create_line(130, 90, 150, 70, fill="black", width=4)


line3 = canvas.create_line(150, 70, 170, 90, fill="black", width=4)


line4 = canvas.create_line(170, 90, 190, 70, fill="black", width=4)


line5 = canvas.create_line(190, 70, 210, 90, fill="black", width=4)


line6 = canvas.create_line(210, 90, 230, 70, fill="black", width=4)


line7 = canvas.create_line(230, 70, 250, 90, fill="black", width=4)


line8 = canvas.create_line(250, 90, 280, 90, fill="black", width=4)


inbetween = canvas.create_line(250, 90, 380, 90, fill="black", width=4)


l = canvas.create_line(380, 90, 410, 90, fill="black", width=4)


line = canvas.create_line(410, 90, 430, 70, fill="black", width=4)


l2 = canvas.create_line(430, 70, 450, 90, fill="black", width=4)


l3 = canvas.create_line(450, 90, 470, 70, fill="black", width=4)


l4 = canvas.create_line(470, 70, 490, 90, fill="black", width=4)


l5 = canvas.create_line(490, 90, 510, 70, fill="black", width=4)


l6 = canvas.create_line(510, 70, 530, 90, fill="black", width=4)


l7 = canvas.create_line(530, 90, 550, 70, fill="black", width=4)


l8 = canvas.create_line(550, 70, 570, 90, fill="black", width=4)


l9 = canvas.create_line(570, 90, 570, 420, fill="black", width=4)


l10 = canvas.create_line(530, 420, 610, 420, fill="black", width=4)


l11 = canvas.create_line(555, 440, 585, 440, fill="black", width=4)


l12 = canvas.create_line(565, 460, 575, 460, fill="black", width=4)


l15 = canvas.create_line(40, 280, 120, 280, fill="black", width=4)

l17 = canvas.create_line(80, 70, 80, 280, fill="black", width=4)

l18 = canvas.create_line(60, 300, 100, 300, fill="black", width=4)


l118 = canvas.create_line(80, 300, 80, 420, fill="black", width=4)


gndl20 = canvas.create_line(40, 420, 120, 420, fill="black", width=4)

gndl21 = canvas.create_line(60, 440, 100, 440, fill="black", width=4)


gndl22 = canvas.create_line(75, 460, 85, 460, fill="black", width=4)


##l19 = canvas.create_line(40, 280, 120, 280, fill ='black', width = 4)

##l20 = canvas.create_line(80 ,70, 80, 280, fill ='black', width = 4)

##

##l14 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

##

##    line6 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

# 7

##    line7 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

##

##    line8 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)


def checkered(canvas, line_distance):

    for line in range(0, width, 10):  # range(start, stop, step)

        canvas.create_line(
            [(line, 0), (line, height)], fill="black", tags="grid_line_w"
        )

        canvas.create_line(x, y, x2, y2, fill="#476042")

    for line in range(0, height, 10):

        canvas.create_line([(0, line), (width, line)], fill="black", tags="grid_line_h")

        canvas.create_line(x, y, x2, y2, fill="#476042")


def lines():

    ##    line5 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line6 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line7 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line8 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##

    ##    line9 = canvas.create_line(480, 70, 510, 70, fill ='black', width = 4)

    ##

    ##

    ##    line10 = canvas.create_line(510,70, 530, 90, fill ='black', width = 4)

    ##

    ##    line11 = canvas.create_line(530,90, 550, 70, fill ='black', width = 4)

    ##

    ##    line12 = canvas.create_line(550,70, 570, 90, fill ='black', width = 4)

    ##

    ##    line13 = canvas.create_line(570, 90, 590, 70, fill ='black', width = 4)

    ##

    ##    line14 = canvas.create_line(590, 70, 610, 90, fill ='black', width = 4)

    ##

    ##    line15 = canvas.create_line(610, 90, 630, 70, fill ='black', width = 4)

    ##

    ##    line16 = canvas.create_line(630, 70, 650, 90, fill ='black', width = 4)

    ##

    ##    line17 = canvas.create_line(650, 90, 680, 90, fill ='black', width = 4)

    ##

    ##    line18 = canvas.create_line(680, 70, 710, 70, fill ='black', width = 4)

    ##

    ##

    ##    line19 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line20 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line21 = canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line22 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line23 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line24 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line25 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line26 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##    line27 = canvas.create_line(80, 70, 110, 70, fill ='black', width = 4)

    ##

    ##

    ##    line28 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line29 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line30 = canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line31 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line32 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line33 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line34 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line35 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##    line36 = canvas.create_line(80, 70, 110, 70, fill ='black', width = 4)

    ##

    ##

    ##    line37 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line38 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line39= canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line40 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line41 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line42 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line43 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line44 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##    line45 = canvas.create_line(80, 70, 110, 70, fill ='black', width = 4)

    ##

    ##

    ##    line46 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line47 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line48 = canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line49 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line50 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line51 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line52 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line53 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##    line54 = canvas.create_line(80, 70, 110, 70, fill ='black', width = 4)

    ##

    ##

    ##    line55 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line56 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line57 = canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line58 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line59 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line60 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line61 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line62 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##    line63 = canvas.create_line(80, 70, 110, 70, fill ='black', width = 4)

    ##

    ##

    ##    line64 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line65 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line66 = canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line67 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line68 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line69 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line70 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line71 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##    line72 = canvas.create_line(80, 70, 110, 70, fill ='black', width = 4)

    ##

    ##

    ##    line73 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line74 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line75 = canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line76 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line77 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line78 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line79 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line80 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##    line81 = canvas.create_line(80, 70, 110, 70, fill ='black', width = 4)

    ##

    ##

    ##    line82 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line83 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line84 = canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line85 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line86 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line87 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line88 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line89 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##    line90 = canvas.create_line(80, 70, 110, 70, fill ='black', width = 4)

    ##

    ##

    ##    line91 = canvas.create_line(110,70, 130, 90, fill ='black', width = 4)

    ##

    ##    line91 = canvas.create_line(130,90, 150, 70, fill ='black', width = 4)

    ##

    ##    line92 = canvas.create_line(150,70, 170, 90, fill ='black', width = 4)

    ##

    ##    line93 = canvas.create_line(170, 90, 190, 70, fill ='black', width = 4)

    ##

    ##    line94 = canvas.create_line(190, 70, 210, 90, fill ='black', width = 4)

    ##

    ##    line95 = canvas.create_line(210, 90, 230, 70, fill ='black', width = 4)

    ##

    ##    line96 = canvas.create_line(230, 70, 250, 90, fill ='black', width = 4)

    ##

    ##    line97 = canvas.create_line(250, 90, 280, 90, fill ='black', width = 4)

    ##

    ##

    ##

    ##line = canvas.create_line(80,70, 120,140 , fill ='black', width = 4)

    ##

    ##line2 = canvas.create_line(120,140, 160,70 , fill ='black', width = 4)

    ##

    ##line3 = canvas.create_line(161,70, 200,140 , fill ='black', width = 4)

    ##

    ##line4 = canvas.create_line(200,140, 240,70 , fill ='black', width = 4)

    ##

    ##line5 = canvas.create_line(240,70, 280,140 , fill ='black', width = 4)

    ##

    ##line6 = canvas.create_line(280,140, 320,140 , fill ='black', width = 4)

    ##

    ##line7 = canvas.create_line(80,70, 40,140 , fill ='black', width = 4)

    ##

    ##line8 = canvas.create_line(40,140, 10,140 , fill ='black', width = 4)

    ##

    ##

    ##def grid loop(canvas, line_distance):

    ##   # vertical lines at an interval of "line_distance" pixel

    ##   for x in range(1000):

    ##      canvas.create_line(x, y, x2, y2, fill="#476042")

    ##   # horizontal lines at an interval of "line_distance" pixel

    ##   for y in range(1000):

    ##      canvas.create_line(x, y, x2, y2, fill="#476042")

    if __name__ == "__main__":

        checkered(canvas, 10)

        root.mainloop()
