import sqlite3 as slt
pss = ['123f', '42ef', '2fe', 'g432g', 'fvfbtt']
with slt.connect("user.db") as db:
    for i in range(1, 5):
        db.cursor().execute(f"INSERT INTO USERPASSWORDS VALUES (?, ?, ?)", (i, i, pss[i-1]))
        db.commit()
