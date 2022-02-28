import sqlite3

try:
    banco = sqlite3.connect('elaine.db')
    cursor = banco.cursor()
    cursor.execute("UPDATE pessoas SET nome = 'Joana' WHERE idade = 46")
    banco.commit()
    banco.close
    print('Dados alterados com SUCESSO!')
except sqlite3.Error as erro:
    print('Erro na tentativa de alterar os dados!')