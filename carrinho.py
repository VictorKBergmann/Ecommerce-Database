import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE carrinho (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
            ) ENGINE=InnoDB;""")

def insere_carrinho(produto, usuario,quantidade):
    sql =  f"""  SELECT cod_carrinho from usuarios WHERE id = {usuario}"""
    cursor.execute(sql)
    cod_carrinho = cursor.fetchone()
    sql = f"INSERT INTO produto_no_carrinho(cod_produto,cod_carrinho,quantidade) values ({produto}, {cod_carrinho},{quantidade})"
    cursor.execute(sql)
