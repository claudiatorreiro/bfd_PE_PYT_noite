.tables

SELECT * FROM Aluno;
SELECT * FROM Curso;
SELECT * FROM Turma;

-- O alias AS total_alunos nomeia a coluna do resultado.
SELECT COUNT(*) AS total_alunos FROM Aluno;

-- MIN(coluna) retorna o menor valor da coluna mensalidade da tabela Curso.
SELECT MIN(mensalidade) AS menor_mensalidade FROM Curso;


-- MAX(nota1) retorna o valor mais alto da coluna nota1 entre todos os alunos.
SELECT MAX(nota1) AS maior_nota1 FROM Aluno;


-- SUM(mensalidade) soma todos os valores da coluna mensalidade.
SELECT SUM(mensalidade) AS total_mensalidades FROM Curso;


-- AVG(nota2) calcula a média de todos os valores da coluna nota2.
SELECT AVG(nota2) AS media_geral_nota2 FROM Aluno;






