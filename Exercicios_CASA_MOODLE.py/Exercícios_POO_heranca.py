# Exercício 1
# Crie uma classe Usuario com atributos nome e email. Depois, crie uma classe Cliente que herde de Usuario. 
# Crie uma instância de um cliente e acesse todos os atributos.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario): 
    pass

# Criando um cliente
cliente1 = Cliente("Ana", "ana@email.com")
cliente2 = Cliente("Giza", "giza@email.com")

# Acessando os atributos herdados
print(cliente1.nome)   # Ana
print(cliente1.email)  # ana@email.com

print(cliente2.nome)   
print(cliente2.email)

# Exercício 2
# Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente. 
# Mostre como chamar o método herdado a partir de um objeto Cliente.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome} - Email: {self.email}")

class Cliente(Usuario):
    pass

cliente1 = Cliente("Ana", "ana@email.com")
cliente1.exibir_informacoes()

cliente2 = Cliente("Giza", "giza@email.com")
cliente2.exibir_informacoes()

# Exercício 3
# Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". 
# Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente".

class Usuario:
    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def saudacao(self):
        return "Olá, cliente"

cliente1 = Cliente()
print(cliente1.saudacao())  # Olá, cliente

cliente2 = Cliente()
print(cliente2.saudacao())

# Exercício 4
# Na classe Cliente, adicione o atributo saldo. 
# Adicione um método construtor em Cliente que inicialize também os atributos de Usuario usando super().

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

cliente1 = Cliente("Ana", "ana@email.com", 500)
print(cliente1.nome)
print(cliente1.email)
print(cliente1.saldo)

cliente2 = Cliente("Giza", "giza@email.com", 1500)
print(cliente2.nome)
print(cliente2.email)
print(cliente2.saldo)

# Exercício 5
# Crie uma classe Funcionario que herda de Usuario e, em seguida, crie uma classe Gerente que herda de Funcionario. 
# Mostre como instanciar um gerente e acessar seus atributos.

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, departamento):
        super().__init__(nome, email, cargo)
        self.departamento = departamento

# Criando uma instância de Gerente
gerente1 = Gerente("Carlos", "carlos@empresa.com", "Gerente", "TI")
gerente2 = Gerente("João", "joao@empresa.com", "Gerente", "Financeiro")

# Acessando os atributos
print(gerente1.nome)
print(gerente1.email)
print(gerente1.cargo)
print(gerente1.departamento)

print(gerente2.nome)
print(gerente2.email)
print(gerente2.cargo)
print(gerente2.departamento)

# Exercício 6
# Crie uma classe Autenticacao com um método login(). 
# Crie outra classe Permissao com um método verificar_permissao(). 
# Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?

class Autenticacao:
    def login(self):
        print("Login realizado com sucesso!")

class Permissao:
    def verificar_permissao(self):
        print("Permissão concedida.")

class Administrador(Autenticacao, Permissao):
    pass

# Criando instância e utilizando métodos herdados
adm = Administrador()
adm.login()
adm.verificar_permissao()

# Exercício 7
# Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. 
# Se a classe Administrador herda das duas, qual versão de status() será chamada? 
# Use Administrador.__mro__ para mostrar a ordem.

class Autenticacao:
    def status(self):
        print("Status: autenticado")

class Permissao:
    def status(self):
        print("Status: permissões verificadas")

class Administrador(Autenticacao, Permissao):
    pass

adm = Administrador()
adm.status()  # Vai chamar o método de Autenticacao, pois ela vem primeiro

# Ordem de resolução de métodos
print(Administrador.__mro__)
