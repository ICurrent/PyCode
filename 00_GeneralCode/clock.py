from tkinter import *
import time

base = Tk()
base.title("Digital Clock")
base.geometry("800x400")

grid = Label(base, text='Welcome', font=('Constantia', 40, 'bold'))
grid.pack()

def localtime():
    mytext = time.strftime('%I : %M : %S %p')
    mytext2 = time.strftime("%A")

    myLabel.config(text = mytext)
    myLabel2.config(text = mytext2)

    myLabel.after(1000, localtime)


myLabel0 = Label(base, text="Digital Clock", font=("Impact", 35), fg = "blue")
myLabel0.pack()

myLabel = Label(base, text="", font=("beauty flower", 45), fg = "white", bg='black')
myLabel.pack()
myLabel2 = Label(base, text="", font=("Impact", 35), fg = "blue")
myLabel2.pack()
localtime()

base.mainloop()