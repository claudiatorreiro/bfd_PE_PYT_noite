idade = int(input("Qual a sua idade?"))
carteira = input(("Tem carteira de motorista?" 
"(Sim/Não): "))
cachaca = input(("Ingeriu bebida alcoolica?" 
"(Sim/Não): "))

if idade >= 18 and carteira == "Sim" and cachaca == "Sim":
    print("Você não pode dirigir")