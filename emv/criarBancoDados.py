import sqlite3

banco = sqlite3.connect('elaine.db')
cursor = banco.cursor()
try:
    cursor.execute("CREATE TABLE pessoas (nome text, idade integer, sexo text)")
except sqlite3.OperationalError:
    print('Tabela já existe!')
while True: 
     
    nome = str(input('Nome: '))
    idade = int(input('Qual é sua idade: '))
    sexo = str(input('Sexo [M/F]')).upper()
    if sexo not in 'MF':
        print('ERRO! por favor digite [M/F]')
    resp = str(input('Quer continuar [S/N] ')).upper()
    cursor.execute("INSERT INTO pessoas VALUES ('"+nome+"', "+str(idade)+", '"+sexo+"')")
    banco.commit() 
    if resp == 'N':
        break

banco.close()