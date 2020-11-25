import sqlite3 as slt
""" fetchone - tek tek alır. fetchmany - belirtilen sayı kadar alır. """
db = slt.connect("user.db")
print(db.cursor().execute("SELECT * FROM USERPASSWORDS").fetchall())
#print(db.cursor().execute("SELECT * FROM USERNAMES").fetchmany(2))
#print(db.cursor().execute("SELECT * FROM USERNAMES").fetchone())
db.commit();db.close()
