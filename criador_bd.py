import sqlite3

con = sqlite3.connect('vagas.db')
cursor = con.cursor()
cursor.execute('''CREATE TABLE VAGAS(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               TITULO TEXT,
               EMPRESA TEXT,
               CIDADE TEXT,
               DATA_COLETA DATE,
               URL TEXT UNIQUE)''')
con.commit()
con.close()
