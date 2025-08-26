### Exercício DICIONÁRIOS

### 1. Crie um dicionário vazio chamado cadastro e adicione os seguintes pares chave-valor:

dicionario = {
"nome": "Lucas",
"idade": 25,
"email": "lucas@email.com"
    }

print(dicionario)

cadastro = {}  # dicionário vazio

# Adicionando pares chave-valor
cadastro["nome"] = "Lucas"
cadastro["idade"] = 25
cadastro["email"] = "lucas@email.com"

print(cadastro)

# Explicação:
# cadastro["nome"] = "Lucas" → cria a chave "nome" e associa ao valor "Lucas".
# Isso é como no Scratch, onde você cria uma variável com nome e atribui um valor.

### 2. Usando o dicionário abaixo, use o método .get() para obter o valor da chave "telefone", 
# retornando "Não informado" se a chave não existir.

cliente = {"nome": "Amanda", "idade": 31}
telefone = cliente.get("telefone", "Não informado")

print("Telefone:", telefone)
print(cliente)

# Explicação:
# get() procura uma chave no dicionário.
# Se a chave existe, ele retorna o valor.
# Se a chave não existe, ele retorna o que você colocar como valor padrão (nesse caso, "Não informado").

### 3. Utilize um laço for para imprimir todas as chaves do dicionário abaixo.
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}

for chave in livro:
    print(chave)

# Explicação:
# Em um for sobre um dicionário, o Python percorre as chaves por padrão.
# Isso é como percorrer uma lista no Scratch usando "para cada item da lista".

# ### 4. Adicione uma nova chave chamada "disponível" ao dicionário acima com o valor True.

livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
livro["disponível"] = True

# Explicação:
# Isso adiciona um novo par chave-valor ao dicionário.
# True é um valor booleano (verdadeiro ou falso), assim como os blocos de condições no Scratch.

### 5. Use o método .pop() para remover a chave "ano" do dicionário livro. Imprima o valor removido.
ano_removido = livro.pop("ano")
print("Ano removido:", ano_removido)

print("Dicionário final:", livro)

# Explicação:
# .pop("chave") remove a chave do dicionário e retorna o valor que estava nela.
# Assim, além de remover, você pode usar ou mostrar esse valor depois.

### 6. Crie um dicionário compras com pelo menos 3 itens (nome do produto como chave e preço como valor). 
# Em seguida, use .values() para calcular o total da compra.

# Criando o dicionário de compras
compras = {
    "arroz": 15.0,
    "feijão": 8.5,
    "leite": 6.0
}

# Somando os valores usando .values()
total = sum(compras.values())

print("Total da compra: R$", total)

# Explicação:
# compras.values() pega só os valores do dicionário → [15.0, 8.5, 6.0]
# sum() soma todos os valores.

### 7. Dado o dicionário:
# frutas = {"maçã": 3, "banana": 5, "laranja": 2}
# Imprima as frutas que têm mais de 2 unidades usando um laço for.

frutas = {"maçã": 3, "banana": 5, "laranja": 2}

for fruta, quantidade in frutas.items():
    if quantidade > 2:
        print(fruta)

# Explicação:
# frutas.items() retorna os pares chave e valor (("maçã", 3), etc.)
# A condição if quantidade > 2 filtra as frutas com mais de 2 unidades.

### 8. Verifique se a chave "senha" está presente no dicionário abaixo. Se não estiver, 
# adicione-a com o valor "123456".
# usuario = {"login": "joaosilva"}

usuario = {"login": "joaosilva"}

# Verificando se a chave "senha" existe
if "senha" not in usuario:
    usuario["senha"] = "123456"

print(usuario)

# Explicação:
# if "senha" not in usuario → verifica se não existe a chave "senha".
# usuario["senha"] = "123456" → adiciona a chave com o valor padrão

### 9. Use o método .items() para iterar sobre o dicionário abaixo e imprima frases como 
# "A capital de SP é São Paulo".

# capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}

capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}

for estado, capital in capitais.items():
    print(f"A capital de {estado} é {capital}")

# Explicação:
# .items() retorna pares chave-valor do dicionário.
# estado pega a sigla ("SP", "RJ"...), e capital pega o valor ("São Paulo", etc.).
# f"A capital de {estado} é {capital}" é uma f-string, 
# que junta texto com variáveis (como combinar blocos no Scratch).

### 10. Dado o dicionário abaixo, atualize o valor da chave "estoque" somando 10 unidades ao valor atual.
# produto = {"nome": "Teclado", "estoque": 15}

produto = {"nome": "Teclado", "estoque": 15}

# Atualizando o valor da chave "estoque"
produto["estoque"] = produto["estoque"] + 10

# Exibindo o dicionário atualizado
print(produto)

# Explicação:
# produto["estoque"] acessa o valor atual (15).
# produto["estoque"] + 10 soma 10.
# O novo valor (25) é atualizado no dicionário.
