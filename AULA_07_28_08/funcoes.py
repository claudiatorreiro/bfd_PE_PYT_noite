# bloco de código que só é executado quando chamado - evita repetição
# def nome_funcao(argumento-variavel)
#     código:

# EX:

# def saudacao():
#     print("Olá! Tudo bem?")

# saudacao()

# def soma(*nuns): #não tem como saber quantos valores
#     resultado=0 #sempre dentro da função
#     for numero in nuns:
#         resultado+=numero
#     return resultado

# print(soma(2,3,5,2,7))

# def saudacao(nome = "João", sobrenome = "Silva"):
#     return f"Olá, {nome}" {sobrenome}! Tudo bem?"

def soma(num1,num2):
    return num1 + num2

from funcoes import soma

resultado = soma(5,3)
print(resultado)
