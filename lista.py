import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE lista (
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cod_produto INT,
            FOREIGN KEY ( cod_produto ) REFERENCES produto ( idprod )
        );""")

resultado = cursor.fetchone()
print('conectado ao banco de dados:',resultado)