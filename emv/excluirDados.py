import sqlite3
ex = str(input('Digite o nome para excluir banco de dados: '))
try:
    banco = sqlite3.connect('elaine.db')
    cursor = banco.cursor()
    cursor.execute("DELETE from pessoas WHERE nome = '"+ex+"'")
    banco.commit()
    banco.close
    print('Dados excluidos com SUCESSO!')
except sqlite3.Error as erro:
    print('Erro ao excluir os dados!', erro)
