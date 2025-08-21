# criando um dicionário
# coleções valores chave:valor- ordenados, alterável e não aceita valores duplicados
# usa {chave:valor}
# item = key:value

#Acessando dicionario
dicionario_vazio = {"item":"nome", "item": "giza"}
print(type(dicionario_vazio))

# dicionario = {
#     "nome":"Giza",
#     "idade":"44 anos",
#     "nacionalidade": "brasileira",
#     "rico":"false",
#     "filmes favoritos":"comédia romântica"}

# print(dicionario["nome"])
# print(dicionario["idade"])
# print(dicionario["nacionalidade"])
# print(dicionario["rico"])
# print(dicionario["filmes favoritos"])

# print(dicionario.get("nome"))

### listar todos itens (key:value) no dicionario
# print(dicionario.items())

### listar todas as chaves (key) no dicionario
# print(dicionario.keys())

### listar todos os valores (value) no dicionario
# print(dicionario.values())

### add itens
dicionario = {
    "nome":"Giza",
    "idade":"44 anos",
    "nacionalidade": "brasileira",
    "rico":"false",
    "filmes favoritos":"comédia romântica"}

# dicionario = {"profissão": "advogada"}
#print(dicionario)

### alterando itens
# dicionario.update ["rico":"não"]
# print(dicionario)


### apagar itens

# del.dicionario
# print(dicionario)


### cópia de dicionario

dicionario2 = dicionario.copy()
#print(dicionario)
print(f"id de dicionario: {id(dicionario)}\nid de dicionario2: {id(dicionario2)}")

for itens in dicionario.keys():
    if itens == "Giza":
        print("aprovada")