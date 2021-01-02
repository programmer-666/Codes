import sqlite3, hashlib
class Create_Database:
    __TABLES__ = []
    __COLUMNS__ = []
    def __init__(self, dbname="bytecoin.db"):
        ### CREATING DATABASE AND CURSOR ###
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()
        self.tableQueries()

    def tableQueries(self):
        ### CREATING TABLES AND EXAMPLE VALUES
        self.__TABLES__.append("CREATE TABLE IF NOT EXISTS USERS (id_user INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)")
        self.__TABLES__.append("CREATE TABLE IF NOT EXISTS WALLETS (id_wallet INTEGER PRIMARY KEY, id_user INTEGER NOT NULL REFERENCES USERS(id_user), bytecoin REAL NOT NULL)")

        for i in range(len(self.__TABLES__)):
            self.cursor.execute(self.__TABLES__[i])
        self.connection.commit()

        self.cursor.execute("INSERT INTO USERS (username, password) VALUES ('programmer666', '"+hashlib.md5(bytes("qwerty".encode())).hexdigest()+"')")
        self.cursor.execute("INSERT INTO USERS (username, password) VALUES ('deity', '"+hashlib.md5(bytes("x.01*!A?".encode())).hexdigest()+"')")
        self.cursor.execute("INSERT INTO WALLETS (id_wallet, id_user, bytecoin) VALUES (1000001, 1, 0.0)")
        self.cursor.execute("INSERT INTO WALLETS (id_wallet, id_user, bytecoin) VALUES (2000002, 2, 0.0)")
        self.connection.commit()

    