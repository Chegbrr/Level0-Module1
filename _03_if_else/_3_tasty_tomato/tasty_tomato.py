from tkinter import *
import tkinter as tk
from tkinter import simpledialog

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
q1 = simpledialog.askstring(title= '', prompt= 'What color would you like your tomato base. (Red, purple, black, or yellow) ')
q2 = simpledialog.askstring(title= '', prompt= 'What color would you like the stem of the tomato. (Red, green, yellow, or purple)')

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if q1 == 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
else:
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
if q1 == 'purple':
    canvas.create_oval(75, 200, 400, 450, fill="purple", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
if q1 == 'black':
    canvas.create_oval(75, 200, 400, 450, fill="black", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="black", outline="")
if q1 == 'yellow':
    canvas.create_oval(75, 200, 400, 450, fill="yellow", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")


if q2 == 'red':
    canvas.create_rectangle(275, 100, 325, 230, fill="red", outline="")
if q2 == 'green':
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
if q2 == 'yellow':
    canvas.create_rectangle(275, 100, 325, 230, fill="yellow", outline="")
if q2 == 'purple':
    canvas.create_rectangle(275, 100, 325, 230, fill="purple", outline="")
else:
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
root.mainloop()
