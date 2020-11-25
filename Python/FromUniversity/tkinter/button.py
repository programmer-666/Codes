from tkinter import *
import random
root = Tk()
def ch():
    lb1["text"] = str(random.randrange(0, 100))

lb1 = Label(text = "Ok")
btn_1 = Button(text = "This is a Button", bg="black", fg="white", command=ch, activebackground="purple", activeforeground="lightgreen")

btn_1.pack()
lb1.pack()
root.mainloop()