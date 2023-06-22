import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'crud_python'
)
cursor = conn.cursor()

nome = "Pants"
valor = 35

#CREATE
# sql = f'INSERT INTO vendas (nome, valor) VALUES ("{nome}", {valor})'
# cursor.execute(sql)

#READ
# sql = 'SELECT * FROM vendas'
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)

#UPDATE
# sql = f'UPDATE vendas SET nome = "Hat", valor = {valor} WHERE idVenda = 3'
# cursor.execute(sql)
# conn.commit()

#DELETE
sql = 'DELETE FROM vendas WHERE idVenda = 3'
cursor.execute(sql)
conn.commit()

cursor.close()
conn.close()