import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE produto_no_carrinho (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            cod_produto INT,
            cod_carrinho INT,
            cod_pedido INT,
            quantidade INT,
            FOREIGN KEY (cod_produto) REFERENCES produto(idProd),
            FOREIGN KEY (cod_carrinho) REFERENCES carrinho(id),
            FOREIGN KEY (cod_pedido) REFERENCES venda_pedido(idTransaction)

        );""")