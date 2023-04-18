import sqlite3

Ncon = sqlite3.connect("Nusers.db")
Ncur = Ncon.cursor()

Ncur.execute("""CREATE TABLE IF NOT EXISTS users
                (id INTEGER,  
                name TEXT, 
                group_number INTEGER)
            """)

con = sqlite3.connect("users.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users
                (id INTEGER,  
                name TEXT, 
                group_number INTEGER)
            """)

