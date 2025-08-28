# crud_pets.py

# Dicionário para armazenar os pets
pets = {}
proximo_id = 1

# Função para cadastrar um novo pet
def cadastrar_pet(pets, proximo_id):
    nome = input("Nome do pet: ")
    idade = int(input("Idade do pet: "))
    raca = input("Raça do pet: ")

    pets[proximo_id] = {
        'nome': nome,
        'idade': idade,
        'raca': raca,
        'adotado': False
    }

    print(f"\nPet '{nome}' cadastrado com sucesso! ID: {proximo_id}")
    return proximo_id + 1

# Função para listar todos os pets
def listar_pets(pets):
    if not pets:
        print("Nenhum pet cadastrado.")
        return

    for id_pet, dados in pets.items():
        status = "Adotado" if dados['adotado'] else "Disponível"
        print(f"\nID: {id_pet}")
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']} ano(s)")
        print(f"Raça: {dados['raca']}")
        print(f"Status: {status}")

# Função para buscar pet por nome
def buscar_pet(pets):
    nome = input("Digite o nome do pet para buscar: ").lower()
    encontrados = []

    for id_pet, dados in pets.items():
        if dados['nome'].lower() == nome:
            encontrados.append((id_pet, dados))

    if encontrados:
        for id_pet, dados in encontrados:
            status = "Adotado" if dados['adotado'] else "Disponível"
            print(f"\nID: {id_pet} | Nome: {dados['nome']} | Idade: {dados['idade']} | Raça: {dados['raca']} | Status: {status}")
    else:
        print("Nenhum pet com esse nome foi encontrado.")

# Função para atualizar dados de um pet
def atualizar_pet(pets):
    id_pet = int(input("Digite o ID do pet para atualizar: "))

    if id_pet in pets:
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        raca = input("Nova raça: ")

        pets[id_pet]['nome'] = nome
        pets[id_pet]['idade'] = idade
        pets[id_pet]['raca'] = raca

        print("Informações atualizadas com sucesso!")
    else:
        print("ID inválido.")

# Função para marcar um pet como adotado
def marcar_como_adotado(pets):
    id_pet = int(input("Digite o ID do pet para marcar como adotado: "))

    if id_pet in pets:
        pets[id_pet]['adotado'] = True
        print(f"Pet '{pets[id_pet]['nome']}' marcado como adotado!")
    else:
        print("ID inválido.")

# Função para remover um pet do sistema
def remover_pet(pets):
    id_pet = int(input("Digite o ID do pet para remover: "))

    if id_pet in pets:
        nome = pets[id_pet]['nome']
        del pets[id_pet]
        print(f"Pet '{nome}' removido com sucesso.")
    else:
        print("ID inválido.")

# Função para exibir o menu
def menu():
    print("\n--- SISTEMA DE ADOÇÃO DE PETS ---")
    print("1. Cadastrar pet")
    print("2. Listar pets")
    print("3. Buscar pet por nome")
    print("4. Atualizar pet")
    print("5. Marcar como adotado")
    print("6. Remover pet")
    print("0. Sair")

# Programa principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        proximo_id = cadastrar_pet(pets, proximo_id)
    elif opcao == '2':
        listar_pets(pets)
    elif opcao == '3':
        buscar_pet(pets)
    elif opcao == '4':
        atualizar_pet(pets)
    elif opcao == '5':
        marcar_como_adotado(pets)
    elif opcao == '6':
        remover_pet(pets)
    elif opcao == '0':
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida.")
