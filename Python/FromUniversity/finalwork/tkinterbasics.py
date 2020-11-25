from tkinter import *
class basics:
    def __init__(self):
        self.mainpage = Tk()
        self.mainpage.geometry("200x200")
        self.mainpagewidgets()
    def mainpagewidgets(self):
        self.e1 = Entry(self.mainpage)
        self.e1.grid(row = 0, column = 0)
        #Entrys
        self.b1 = Button(self.mainpage, text = "Calculate", command=self.calc)
        self.b1.grid(row = 0, column = 1)
        #Buttons
        self.lb1 = Listbox(self.mainpage)
        self.lb1.grid(row = 1, column = 0)
        #Listboxs
    def calc(self):
        self.lb1.delete(0, END)
        for i in range(1, int(self.e1.get())+1):
            self.lb1.insert(i, i)
    def mainpageloop(self):
        self.mainpage.mainloop()
if __name__ == "__main__":
    basics().mainpageloop()