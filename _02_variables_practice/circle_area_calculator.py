import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    rad = simpledialog.askinteger(title='', prompt='Enter the radius of a circle to know the area. ')

    # Make a new turtle
    turt = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    turt.circle(radius=rad)
    # Call the turtle .penup() method
    turt.penup()
    # Move your turtle to a new x,y position using .goto()
    turt.goto(-250,-100)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = (rad^2)*math.pi
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    turt.write(arg="area = " + str(area), move=True, align = 'left', font=('Arial', 50, 'normal'))
    # Hide your turtle
    turt.hideturtle()
    # Call turtle.done()
turtle.done()
