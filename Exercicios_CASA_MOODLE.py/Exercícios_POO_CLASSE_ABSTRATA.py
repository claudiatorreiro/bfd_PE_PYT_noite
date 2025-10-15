from abc import ABC, abstractmethod

# Classe abstrata
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

# Classes concretas
class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

# Criando objetos e chamando o método falar
cachorro = Cachorro()
gato = Gato()

print(cachorro.falar())  # Saída: Au Au!
print(gato.falar())      # Saída: Miau!


#animal = Animal()  # Tentar instanciar a classe abstrata


from abc import ABC, abstractmethod

# Classe abstrata
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Classe concreta
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

# Teste
ret = Retangulo(5, 3)
print("Área:", ret.area())          # Saída: Área: 15
print("Perímetro:", ret.perimetro())  # Saída: Perímetro: 16


from abc import ABC, abstractmethod

# Classe abstrata
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

# Subclasse que implementa apenas um método
class Carro(Transporte):
    def mover(self):
        print("Carro está se movendo")

# Tentar instanciar Carro
# carro = Carro()  # Isso gerará um erro!

class Carro(Transporte):
    def mover(self):
        print("Carro está se movendo")

    def parar(self):
        print("Carro parou")

# Agora é possível instanciar
carro = Carro()
carro.mover()  # Saída: Carro está se movendo
carro.parar()  # Saída: Carro parou
