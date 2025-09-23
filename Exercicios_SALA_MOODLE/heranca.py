# 1. Classe Usuario e Cliente com herança
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    pass

# Criando instância
cliente1 = Cliente("Maria", "maria@email.com")
print(cliente1.nome)
print(cliente1.email)

# 2. Método exibir_informacoes() herdado
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

class Cliente(Usuario):
    pass

cliente1 = Cliente("João", "joao@email.com")
cliente1.exibir_informacoes()

# 3. Método saudacao() sobrescrito
class Usuario:
    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def saudacao(self):
        return "Olá, cliente"

cliente1 = Cliente()
print(cliente1.saudacao())  # Resultado: Olá, cliente

# 4. Atributo saldo na classe Cliente + uso do super()
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
print(f"Saldo: R${cliente1.saldo:.2f}")

# 5. Classe Funcionario e Gerente com herança em cadeia
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Funcionario(Usuario):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

class Gerente(Funcionario):
    def __init__(self, nome, email, cargo, setor):
        super().__init__(nome, email, cargo)
        self.setor = setor

gerente1 = Gerente("Carlos", "carlos@email.com", "Gerente", "TI")
print(gerente1.nome)
print(gerente1.email)
print(gerente1.cargo)
print(gerente1.setor)

# 6. Herança múltipla: Autenticacao, Permissao, Administrador
class Autenticacao:
    def login(self):
        print("Login realizado com sucesso!")

class Permissao:
    def verificar_permissao(self):
        print("Permissão concedida.")

class Administrador(Autenticacao, Permissao):
    pass

adm = Administrador()
adm.login()
adm.verificar_permissao()

# 7. Método status() com herança múltipla e __mro__
class Autenticacao:
    def status(self):
        print("Status: autenticado")

class Permissao:
    def status(self):
        print("Status: permissões verificadas")

class Administrador(Autenticacao, Permissao):
    pass

adm = Administrador()
adm.status()  # Vai imprimir: Status: autenticado

# Verificando a ordem de resolução
print(Administrador.__mro__)