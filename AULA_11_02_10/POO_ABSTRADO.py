from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def correr(self):
        pass

class Estudante(Pessoa):
    def comer(self):
        print("Estudante está comendo")

    def andar(self):
        print("Estudante está andando")

    def correr(self):
        print("Estudante está correndo")

joao = Estudante()
joao.comer()
joao.andar()
joao.correr()


