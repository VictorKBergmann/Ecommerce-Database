import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE cep (
        cep CHAR(8) NOT NULL,
        cidade VARCHAR(100) NOT NULL,
        estado CHAR(2) NOT NULL,
        PRIMARY KEY (cep)
    );""")

resultado = cursor.fetchone()
print('conectado ao banco de dados:',resultado)
