import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE venda_pedido (
            idTransaction INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            endereco VARCHAR(100) NOT NULL,
            frete DECIMAL(10,2) NOT NULL,
            valorTotal DECIMAL(10,2) NOT NULL,
            data DATE NOT NULL,
            id_user INT,
            FOREIGN KEY (id_user) REFERENCES usuarios ( id )

            ) ENGINE=InnoDB;""")

resultado = cursor.fetchone()
print('conectado ao banco de dados:',resultado)



