# Uma função lambda é uma maneira curta e rápida de escrever funções simples em Python.

# É como fazer uma função sem precisar usar o def.

dobro = lambda x: x * 2

# lambda = palavra-chave que cria a função.
# x = o parâmetro (como uma variável de entrada).
# x * 2 = o que a função retorna (o que ela faz).

# Usando a função
# Depois de criar a função lambda, você pode usá-la assim:

print(dobro(5))  # Saída: 10

soma = lambda a, b: a + b
print(soma(3, 4))  # Saída: 7

# Onde se usa muito lambda?
# Você vai ver lambda sendo muito usado com funções como map(), filter() e sort() — para fazer coisas rapidinhas sem criar uma função completa.
# Exemplo com map():

numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8]

# Desafio 1 – Dobrar números com map() e lambda
# ✨ Descrição:
# Use lambda para dobrar os valores de uma lista.
# 📌 Enunciado:
# Dada a lista abaixo, use map() com uma função lambda para dobrar todos os números:

# Como funciona map()?
# A função map() aplica uma função (neste caso, a lambda) em cada item da lista.
# lambda x: x * 2 vai dobrar cada número da lista.
# Usamos list() para converter o resultado em uma lista normal.

numeros = [1, 2, 3, 4, 5]
print(numeros)
print(dobrados)

# Explicação
# lambda x: x * 2 → é uma função que recebe x e devolve x * 2.
# map(...) → aplica isso em todos os itens da lista numeros.
# list(...) → transforma o resultado em uma lista que você pode imprimir.

# Desafio 2 – Filtrar números pares com filter() e lambda
# ✨ Descrição:
# Use lambda para pegar só os números pares da lista.
# 📌 Enunciado:
# Com a lista abaixo, use filter() e lambda para manter só os pares:

# Lógica passo a passo
# lambda é usada para criar uma função sem nome.
# filter() vai aplicar essa função em cada número da lista e filtrar só os que forem True.
# Um número é par se: numero % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6, 8]

# Explicação
# lambda x: x % 2 == 0 → essa função retorna True para números pares.
# filter(...) → aplica essa função a cada elemento da lista.
# list(...) → converte o resultado (que é um filtro) para uma lista visível.

