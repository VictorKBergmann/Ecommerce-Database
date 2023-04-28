import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE produto_no_carrinho (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            quatidade INT NOT NULL,
            cod_produto INT,
            FOREIGN KEY ( cod_produto ) REFERENCES produto ( idProd ),
            cod_cep INT,
            FOREIGN KEY ( cod_cep ) REFERENCES cep ( cep )

        );""")