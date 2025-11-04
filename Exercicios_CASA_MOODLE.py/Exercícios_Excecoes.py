# 1. Solicitar um número inteiro com tratamento de erro
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou: {numero}")
except ValueError:
    print("Erro: Isso não é um número inteiro.")

# 2. Multiplicação com verificação de entrada inválida
try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    resultado = a * b
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")

# 3. Conversão com else após sucesso
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Isso não é um número válido.")
else:
    print(f"Conversão bem-sucedida. Você digitou {numero}.")

# 4. Abertura de arquivo com try e finally
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Arquivo 'dados.txt' não encontrado.")
finally:
    print("Encerrando programa.")

# 5. Função dividir(a, b) com raise ZeroDivisionError
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b

# Exemplo de uso
try:
    print(dividir(10, 2))
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print(f"Erro: {e}")

# 6. Exceção personalizada IdadeInvalidaError
class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa.")
    print(f"Idade cadastrada: {idade}")

# Exemplo de uso
try:
    idade = int(input("Digite sua idade: "))
    cadastrar_idade(idade)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
except ValueError:
    print("Erro: Digite um número inteiro válido.")

# 7. Divisão com tratamento de dois tipos de erro
try:
    num1 = float(input("Digite o numerador: "))
    num2 = float(input("Digite o denominador: "))
    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

# 8. Verificar se número é par com try, else e finally
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: Isso não é um número inteiro.")
else:
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
finally:
    print("Fim do programa.")

# 9. Função sacar() com exceção personalizada SaldoInsuficienteError
class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
    return saldo - valor

# Exemplo de uso
try:
    saldo_atual = 500
    valor_saque = float(input("Digite o valor do saque: "))
    novo_saldo = sacar(saldo_atual, valor_saque)
    print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
except ValueError:
    print("Erro: Digite um valor numérico válido.")