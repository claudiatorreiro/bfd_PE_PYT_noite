#1 crie uma lista com vários tipos de dados -ok
#2 criar uma lista e add dois itens e remova um - ok
#3 faça uma cópia real de uma lista
#4 crie uma lista com numeros e multiplique cada um por 5
#5 pegue a lista a1 e gere uma nova lista apenas com os valores 4 e 5 
#  a1 = [1,2,3,4,5,6] ===> [4,5]

# 1
# material = ["lápis", "papel","caneta", "livro", "borracha"]  
# print(material)

# 2
# material.insert(5, "quadro")
# print(material)

# material.insert(5, "apontador")
# print(material)

# material.remove("papel")

# 3
# material_escolar = material.copy()
# print(material_escolar)

# 4
l = []
numeros = [10,12,14]
for i in numeros:
    l.append(5 * i)
print(l)

# 5
a1 = [1,2,3,4,5,6]
a2 = a1[3:5]
print(a2)


