from abc import ABC, abstractmethod

# Interface (classe abstrata)
class Animal(ABC):

    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

    def mover(self):
        print("O cachorro está correndo")

class Gato(Animal):
    def falar(self):
        print("Miau")

    def mover(self):
        print("O gato está pulando")

def interagir_com_animal(animal: Animal):
    animal.falar()
    animal.mover()

# Criando os objetos
dog = Cachorro()
cat = Gato()

# Interagindo com ambos sem saber quem é quem!
interagir_com_animal(dog)
interagir_com_animal(cat)

