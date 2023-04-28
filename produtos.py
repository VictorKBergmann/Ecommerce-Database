import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE produto (
        idprod INT NOT NULL AUTO_INCREMENT,
        preco FLOAT,
        imagemUrl VARCHAR(200),
        descricao VARCHAR(500),
        PRIMARY KEY (idprod)
    );""")

resultado = cursor.fetchone()
print('conectado ao banco de dados:',resultado)