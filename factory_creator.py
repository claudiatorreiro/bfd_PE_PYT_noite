from abc import ABC, abstractmethod

# Interface (uma para os produtos - Veículos)
class Veiculo(ABC):
    @abstractmethod
    def operacao(self) -> str:
        pass

# Produtos concretos
class Carro(Veiculo):
    def operacao(self) -> str:
        return "Dirigindo um carro"

class Moto(Veiculo):
    def operacao(self) -> str:
        return "Pilotando uma moto"

# Superclasse Creator (define o método fábrica)
class VeiculoCreator(ABC):
    @abstractmethod
    def factory_method(self) -> Veiculo:
        """Subclasses devem implementar este método para criar o produto certo"""
        pass

# Subclasses concretas do Creator
class CarroCreator(VeiculoCreator):
    def factory_method(self) -> Veiculo:
        return Carro()

class MotoCreator(VeiculoCreator):
    def factory_method(self) -> Veiculo:
        return Moto()

# Código cliente (não precisa saber qual criador está sendo usado)
def cliente_code(creator: VeiculoCreator) -> None:
    print("Cliente: Não sei qual criador está sendo usado, mas funciona.")
    print(creator.factory_method().operacao())

# --- Execução principal ---
if __name__ == "__main__":
    print("App: usando o CarroCreator.")
    cliente_code(CarroCreator())

    print("\nApp: usando o MotoCreator.")
    cliente_code(MotoCreator())
