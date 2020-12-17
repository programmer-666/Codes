import sqlite3
class sqdb3:
    __ERROR_CODES = []
    __CONNECTION_FLAG = False
    def __init__(self):
        self.ConnectDB()
    def ConnectDB(self, dbname = "player_infos.db"):
        self.__CONNECTION_FLAG = True
        self.__connection = sqlite3.connect(dbname)
    def DisconnectDB(self):
        self.__CONNECTION_FLAG = False
        self.__connection.close()
    def GetMessages(self):
        if self.__CONNECTION_FLAG:
            self.__cursor = self.__connection.cursor()
            raw_Messages = self.__cursor.execute("SELECT * FROM MESSAGES").fetchall()
            print(raw_Messages)
        else:
            self.__ERROR_CODES.append(24)
    def ReturnErrorCodes(self):
        if len(self.__ERROR_CODES) > 0:
            return self.__ERROR_CODES
x = sqdb3()
x.GetMessages()
print(x.ReturnErrorCodes())
x.DisconnectDB()