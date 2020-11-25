import sqlite3
db = sqlite3.connect('ps.db')
cs = db.cursor()
cs.execute("CREATE TABLE kisiler (id_isim, isim)")
