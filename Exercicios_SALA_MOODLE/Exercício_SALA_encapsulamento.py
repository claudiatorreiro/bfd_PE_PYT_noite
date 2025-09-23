# Crie uma classe ContaBancaria com os atributos titular e saldo. 
# Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). 
# Teste com depósitos e saques.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque.")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

conta = ContaBancaria("Ana", 100)
conta.exibir_saldo()
conta.depositar(50)
conta.sacar(30)
conta.sacar(150)
conta.exibir_saldo()

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Saldo insuficiente para saque.")
            return False

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")


conta = ContaBancaria("João", 100)

conta.depositar(50)

if conta.sacar(120):
    print("Saque efetuado com sucesso.")
else:
    print("Não foi possível realizar o saque.")

if conta.sacar(50):
    print("Saque efetuado com sucesso.")
else:
    print("Não foi possível realizar o saque.")

conta.exibir_saldo()


# Modifique a classe ContaBancaria para que o método sacar retorne True se a operação for bem-sucedida e False caso contrário. 
# Teste o retorno e imprima mensagens adequadas.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    # Getter do saldo
    def get_saldo(self):
        return self.__saldo

    # Setter do saldo com regra: não pode ser negativo
    def set_saldo(self, valor):
        if valor < 0:
            print("Erro: O saldo não pode ser negativo.")
        else:
            self.__saldo = valor

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Saque não autorizado. Saldo insuficiente ou valor inválido.")
            return False

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.__saldo:.2f}")


conta = ContaBancaria("Maria", 200)

# Usando getter
print("Saldo inicial:", conta.get_saldo())

# Usando setter com valor inválido
conta.set_saldo(-100)  # Deve exibir erro

# Setter com valor válido
conta.set_saldo(500)
print("Novo saldo:", conta.get_saldo())

# Na classe, ContaBancaria, converta saldo para uma atributo privado. 
# Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica 
# (Ex: saldo não pode ser negativo)

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    # Getter do saldo
    def get_saldo(self):
        return self.__saldo

    # Setter do saldo com regra: não pode ser negativo
    def set_saldo(self, valor):
        if valor < 0:
            print("Erro: O saldo não pode ser negativo.")
        else:
            self.__saldo = valor

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Saque não autorizado. Saldo insuficiente ou valor inválido.")
            return False

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.__saldo:.2f}")


conta = ContaBancaria("Maria", 200)

# Usando getter
print("Saldo inicial:", conta.get_saldo())

# Usando setter com valor inválido
conta.set_saldo(-100)  # Deve exibir erro

# Setter com valor válido
conta.set_saldo(500)
print("Novo saldo:", conta.get_saldo())

# Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. 
# Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar e editar os valores

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf                # Atributo privado
        self.__identidade = identidade  # Atributo privado

    # Getters
    def get_cpf(self):
        return self.__cpf

    def get_identidade(self):
        return self.__identidade

    # Setters com simples validação de tamanho
    def set_cpf(self, novo_cpf):
        if len(novo_cpf) == 11 and novo_cpf.isdigit():
            self.__cpf = novo_cpf
        else:
            print("CPF inválido. Deve conter 11 dígitos.")

    def set_identidade(self, nova_identidade):
        if nova_identidade:
            self.__identidade = nova_identidade
        else:
            print("Identidade não pode ser vazia.")

pessoa = Pessoa("João", "01/01/2000", "12345678900", "MG1234567")

print("CPF:", pessoa.get_cpf())
print("Identidade:", pessoa.get_identidade())

# Tentando alterar CPF com valor inválido
pessoa.set_cpf("abc")  # Erro
pessoa.set_cpf("98765432100")  # Correto

# Exibindo novamente
print("Novo CPF:", pessoa.get_cpf())
