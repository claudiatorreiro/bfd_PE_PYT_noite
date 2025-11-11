import pymongo

# URI com parâmetro para ignorar certificados SSL inválidos
uri = "mongodb+srv://cgtorreiro_db_user:%40iPB87116063@conexaomongodb.n0tsteg.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

# Conecta ao MongoDB
cliente = pymongo.MongoClient(uri)

# Cria banco de dados e coleção
banco = cliente["meu_banco"]
colecao = banco["minha_colecao"]

# Insere um documento
documento = {
    "nome": "Claudia",
    "profissao": "Advogada",
    "apaixonada_por": "Tecnologia"
}

resultado = colecao.insert_one(documento)
print("✅ Documento inserido com ID:", resultado.inserted_id)

