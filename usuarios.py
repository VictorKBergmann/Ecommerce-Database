import mysql.connector

con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE usuarios(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nome char(150), 
            cartao VARCHAR(70),
            email VARCHAR(150),
            cod_carrinho INT,
            FOREIGN KEY ( cod_carrinho ) REFERENCES carrinho ( id )
        );""")
    resultado = cursor.fetchone()

resultado = cursor.fetchone()
print('conectado ao banco de dados:',resultado)
