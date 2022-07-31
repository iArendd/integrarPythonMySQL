import pyodbc

dados_conexao = (

    "Driver={SQL Server};"
    "Server=DESKTOP-NJBR2JK;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)

print('Conexão bem sucedida')


cursor = conexao.cursor()


id = 4
client = "Matheus"
produto = "Carro"
data = "31/07/2022"
preco = 5000.00
quantidade = 1


insertTable = f"""INSERT INTO Vendas(id_venda, client, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{client}', '{produto}', '{data}', {preco}, {quantidade})"""


cursor.execute(insertTable)

#O comando abaixo será usado apenas quando você fará alguma alteração no banco de dados, se está apenas lendo informação, não é necessário. Commit server para efetivar a alteração.
cursor.commit()