import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()


#c.execute("""CREATE TABLE players(
 #           name text,
 #           points integer)
#""")

c.execute("INSERT INTO players VALUES('player1', 2)")

conn.commit()

conn.close()