#import tkinter

from tkinter import*

root = Tk()

def grade():
    from cgpa.py import cgpa_eva

button_1 = Button(root,text = "Play", command = grade)
button_1.pack()


root.mainloop()
