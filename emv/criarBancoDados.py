from calendar import c
import sqlite3

banco = sqlite3.connect('elaine.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, sexo text)")
""" cursor.execute("INSERT INTO pessoas VALUES('João Cagão', 34, 'M')")

banco.commit() """
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())