import pymysql
con = pymysql.connect(host='sql280.main-hosting.eu', user='u347527466_pod_admin', password='x.01*!A?', db='u347527466_POD', port=3306)
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM n11_stok")
    f = cur.fetchall()
print(len(f))