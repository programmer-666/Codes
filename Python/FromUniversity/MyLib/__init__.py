from tkinter import *
from tkinter import messagebox
import hashlib
import pymysql

class mylib_form():
    # LOGIN FORM
    def __init__(self):
        self.form()
        self.form_props()
        self.form_wids()
        self.form_wid_pack()
        self.run()
    def form(self):
        self.form = Tk()
    def form_props(self):
        self.form.title("Login")
        self.form.geometry("600x320")
        self.form.resizable(0,0)
        # Window Settings
        self.form.configure(background="#181818")
        # Color Settings
    def form_wids(self):
        self.form_label_1 = Label(self.form ,text = "MyLib", fg = "white", bg="#181818", font=("Sans-serif 50"))
        self.form_entry_1 = Entry(self.form ,fg = "white", bg="#181818", font=("Sans-serif 20"))
        self.form_entry_2 = Entry(self.form ,fg = "white", bg="#181818", font=("Sans-serif 20"), show="*")
        self.form_button_1 = Button(self.form ,text="Login",fg = "white", bg="#181818", font=("Sans-serif 20"), command=self.user_controll)
    def form_wid_pack(self):
        self.form_label_1.grid(row=0, column=0, ipadx=200, ipady=20)
        self.form_entry_1.grid(row=1, column=0, pady=10)
        self.form_entry_2.grid(row=2, column=0, pady=10)
        self.form_button_1.grid(row=3, column=0, pady=10)
    def run(self):
        self.form.mainloop()
    # LOGIN FORM
    # DATABASE
    def database_conn(self):
        self.db_connection = pymysql.connect("sql280.main-hosting.eu", str(self.form_entry_1.get()), str(self.form_entry_2.get()), "u347527466_mylib")
    # DATABASE
    # LOGIN PROCESS
    def user_controll(self):
        if hashlib.sha1(str(self.form_entry_1.get()).encode()).hexdigest() == hashlib.sha1("u347527466_myroot".encode()).hexdigest() and hashlib.sha1(str(self.form_entry_2.get()).encode()).hexdigest() == hashlib.sha1("e6m666_?*?".encode()).hexdigest():
            # DATABASE CONNECTION
            self.database_conn()
            if self.db_connection:
                self.form.destroy()
                self.session = 1
                self.complete_main()
            else:
                messagebox.showerror("Connection Error", "Not connected to database.")
            # DATABASE CONNECTION
        else:
            messagebox.showerror("Bad Login", "Wrong username or password.")
    # LOGIN PROCESS
    # MAIN WINDOW
    def main(self):
        self.main = Tk()
    def main_props(self):
        self.main.title("MyLib")
        self.main.geometry("1147x400")
        self.main.resizable(0, 0)
        # Window
        self.main.configure(background="#181818")
        # Color
    def main_wids(self):
        self.main_new_button = Button(self.main, text = "New", bg="#313131", font=("Sans-serif 15"), fg="white", width=10)
        self.main_new_update = Button(self.main,text = "Update", bg="#313131", font=("Sans-serif 15"), fg="white", width=10)
        self.main_new_delete = Button(self.main,text = "Delete", bg="#313131", font=("Sans-serif 15"), fg="white", width=10)
        # BOOKS LIST
        self.main_book_frame = Frame(self.main)
        self.main_database_listboxes = list()
        for i in range(10):
            self.main_database_listboxes.append(Listbox(self.main_book_frame))
        int_standart_size = 4
        self.main_database_listboxes[0]["width"] = int_standart_size #id_book
        self.main_database_listboxes[2]["width"] = int_standart_size #nop_book
        self.main_database_listboxes[3]["width"] = int_standart_size #id_category
        self.main_database_listboxes[4]["width"] = int_standart_size #id_publisher
        self.main_database_listboxes[5]["width"] = int_standart_size #id_write
        self.main_database_listboxes[9]["width"] = int_standart_size #price
        for x in self.main_database_listboxes:
            x.insert(1,"x")
        # BOOKS LIST
    def main_wid_pack(self):
        self.main_new_button.grid(row=0, column=0, ipady = 3, pady = 3)
        self.main_new_update.grid(row=1, column=0, ipady = 3, pady = 3)
        self.main_new_delete.grid(row=2, column=0, ipady = 3, pady = 3)
        self.main_book_frame.grid(row=0, column=1, rowspan=3, padx = 10)
        for b in self.main_database_listboxes:
            b.pack(side=LEFT)
    def main_run(self):
        self.main.mainloop()
    def complete_main(self):
        self.main()
        self.main_props()
        self.main_wids()
        self.main_wid_pack()
        self.main_run()
    # MAIN WINDOW

if __name__ == "__main__":
    mylib_form().complete_main()
