# Drivers a serem importados para que os bancos sejam integrados 
import MySQLdb # driver para o MySQL
import sqlite # driver para o sqlite
from pyPgSQL import PgSQL # driver para o PostgreSQL
import kinterbasdb # driver para o Interbase / Firebird
import pymssql # driver para o MS-SQL. (existem outros modulos - ADOdb for Python/PHP)
import cx_Oracle # driver para o oracle database

# Criando a conexão

# MySQL:
con1 = MySQLdb.connect('servidor', 'usuario', 'senha')
con1.select_db('banco de dados') # nome do banco de dados no servidor

# SQlite
con2 = sqlite.connect('nome do arquivo', mode=775) # mode define o modo de trabalho

# PostgreSQL
con3 = PgSQL.connect(
    host = 'servidor',
    database = 'banco de dados',
    user = 'usuario'
    password = 'senha'
)

# Interbase / Firebird
con4 = kinterbasdb.connect(
    dsn = 'servidor:/path/arquivo.fdb',
    user = 'usuario',
    password = 'senha'
)

# MS-SQL
con5 = pymssql.connect(
    host = 'servidor',
    user = 'usuario',
    password = 'senha',
    database = 'base de dados' # nome do banco
)

# Oracle database
con6 = cx_Oracle.connect('usuario/senha@tnsname')


# Obtendo uma transação

cursor = con.cursor()


# Executando um sql
cursor.execute('Codigo SQL')


cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)',(valor1, valor2, valor3))
# os ? são os paramstyle de cada modulo, então para execuar corretamente voce deve consultar a documentação do modulo escolhido
# as variaveis que estão depois dos parentesis devem ser do mesmo tipo que as colunas no banco de dados



#Salvando alteraçoes
cursor.execute('INSERT INTO TABELA (CAMPO1, CAMPO2, CAMPO3) VALUES (?,?,?)',(valor1, valor2, valor3))

con.commit()



# Obtendo o resultado
rs = cursor.fetchone() # Busca uma linha
rs = cursor.fetchall() # Busca todas as linhas
rs = cursor.dictfetchall() # busca todas as linhas, cada linha tem um dicionario com os nomes dos campos

# O KinterbasDB (Interbase/Firebird) não possui suporte para o método: dictfetchall()

# O MS-SQL também não possui suporte para o metodo: dictfetchall()


# E no resultado estarão os campos:
print(rs[0]) #valor da primeira coluna

#alternativamente voce pode usar o cursor como um iterador:
for linha in cursor:
    print(linha[0])

