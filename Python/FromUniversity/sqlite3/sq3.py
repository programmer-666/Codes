import sqlite3 as s3
dbn = "user.db"
def sqlite_dbreader(dbname):
    with open(dbname, "rb") as fn:
        for i in fn.read():
            print(chr(i), end="")
database = s3.connect(dbn)
""" sqlite3.connect(':memory:') -> Ram üzerinde çalışan geçici veritabanı. :memory: yerine '' kullanarak diskte geçici bir veritabanı oluşturulabilir. """
database.cursor().execute("CREATE TABLE IF NOT EXISTS USERNAMES (id_uname INTEGER PRIMARY KEY, uname TEXT UNIQUE)")
database.commit()
database.cursor().execute("CREATE TABLE IF NOT EXISTS USERPASSWORDS (id_psw INTEGER PRIMARY KEY, id_uname INTEGER, psw TEXT UNIQUE, FOREIGN KEY(id_uname) REFERENCES USERNAMES(id_uname))")
database.commit()
# IF NOT EXISTS -> Eğer tablo yoksa ...
# Foreign tanımlaması en sonda yapılır.
database.commit()
database.close()
