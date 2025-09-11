# Exercício 1:
# Escreva um programa que peça ao usuário para digitar um número.
# Trate o erro caso ele digite algo que não seja um número inteiro.

# try:
#     numero = int(input("Digite um número inteiro: "))
#     print("Você digitou:", numero)

# except ValueError:
#     print("Erro! Você não digitou um número inteiro.")


# Exercício 2 – Enunciado
# Peça ao usuário dois números e tente multiplicá-los.
# Se o usuário digitar algo inválido, exiba uma mensagem de erro.

# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     resultado = num1 * num2

#     print(f"Resultado da multiplicação: {resultado}")

# except ValueError:
#     print("Erro! Você precisa digitar apenas números.")

# Exercício 3 
# Crie um programa que peça ao usuário um número inteiro.
# Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.

# try:
#     numero = int(input("Digite um número inteiro: "))

# except ValueError:
#     print("Erro! Você não digitou um número inteiro.")

# else:
#     print(f"Parabéns! Você digitou o número {numero}")

# Exercício 4 
# Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir).
# Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.

# try:
#     arquivo = open("dados.txt", "r")  # Tenta abrir o arquivo no modo leitura
#     conteudo = arquivo.read()
#     print("Arquivo aberto com sucesso!")
#     print(conteudo)

# except FileNotFoundError:
#     print("Erro: O arquivo 'dados.txt' não foi encontrado.")

# finally:
#     print("Encerrando programa...")

# Exercício 5 
# Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero.
# Caso contrário, retorne o resultado da divisão normalmente.

# def dividir(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Você tentou dividir por zero.")
#     return a / b

# try:
#     resultado = dividir(10, 2)
#     print("Resultado:", resultado)

# except ZeroDivisionError as erro:
#     print("Erro ao dividir:", erro)

# Exercício 6
# Crie uma exceção personalizada chamada IdadeInvalidaError.
# Depois, crie uma função cadastrar_idade(idade) que lança essa exceção caso a idade seja negativa.

# class IdadeInvalidaError(Exception):
#     pass

# def cadastrar_idade(idade):
#     if idade < 0:
#         raise IdadeInvalidaError("Idade não pode ser negativa!")
#     print(f"Idade {idade} cadastrada com sucesso.")

# try:
#     idade = int(input("Digite sua idade: "))
#     cadastrar_idade(idade)

# except IdadeInvalidaError as erro:
#     print("Erro:", erro)

# except ValueError:
#     print("Erro: Você precisa digitar um número inteiro.")

# Exercício 7 
# Peça ao usuário dois números e divida o primeiro pelo segundo.
# Trate dois tipos de erro:
# ValueError se o usuário digitar algo inválido (ex: letras).
# ZeroDivisionError se tentar dividir por zero.

# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     resultado = num1 / num2

# except ValueError:
#     print("Erro: Você precisa digitar apenas números.")

# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")
    
# else:
#     print(f"Resultado da divisão: {resultado}")

# Exercício 8 
# Crie um programa que peça ao usuário um número inteiro e verifique se ele é par.
# Use:
# try para tentar converter a entrada
# else para verificar se é par ou ímpar
# finally para exibir "Fim do programa"

# try:
#     numero = int(input("Digite um número inteiro: "))

# except ValueError:
#     print("Erro: Você não digitou um número inteiro.")

# else:
#     if numero % 2 == 0:
#         print(f"O número {numero} é par.")
#     else:
#         print(f"O número {numero} é ímpar.")

# finally:
#     print("Fim do programa.")


# Exercício 9 
# Crie uma função sacar(saldo, valor) que:
# Lance uma exceção personalizada chamada SaldoInsuficienteError se o valor for maior que o saldo.
# Caso contrário, retorne o novo saldo.
# Teste a função dentro de um bloco try-except e exiba uma mensagem apropriada ao usuário.

class SaldoInsuficienteError(Exception):
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
    return saldo - valor

try:
    saldo = float(input("Digite seu saldo atual: "))
    valor_saque = float(input("Digite o valor que deseja sacar: "))
    
    novo_saldo = sacar(saldo, valor_saque)
    print(f"Saque realizado com sucesso! Novo saldo: R$ {novo_saldo:.2f}")

except SaldoInsuficienteError as erro:
    print("Erro:", erro)
    
except ValueError:
    print("Erro: Digite apenas números válidos.")
