frutas = ["banana", "manga", "laranja", "jaca", "jaca", ["sal", "pimenta"]]

#print(frutas[-1])

frutas[-1] = "pimenta do reino"
frutas[-1] [-1]
print(frutas)

# salada_de_fruta = frutas

# print(id(frutas))
# print(id(salada_de_fruta))

# salada_de_fruta.append("melão")
# print(id(frutas))
# print(id(salada_de_fruta))


# print(frutas[:])
# print(frutas)

### ADD ELEMENTS

temperos = ["pimenta", "sal"]
frutas += temperos

# frutas.append("manga")
# frutas.insert(-1, "limão")
# frutas.append("jacas")
# # fruta = "manga"

# print(frutas)

#### REMOVER ITENS
#frutas.remove("manga")
#temperos.remove("sal")

#frutas.pop(1)
#temperos.pop(1)

#del frutas[2]

#frutas.remove("jaca")]

#frutas.pop()
# frutas.pop(2)
# print(frutas)

#print(frutas.clear())
#print(temperos)

#### ORDENAR LISTAS
#sorted - ordena temporariamente
#sort - ordena definitivamente

# print(sorted(frutas))
# frutas.sort(reverse=True) - ordem inversa
# print(frutas)

# frutas[1] = "mangaba" - modifica um elemento dentro da lista
# print(frutas)

# fruta = "morango"

# morango_do_amor = fruta

#print(morango_do_amor)

# print(id(fruta))
# print(id(morango_do_amor))
# fruta = "molango"
# print(id(fruta))
# print(id(morango_do_amor))

#### COPIAR LISTA DE FORMA INTELIGENTE

#salada_de_fruta = frutas.copy()

# salada_de_fruta = ["maça"]
# print(frutas)
# idx_jaca = frutas.index("jaca")
# frutas.pop(idx_jaca)
# print(frutas)

#salada_de_fruta.extend(frutas)

# print(frutas.index("banana"))
# print(frutas.index("jaca"))

# print(salada_de_fruta)

#salada_de_fruta = fruta[:]

# for fruta in frutas:
#     salada_de_fruta.append(fruta)
#     print(fruta)
#     print(salada_de_fruta)

# print(frutas.count("jaca"))

# print(id(fruta))
# print(id(salada_de_fruta))