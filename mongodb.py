import pymongo

# URI completa com usuário, senha (codificada) e host correto
uri = (
    "mongodb+srv://cgtorreiro_db_user:%40iPB87116053"
    "@conexaomongodb.n0tsteg.mongodb.net/"
    "?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true&appName=conexaomongodb"
)

# Cria o cliente e tenta conectar
conexao = pymongo.MongoClient(uri)

print("✅ Conectado com sucesso!")

# Testa o status do servidor
try:
    conexao.admin.command("ping")
    print("✅ Conexão com MongoDB está ativa!")
except Exception as e:
    print("❌ Erro ao tentar conectar:", e)

# (Opcional) Exibe as informações do servidor
try:
    print(conexao.server_info())
except Exception as e:
    print("⚠️ Não foi possível obter informações do servidor:", e)

