# Exercícios sobre funções em Python

# 1. Função saudacao
def saudacao():
    print("Olá, bem-vindo ao Python!")

# 2. Função dobro
def dobro(numero):
    return numero * 2

# 3. Função soma
def soma(a, b):
    return a + b

# 4. Função mensagem
def mensagem(nome="visitante"):
    print(f"Olá, {nome}!")

# 5. Função operacoes
def operacoes(a, b):
    soma = a + b
    sub = a - b
    mult = a * b
    return soma, sub, mult

# 6. Função media
def media(*numeros):
    return sum(numeros) / len(numeros)

# 7. Função dados_pessoais
def dados_pessoais(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# 8. Função calculadora
def calculadora(a, b, operacao):
    if operacao == "somar":
        return a + b
    elif operacao == "subtrair":
        return a - b
    elif operacao == "multiplicar":
        return a * b
    elif operacao == "dividir":
        return a / b
    else:
        return "Operação inválida!"

# 9. Função aplicar_operacao
def aplicar_operacao(a, b, funcao):
    return funcao(a, b)

def multiplicar(a, b):
    return a * b

# -------------------------------
# Testando todas as funções
if __name__ == "__main__":

    print("\n1. Saudação:")
    saudacao()

    print("\n2. Dobro de 5 e 12:")
    print(dobro(5))
    print(dobro(12))

    print("\n3. Soma de 10 + 20:")
    print(soma(10, 20))

    print("\n4. Mensagem com e sem nome:")
    mensagem("Lucas")
    mensagem()

    print("\n5. Operações com 10 e 5:")
    print(operacoes(10, 5))

    print("\n6. Média com diferentes quantidades:")
    print(media(10, 20, 30))
    print(media(5, 7, 9, 11, 13))
    print(media(1, 2, 3, 4, 5, 6, 7))

    print("\n7. Dados pessoais:")
    dados_pessoais(nome="Ana", idade=25, cidade="São Paulo")

    print("\n8. Calculadora:")
    print(calculadora(10, 5, "somar"))
    print(calculadora(10, 5, "dividir"))

    print("\n9. Aplicar operação:")
    print(aplicar_operacao(3, 4, soma))
    print(aplicar_operacao(3, 4, multiplicar))