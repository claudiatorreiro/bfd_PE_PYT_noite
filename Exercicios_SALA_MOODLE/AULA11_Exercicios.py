from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

class Funcionario(Pessoa):
    def falar(self):
        print("O funcionário está falando")

    def andar(self):
        print("O funcionário está andando")

    def comer(self):
        print("O funcionário está comendo")

class Aluno(Pessoa):
    def falar(self):
        print("O aluno está falando")

    def andar(self):
        print("O aluno está andando")

    def comer(self):
        print("O aluno está comendo")

func = Funcionario()
aluno = Aluno()

print("Funcionário:")
Manoel = Funcionario()
Manoel.falar()
Manoel.andar()
Manoel.comer()

print("\nAluno:")
Patricia = Aluno()
Patricia.falar()
Patricia.andar()
Patricia.comer()


#Convertida em Interface

from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self):
        pass

class Aluno(Pessoa):
    def falar(self):
        print("O aluno está falando")

    def andar(self):
        print("O aluno está andando")

    def comer(self):
        print("O aluno está comendo")

a = Aluno()
a.falar()
a.andar()
a.comer()
