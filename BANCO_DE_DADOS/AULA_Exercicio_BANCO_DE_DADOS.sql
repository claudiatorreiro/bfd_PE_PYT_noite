.tables

SELECT * FROM Aluno;
SELECT * FROM Curso;
SELECT * FROM Turma;

SELECT * FROM Aluno
cross join Turma ON Aluno.id_turma = Turma.id;

SELECT * FROM Aluno
INNER JOIN Turma ON Aluno.id_turma = Turma.id;

SELECT A.nome AS nome_aluno,
       A.nota1,
       T.nome AS nome_turma,
       T.ano
FROM Aluno A
INNER JOIN Turma T ON A.id_turma = T.id;

-- 1️⃣ Mostrar todos os registros da tabela Aluno

-- 🛠️ Comando: SELECT com FROM completo
-- 🧠 Explicação:
-- O * significa todas as colunas. Esse comando traz tudo: nome, notas, data de nascimento, etc.

SELECT * FROM Aluno;


-- 2️⃣ Exibir apenas o nome e a nota1 de todos os alunos

-- 🛠️ Comando: SELECT com colunas específicas
-- 🧠 Explicação:
-- Selecionamos apenas as colunas desejadas, evitando o uso do * para ser mais eficiente e claro.

SELECT nome, nota1 FROM Aluno;


-- 3️⃣ Listar alunos cuja nota2 seja maior que 8

-- 🛠️ Comando: SELECT com WHERE
-- 🧠 Explicação:
-- O WHERE filtra os registros onde a condição é verdadeira.

SELECT * FROM Aluno
WHERE nota2 > 8;


-- 4️⃣ Alunos que nasceram após o ano de 2000

-- 🛠️ Comando: WHERE com data
-- 🧠 Explicação:
-- Comparação direta com datas no formato YYYY-MM-DD.

SELECT * FROM Aluno
WHERE data_nascimento > '2000-12-31';


-- 5️⃣ Nome e mensalidade dos cursos com valor acima de R$600

-- 🛠️ Comando: WHERE com número
-- 🧠 Explicação:
-- Simples filtro numérico. Aqui, assumimos que a coluna se chama mensalidade.

SELECT nome, mensalidade FROM Curso
WHERE mensalidade > 600;


-- 6️⃣ Nome das turmas e ano, ordenados pelo ano (crescente)

-- 🛠️ Comando: ORDER BY
-- 🧠 Explicação:
-- ASC = Ascendente (padrão). Mostra os anos em ordem do menor para o maior.

SELECT nome, ano FROM Turma
ORDER BY ano ASC;

-- 7️⃣ Ano das turmas e quantidade de turmas por ano

-- 🛠️ Comando: GROUP BY + COUNT
-- 🧠 Explicação:
-- Agrupa por ano e conta quantas turmas existem em cada ano.

SELECT ano, COUNT(*) AS quantidade_turmas
FROM Turma
GROUP BY ano;


-- 8️⃣ Média da nota1 dos alunos por turma_id

-- 🛠️ GROUP BY com AVG
-- 🧠 Explicação:
-- Agrupamos por turma e calculamos a média da nota1 dos alunos de cada uma.

SELECT id_turma, AVG(nota1) AS media_nota1
FROM Aluno
GROUP BY id_turma;


-- 9️⃣ Ano e quantidade de turmas apenas para anos com mais de 2 turmas

-- 🛠️ GROUP BY com HAVING
-- 🧠 Explicação:
-- HAVING é usado para filtrar resultados de agregações, diferente do WHERE.

SELECT ano, COUNT(*) AS quantidade_turmas
FROM Turma
GROUP BY ano
HAVING COUNT(*) > 2;


-- 🔟 Cursos e suas mensalidades, ordenando pela mensalidade (decrescente)

-- 🛠️ ORDER BY DESC
-- 🧠 Explicação:
-- DESC = ordem decrescente, do maior valor para o menor.

SELECT nome, mensalidade FROM Curso
ORDER BY mensalidade DESC;








