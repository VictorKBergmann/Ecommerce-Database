import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()
    cursor.execute("""
        ALTER TABLE "usuarios" ADD CONSTRAINT "fk_cidade" FOREIGN KEY ( "codcidade" ) REFERENCES "cidade" ( "codcidade" );    
    """)
    resultado = cursor.fetchone()
    print('conectado ao banco de dados:',resultado)



