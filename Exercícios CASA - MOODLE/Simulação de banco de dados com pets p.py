# Simulação de banco de dados com pets para adoção
animais_para_adocao = [
    {
        "nome": "Rex",
        "especie": "Cachorro",
        "idade": 3,
        "raca": "Labrador",
        "status": "disponível"
    },
    {
        "nome": "Mimi",
        "especie": "Gato",
        "idade": 2,
        "raca": "Persa",
        "status": "adotado"
    },
    {
        "nome": "Bidu",
        "especie": "Cachorro",
        "idade": 5,
        "raca": "Poodle",
        "status": "disponível"
    },
    {
        "nome": "Nina",
        "especie": "Gato",
        "idade": 1,
        "raca": "Siamês",
        "status": "disponível"
    },
    {
        "nome": "Thor",
        "especie": "Cachorro",
        "idade": 4,
        "raca": "Pitbull",
        "status": "adotado"
    }
]
# Mostrar todos os pets disponíveis
print("Pets disponíveis para adoção:")
for pet in animais_para_adocao:
    if pet["status"] == "disponível":
        print(f"- {pet['nome']} ({pet['especie']} - {pet['raca']}, {pet['idade']} anos)")


### Saída esperada:
# Pets disponíveis para adoção:
# - Rex (Cachorro - Labrador, 3 anos)
# - Bidu (Cachorro - Poodle, 5 anos)
# - Nina (Gato - Siamês, 1 anos)
