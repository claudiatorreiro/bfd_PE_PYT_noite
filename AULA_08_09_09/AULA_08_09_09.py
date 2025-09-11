# print(list([("casa","predio")])) - criando uma list

#criando uma classe
# class Cachorro:... #palavra reservada *sempre a primeira letra maiuscula

# # Adicionando atributos de classe
# class Cachorro:
#     especie = "Canis lupus familiaris"
#     nome = "Toto"
#     raca = "caramelo"
#     idade = 2

# # Instanciando objeto
# auau = Cachorro()
# print(auau)

# # Acessando os atributos do objeto
# print(auau.especie, auau.nome, auau.raca, auau.idade, sep="\n")

# print(Cachorro.nome)

# Atributos de objetos
# __init__ - metodo construtor

class Cachorro:
    especie = "Canis lupus familiaris"
    dono = "Fred"
    
    def __init__(self, nome: str, idade: int, raca: str = "caramelo"):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        
    def __str__(self):
        return f"Especie: {self.especie}\nNome: {self.nome}\nRaca: {self.raca}\nIdade: {self.idade}"
    
    def latir(self):
        print("auauauaau")
    
    def correr(self, metros):
        print(f"{self.nome} correu {metros}m")

# Criar o objeto com raça padrão
auau = Cachorro("Rex", 3)

print(auau)
auau.latir()
auau.correr(50)




# doguinho01 = Cachorro("Rex", "caramelo", 2)
# print(doguinho01)
# print(doguinho01.especie, doguinho01.nome, doguinho01.raca, doguinho01.idade, sep="\n")
# print(Cachorro.especie)

# doguinho02 = Cachorro("Max", "Toto", 3)
# print(doguinho02)
# print(doguinho02.especie, doguinho02.nome, doguinho02.raca, doguinho02.idade, sep="\n")
