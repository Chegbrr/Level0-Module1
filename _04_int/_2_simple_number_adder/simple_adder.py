"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    n1 = simpledialog.askinteger(title='', prompt='Choose an integer')
    n2 = simpledialog.askinteger(title='', prompt='Choose another integer')

    sum1 = n1 + n2

    messagebox.showinfo(message='The sum of both the integers is ' + str(sum1))

    turt = turtle.Turtle()

    turt.write(arg= str(sum1), move=True, align = 'left', font=('Arial', 50, 'normal'))
    turt.hideturtle()
turtle.done()
