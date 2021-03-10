import sqlite3

conn = sqlite3.connect('tata_data.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO TESTER VALUES ('biome', 1, 2, 3, 4, 5, 'position', 'velocity', 'rotation', 'direction', 10, 11, 12, 13, 14, 15, 'names', 'amount', 18, 19, 'time', 'as')")

conn.commit()