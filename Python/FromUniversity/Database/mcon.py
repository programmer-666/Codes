import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="e6m666_?*?",
  database="mylib"
)
mycursor = mydb.cursor()

sql = "INSERT INTO  (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")