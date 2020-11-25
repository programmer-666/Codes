from tkinter import *
root = Tk()
cbv = IntVar()
def cnt():
    if cbv.get() == 1:
        lb1["text"] = "1"
    else:
        lb1["text"] = "0"
cb1 = Checkbutton(root, text="CB1", variable=cbv, command=cnt)
lb1 = Label(root, text="LB1")
cb1.pack()
lb1.pack()
root.mainloop()