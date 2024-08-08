import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    turt = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='', prompt='Choose a shape. (rectangle, circle, triangle, and square)')
    # Draw the shape requested by the user using if-elif-else statements
    turt.penup()
    turt.speed(0)
    turt.color('black')
    turt.pencolor('black')
    if shape == 'rectangle':
        turt.pendown()
        turt.begin_fill()
        for i in range (2):
            turt.forward(100)
            turt.left(90)
            turt.forward(50)
            turt.left(90)
    if shape == 'circle':
        turt.pendown()
        turt.begin_fill()
        turt.circle(100)
    if shape == 'triangle':
        turt.pendown()
        turt.begin_fill()
        for i in range (3):
            turt.forward(100)
            turt.left(120)
    if shape == 'square':
        turt.goto(-50, -50)
        turt.pendown()
        turt.begin_fill()
        for i in range (4):
            turt. forward(100)
            turt.left(90)
    else:
        messagebox.showinfo(message='I can not draw this shape. (or it was not writen as said in the question)')
    turt.end_fill()
    turt.hideturtle()

    # Call the turtle .done() method
turtle.done()
