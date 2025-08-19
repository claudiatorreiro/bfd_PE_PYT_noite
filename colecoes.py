### TUPLAS - não consegue modificar igual a lista
## tuplas x lista = não pode fazer adicoes por que ela é mais leve menos memoria
##como define a tupla = além dos () é a virgula tupla1 = (_) tupla1 = (1,) lista []
# converte em lista
# nome = "Giza"
# print(list(nome))

# - criando tupla
# tupla1 = (1,) 

# print(type(tupla1))

# tupla1 = (1,2,3,4) 
# for num in tupla1:
#     print(num+5)

# print(type(tupla1))

# tupla1 = ("Fred","João","Maria") 

# print(tupla1.index("Fred")) - busca o numero do index
# print(tupla1.count("Fred")) - conta a quantidade

#### CONJUNTO SET

# teste = {"Fred", "Fred"}
# print(teste)

# teste = {"Fred"}
# print(type(teste))

# teste = {1,2}
# teste.add(4)
# print(teste)

# teste = {1,2}
# teste.clear()
# print(teste)

# teste = {1,2}
# teste2 = teste.copy
# print(teste)

frutas = {"banana", "limão", "tomate"}
legumes = {"cenoura", "tomate", "beterraba"}
# print(frutas.difference(legumes))
# print(legumes.difference(frutas))
# print(legumes.difference_update(frutas))
# print(legumes)
# 

# print(legumes.intersection(legumes))
# print(legumes & frutas)
# print(legumes | frutas)
# print(legumes.intersection(frutas))

lista_alunos = {"nome": "Giza",
                "idade": "44 anos",
                "cidade":"Recife/PE",
                "turma": ("turma 34", "turma 36") , }
