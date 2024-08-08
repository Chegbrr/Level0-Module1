"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    n1 = simpledialog.askinteger(title='', prompt='Choose an integer')
    n2 = simpledialog.askinteger(title='', prompt='Choose another integer')

    add = n1 + n2
    sub = n1 - n2
    mult = n1 * n2
    div = n1/n2

    q = simpledialog.askstring(title='', prompt='Would you like to add, subtract, multiply, or divide the two numbers.')
    if q == 'add':
        messagebox.showinfo(message='The sum of the two numbers is: ' + str(add))
    if q == 'subtract':
        messagebox.showinfo(message='The difference of the two numbers is: ' + str(sub))
    if q == 'multiply':
        messagebox.showinfo(message='When you multiply the numbers together you get: ' + str(mult))
    if q == 'divide':
        messagebox.showinfo(message='When you divide the first number by the second number you get: ' + str(div))
