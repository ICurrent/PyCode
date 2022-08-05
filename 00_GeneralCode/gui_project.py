from tkinter import *


base = Tk()
base.geometry("500x750")
base.title("Database")

bg = PhotoImage(file="God copy.jpg") #Add image
canvas1 = Canvas(base, width=500, height=750) #Create canvas
canvas1.pack(fill="both", expand=True)
# Display image
canvas1.create_image(0, 0, image= bg, anchor="nw")

def some_func():
    pass


label_1 = Label(base, text="His Glory Ventures", fg="white", bg="red", font=("beauty flower", 50, "bold"))
label_1.pack()

label_2 = Label(base, text="Customer Name: ", fg="black", font=("impact", 10, "italic"))
label_2.pack()

entry_1 = Entry(base, bg= "sky blue")
entry_1.pack()

#label_1.grid(row=0, column=2)


base.mainloop()