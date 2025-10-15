# ===========================================
# Atividade: POO - Associação / Agregação / Composição
# ===========================================

print("\n=== 1. Associação: Pessoa e Livro ===")

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def ler(self, livro):
        print(f"{self.nome} está lendo '{livro.titulo}'.")

livro1 = Livro("Python para Iniciantes")
pessoa1 = Pessoa("Ana")
pessoa1.ler(livro1)


print("\n=== 2. Agregação: Aluno e Ônibus ===")

class Onibus:
    def __init__(self, linha):
        self.linha = linha

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def pegar_onibus(self, onibus):
        print(f"{self.nome} está pegando o ônibus da linha {onibus.linha}.")

onibus1 = Onibus("742")
aluno1 = Aluno("Carlos")
aluno1.pegar_onibus(onibus1)


print("\n=== 3. Agregação: Departamento e Funcionários ===")

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Funcionários do departamento {self.nome}:")
        for f in self.funcionarios:
            print(f"- {f.nome}")

f1 = Funcionario("Lucas")
f2 = Funcionario("Maria")
dep = Departamento("RH")
dep.adicionar_funcionario(f1)
dep.adicionar_funcionario(f2)
dep.listar_funcionarios()


print("\n=== 4. Agregação: Time e Jogadores ===")

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def escalar(self):
        print(f"Escalação do {self.nome}:")
        for j in self.jogadores:
            print(f"- {j.nome} ({j.posicao})")

j1 = Jogador("Ronaldo", "Atacante")
j2 = Jogador("Carlos", "Lateral")
time = Time("Brasil FC")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)
time.escalar()


print("\n=== 5. Composição: Carro e Motor ===")

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print(f"Motor {self.tipo} ligado.")

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor("1.6")

    def ligar_carro(self):
        print(f"Ligando o carro {self.modelo}")
        self.motor.ligar()

carro = Carro("Fusca")
carro.ligar_carro()

del carro
print("Carro deletado. O motor também deixou de existir.")


print("\n=== 6. Composição: Casa e Cômodos ===")

class Comodo:
    def __init__(self, nome):
        self.nome = nome

class Casa:
    def __init__(self):
        self.comodos = [
            Comodo("Sala"),
            Comodo("Cozinha"),
            Comodo("Quarto"),
            Comodo("Banheiro")
        ]

    def mostrar_comodos(self):
        print("Cômodos da casa:")
        for c in self.comodos:
            print(f"- {c.nome}")

casa = Casa()
casa.mostrar_comodos()
