# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    window = Tk()
    window.withdraw()

    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    r = simpledialog.askinteger(title='', prompt='Enter a radius. ')
    x = simpledialog.askstring(title='', prompt='Would you like to know the area or circumference? (type Area or Circumference)')

    area1 = r*r
    area2 = 3.141592693589 * area1
    circ = 2 * r * 3.141592693589
    if x == 'Area':
        messagebox.showinfo(message ='The area of the circle is: ' + str(area2))

    if x == 'Circumference':
        messagebox.showinfo(message='The circumference of the circle is: ' + str(circ))
