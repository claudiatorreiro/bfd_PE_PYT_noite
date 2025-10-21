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







