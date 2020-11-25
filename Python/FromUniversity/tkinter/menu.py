from tkinter import *
main_window = Tk()

men = Menu(main_window)
main_window.config(menu=men)

smen = Menu(men, tearoff=0)
men.add_cascade(label="dosya", menu=smen)
smen.add_command(label="1")

main_window.mainloop()