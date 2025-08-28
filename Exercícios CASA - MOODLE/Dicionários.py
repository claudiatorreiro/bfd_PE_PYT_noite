# 1. Criando um dicionário com informações de um aluno
aluno = {
    "nome": "Juliana",
    "idade": 17,
    "nota": 9.5
}
print(aluno)

# Explicação:
# Um dicionário guarda dados com nome (chave) e valor, como uma etiqueta. 
# Aqui temos 3 informações sobre uma aluna.

produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}

# 2. Acessando valores do dicionário pelas chaves
print("Nome do produto:", produto["nome"])
print("Estoque:", produto["estoque"])

# Explicação:
# Para pegar um valor dentro do dicionário, usamos nome_do_dicionario["chave"].

pessoa = {"nome": "Carlos", "idade": 30}

# 3. Adicionando uma nova informação (cidade)
pessoa["cidade"] = "São Paulo"

print(pessoa)

# Explicação:
# Usamos o nome da nova chave e atribuímos um valor. Simples assim!

carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}

# 4. Removendo a chave "ano"
del carro["ano"]

print(carro)

# Explicação:
# A palavra del serve para deletar chaves do dicionário.

contato = {"nome": "Ana", "email": "ana@email.com"}

# 5. Verificando se existe a chave "telefone"
if "telefone" in contato:
    print("Telefone existe.")
else:
    print("Telefone não encontrado.")

# Explicação:
# Usamos "chave" in dicionario para verificar se a chave está presente.

# 6. Contando frequência de 
# O comando def no Python é usado para definir uma função.

def contar_palavras(lista):
    contagem = {}
    for palavra in lista:
        if palavra in contagem:
            contagem[palavra] += 1  # Já existe, soma 1
        else:
            contagem[palavra] = 1  # Primeira vez, começa com 1
    return contagem

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
resultado = contar_palavras(palavras)
print(resultado)

# Explicação:
# Criamos um dicionário que conta quantas vezes cada palavra aparece na lista.
# def contar_palavras(lista): → Aqui estamos criando uma função chamada contar_palavras.
# Ela recebe uma lista como entrada (entre os parênteses).
# O código dentro da função conta quantas vezes cada palavra aparece.
# return contagem → O return devolve o resultado para quem chamou a função.


# 7. Invertendo chaves e valores
d = {"a": 1, "b": 2, "c": 3}

invertido = {valor: chave for chave, valor in d.items()}

print(invertido)

# Explicação:
# Usamos um “for especial” para criar um novo dicionário trocando a posição: chave ↔ valor.

alunos = {
    "Claudia": [8, 9, 10],
    "Juliana": [7, 6, 9],
    "Myrella": [10, 10, 9]
}

# 8. Calculando a média de cada aluno
for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome} - Média: {media:.2f}")

# Explicação:

# Cada valor do dicionário é uma lista com as 3 notas do aluno.

# sum(notas) soma as notas.

# len(notas) conta quantas são (3).

# 9. Dividimos para ter a média.

def mesclar_dicts(d1, d2):
    resultado = d1.copy()  # Cópia do primeiro dicionário
    resultado.update(d2)   # Junta com o segundo
    return resultado

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

novo = mesclar_dicts(d1, d2)
print(novo)

# Explicação:
# Se uma chave existir nos dois, o valor do segundo dicionário vence.


# 10. Ordenando pelo valor (pontuação), do maior para o menor
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
ordenado = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)

# Mostrando os itens ordenados
for nome, pontuacao in ordenado:
    print(f"{nome} - {pontuacao}")

# Explicação:

# sorted() organiza os itens.

# key=lambda item: item[1] diz pra usar o valor como base.

# reverse=True coloca do maior para o menor.






