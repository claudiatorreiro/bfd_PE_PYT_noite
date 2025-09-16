# Lista de Exercícios – POO classes e objetos
# 1. Na classe, ContaBancaria, converta saldo para uma atributo privado. 
# Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)

# class ContaBancaria:
#     def __init__(self, titular, saldo_inicial=0.0):
#         self.titular = titular
#         self.__saldo = saldo_inicial  # saldo privado __

#     # Getter para o saldo
#     def get_saldo(self):
#         return self.__saldo

#     # Setter para o saldo com regra lógica
#     def set_saldo(self, novo_saldo):
#         if novo_saldo < 0:
#             print("Erro: O saldo não pode ser negativo.")
#         else:
#             self.__saldo = novo_saldo

#     # Método para exibir informações da conta
#     def exibir_conta(self):
#         print(f"Titular: {self.titular} | Saldo: R${self.get_saldo():.2f}")


# # Teste da classe
# conta1 = ContaBancaria("Maria", 1000.0)
# conta1.exibir_conta()

# # Tentando alterar o saldo com valor válido
# conta1.set_saldo(500.0)
# conta1.exibir_conta()

# # Tentando alterar o saldo com valor negativo
# conta1.set_saldo(-200.0)
# conta1.exibir_conta()

# 2. Crie uma classe, Pessoa, que tenha os atributos: 
# nome, data de nascimento, cpf, identidade. Deixe os atributos cpf e identidade como privado e 
# monte os métodos setters e getters para acessar e editar os valores

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf  # Atributo privado
        self.__identidade = identidade  # Atributo privado

    # Getter para CPF
    def get_cpf(self):
        return self.__cpf

    # Setter para CPF
    def set_cpf(self, novo_cpf):
        if isinstance(novo_cpf, str) and len(novo_cpf) == 14:  # Ex: 000.000.000-00
            self.__cpf = novo_cpf
        else:
            print("CPF inválido. O formato correto é '000.000.000-00'.")

    # Getter para Identidade
    def get_identidade(self):
        return self.__identidade

    # Setter para Identidade
    def set_identidade(self, nova_identidade):
        if isinstance(nova_identidade, str) and len(nova_identidade) >= 5:
            self.__identidade = nova_identidade
        else:
            print("Identidade inválida. Verifique o valor.")

    # Método auxiliar para exibir os dados da pessoa
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Identidade: {self.get_identidade()}")


# Testando a classe
pessoa1 = Pessoa("João Silva", "10/05/1990", "123.456.789-00", "MG1234567")
pessoa1.exibir_dados()

# Alterando CPF e Identidade
pessoa1.set_cpf("111.222.333-44")
pessoa1.set_identidade("MG7654321")

print("\nApós alteração:")
pessoa1.exibir_dados()
