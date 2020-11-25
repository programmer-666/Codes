import pymysql
from random import randint
con = pymysql.connect('127.0.0.1', 'root', 'e6m666_?*?', 'testbase')
with con:
    cur = con.cursor()
    cur.execute("SELECT x,y,z FROM spacetime WHERE x=0")
    f = cur.fetchall()
print(len(f))