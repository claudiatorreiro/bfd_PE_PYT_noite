### Exeercício 1 - Turma 36

## 1

livros = ["1984", "O Senhor dos Anéis", "Dom Casmurro"]
print(livros)

## 2

print("Primeiro livro:", livros[0])
print("Último livro:", livros[-1])

## 3

livros.append("Harry Potter")
livros.append("O Pequeno Príncipe")
print(livros)


## 4

livros.insert(1, "Duna")
print(livros)


## 5

if "Silêncio dos inocentes" in livros:
    livros.remove("Silêncio dos inocentes")
else:
    print("Livro não encontrado")


## 6

numeros = [1, 2, 3, 2, 4, 2, 5]
quantidade = numeros.count(2)
print("O número 2 aparece", quantidade, "vezes.")


## 7

for livro in livros:
    print(f"O livro {livro} é interessante")


## 8

idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
        print(idade)


## 9

valores = [10, 20, 30, 40]
soma = 0
for valor in valores:
    soma += valor
print("Soma dos valores:", soma)


## 10

notas = []

for i in range(2):
    aluno = []
    print(f"Digite as 3 notas do aluno {i+1}:")
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        aluno.append(nota)
    notas.append(aluno)

for i in range(2):
    media = sum(notas[i]) / 3
    print(f"Média do aluno {i+1}: {media:.2f}")

## 11

linha_pecas = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]

linha_peoes = ["pea" for _ in range(8)]

linha_vazia = ["[ ]" for _ in range(8)]

tabuleiro = [
    linha_pecas,             
    linha_peoes,             
    linha_vazia.copy(),      
    linha_vazia.copy(),      
    linha_vazia.copy(),      
    linha_vazia.copy(),      
    linha_peoes,             
    linha_pecas              
]

print("Tabuleiro de Xadrez:") 
for linha in tabuleiro:
    for item in linha:
        print(item, end=" ")  
        print()




