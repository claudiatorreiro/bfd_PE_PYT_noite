import sqlite3

from tabulate import tabulate


# Conectando ao banco de dados
conexao = sqlite3.connect("escola_v2_giza.db")
cursor = conexao.cursor()

# 1. Pegando todos os dados da tabela Aluno
print("=== Todos os alunos ===")
cursor.execute("SELECT * FROM Aluno")
alunos = cursor.fetchall()
headers = ["id", "nome", "data_nascimento", "nota1", "nota2", "id_turma"]
print(tabulate(alunos, headers=headers, tablefmt="grid"))

# 2. Calculando a média entre nota1 e nota2, ordenando e pegando os 10 maiores
print("\n=== Top 10 alunos por média ===")
cursor.execute("""
    SELECT nome, nota1, nota2, ROUND((nota1 + nota2) / 2.0, 2) AS media
    FROM Aluno
    ORDER BY media DESC
    LIMIT 10
""")
top_alunos = cursor.fetchall()
headers = ["nome", "nota1", "nota2", "media"]
print(tabulate(top_alunos, headers=headers, tablefmt="grid"))

# 3. LEFT JOIN com Aluno e Turma
print("\n=== Alunos com informações da Turma (LEFT JOIN) ===")
cursor.execute("""
    SELECT Aluno.*, Turma.*
    FROM Aluno
    LEFT JOIN Turma ON Aluno.id_turma = Turma.id
""")
alunos_turma = cursor.fetchall()
headers = [desc[0] for desc in cursor.description]
print(tabulate(alunos_turma, headers=headers, tablefmt="grid"))

# 4. LEFT JOIN filtrando apenas alunos da turma 2
print("\n=== Alunos da Turma 2 ===")
cursor.execute("""
    SELECT Aluno.*, Turma.*
    FROM Aluno
    LEFT JOIN Turma ON Aluno.id_turma = Turma.id
    WHERE Aluno.id_turma = 2
""")
turma2 = cursor.fetchall()
headers = [desc[0] for desc in cursor.description]
print(tabulate(turma2, headers=headers, tablefmt="grid"))

# Fechando a conexão
conexao.close()






