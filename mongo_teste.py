import pymongo
from urllib.parse import quote_plus

usuario = quote_plus("ctporneiro_db_user")
senha = quote_plus("%40iPB87B11603")  # '@' precisa ser codificado
cluster = "conexaomongodb.n0tsteg.mongodb.net"
banco = "conexaomongodb"

# URI com SSL, mas desabilitando verificação de certificado
uri = f"mongodb+srv://{usuario}:{senha}@{cluster}/?retryWrites=true&tls=true&tlsAllowInvalidCertificates=true"

try:
    conexao = pymongo.MongoClient(uri)
    conexao.admin.command("ping")  # testa conexão
    print("✅ Conectado ao MongoDB com sucesso!")
    print("ℹ️ Informações do servidor:")
    print(conexao.server_info())
except Exception as e:
    print("❌ Erro ao tentar conectar:", e)
