"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    q1 = simpledialog.askstring(title='', prompt='Samuel was out for a walk when it started to rain. He did not have an umbrella and he was not wearing a hat. \n'
                                             'His clothes were soaked, yet not a single hair on his head got wet. How could this happen? (call the man he and write your answer after)')

    q1a = 'he was bald'
    score = 0
    if q1 == q1a:
        messagebox.showinfo(message='That is the correct answer!')
        score += 1
    else:
        messagebox.showinfo(message='That answer is incorrect. \n'
                                    'Better luck next time. ')
        print('The correct answer was: he was bald. ')

    q2 = simpledialog.askstring(title='', prompt='What 8 letter word can have a letter taken away and it still makes a word. \n'
                                                 'Take another letter away and it still makes a word. Keep on doing that until you have one letter left. \n'
                                                 'What is the word? (do not use capital letters)')
    q2a = 'starting'
    if q2 == q2a:
        messagebox.showinfo(message='That is the correct answer!')
        score +=1
    else:
        messagebox.showinfo(message='That answer is incorrect. \n'
                                    'Better luck next time. ')
        print('The word was starting! starting, staring, string, sting, sing, sin, in, I.')


    q3 = simpledialog.askstring(title='', prompt='Davids father has three sons: Snap, Crackle, and _____?\n'
                                                 'Who is the third child?')

    q3a = 'David'
    if q3 == q3a:
        messagebox.showinfo(message='That is the correct answer!')
        score +=1
    else:
        messagebox.showinfo(message='That answer is incorrect. \n'
                                    'Better luck next time. ')
        print('The correct answer was: David')
    print('You got ' + str(score) + ' questions correct.')
    if score == 3:
        print('100%')
    if score == 2:
        print('Try to get 100%')
    if score == 1:
        print('You need to work on your riddles!')
    if score == 0:
        print('...')
