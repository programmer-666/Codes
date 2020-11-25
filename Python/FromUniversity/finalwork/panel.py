# -*- coding: utf-8 -*- 
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("230x120+2300+0")
# HEAD
def ctrl():
    if e1.get() == "root" and e2.get() == "123":
        messagebox.showwarning("Giriş", "Ojgeldin bea")
    else:
        messagebox.showwarning("Giriş", "Atalı girdin bea")
# CONTROLL
e1 = Entry(root, font = ("Sans-serif 15"))
e2 = Entry(root, show="*", font = ("Sans-serif 15"))
b1 = Button(root, text="Gir", font = ("Sans-serif 20"), command=ctrl)
e1.grid(row = 0, column = 0)
e2.grid(row = 1, column = 0)
b1.grid(row = 2, column = 0)
# WIDGETS
root.mainloop()