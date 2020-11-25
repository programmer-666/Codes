from tkinter import *
class Yapi:
    def __init__(self):
        self.LoginWidgets()
        self.LoginPack()
        self.LoginLoop()

    """ LOGIN """
    def LoginWidgets(self):
        self.loginW = Tk()
        self.entry_1 = Entry(self.loginW)
        self.button_1 = Button(self.loginW,text = "Login", command=self.MainExec)
    def LoginPack(self):
        self.entry_1.pack()
        self.button_1.pack()
    def LoginLoop(self):
        self.loginW.mainloop()
    """ LOGIN """
    """ MAIN """
    def MainWidgets(self):
        self.mainW = Tk()
        self.label_1_main = Label(self.mainW,text = "Entered Main Form")
    def MainPack(self):
        self.label_1_main.pack()
    def MainLoop(self):
        self.mainW.mainloop()
    def MainExec(self):
        self.MainWidgets()
        self.MainPack()
        self.MainLoop()
    """ MAIN """

test = Yapi()
test.LoginPack()
test.LoginLoop()