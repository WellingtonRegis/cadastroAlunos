import _sqlite3
import sqlite3

banco = sqlite3.connect('banco_teste.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")
#cursor.execute("INSERT INTO pessoas VALUES('Maria',40,'maria_123@gmail.com')")


#banco.commit()
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())