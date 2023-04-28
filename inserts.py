import mysql.connector
con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')

if con.is_connected():
    db_info = con.get_server_info()
    print('conectado ao servidor MySQL versão:', db_info)
    cursor = con.cursor()


lista_usuario= [{'endereco':'Rua das Flores, 123','frete':15.99, 'valor_pedido':102.50, 'data':'2023-04-10'}, 
        {'endereco':'Avenida do Sol, 453','frete':20.00, 'valor_pedido':78.30, 'data':'2023-04-12'},
        {'endereco':'Rua das Palmeiras, 789','frete':10.50, 'valor_pedido':45.70, 'data':'2023-04-14'}]

for usuario in lista_usuario:
    insert_pedido(usuario.get('endereco'),usuario.get('frete'),usuario.get('valor_pedido'),usuario.get('data'))



lista_lista= [{'nome':'Ofertas'}, 
        {'nome':'Alimentos'},
        {'nome':'Eletrodomesticos'},
        {'nome':'Higiene'},
        {'nome':'Livros'}]

for lista in lista_lista:
    insert_lista(lista.get('nome'))



lista_produtos= [{'preco':'9.99','imagemUrl':'https://static1.patasdacasa.com.br/articles/6/37/16/@/14887-fotos-de-cachorros-filhotes-com-seus-bri-articles_media_slider_mobile-2.jpg','descricao':'cachorro fofo'}, 
        {'preco':'19.99','imagemUrl':'https://static1.patasdacasa.com.br/articles/6/37/16/@/14941-fotos-de-cachorros-pequenos-precisam-ter-articles_media_slider_mobile-2.jpg','descricao':'cachorro fofuxo'},
        {'preco':'29.99','imagemUrl':'https://noticias.buscavoluntaria.com.br/wp-content/uploads/2019/03/kitten-solid-white-cat-motherless-child.jpg','descricao':'gato fofo'}]

for produto in lista_produtos:
    insert_produtos(produto.get('preco'),produto.get('imagemUrl'),produto.get('descricao'))



lista_usuarios= [{'nome':'João Silva','cartao':'1234567890123456','email':'joao.silva@gmail.com'}, 
        {'nome':'Maria Souza','cartao':'2345678901234567','email':'maria.souza@hotmail.com'},
        {'nome':'Carlos Santos','cartao':'3456789012345678','email':'carlos.santos@yahoo.com'}]

for usuario in lista_usuarios:
    insert_usuarios(usuario.get('nome'),usuario.get('cartao'),usuario.get('email'))




lista_venda= [{'endereco':'Rua das Flores, 123','frete':15.99, 'valor_pedido':102.50, 'data':'2023-04-10'}, 
        {'endereco':'Avenida do Sol, 453','frete':20.00, 'valor_pedido':78.30, 'data':'2023-04-12'},
        {'endereco':'Rua das Palmeiras, 789','frete':10.50, 'valor_pedido':45.70, 'data':'2023-04-14'}]

for venda in lista_venda:
    insert_venda(venda.get('endereco'),venda.get('frete'),venda.get('valor_pedido'),venda.get('data'))



lista_ceps= [{'cep':'12345678','cidade':'São Paulo','estado':'SP'}, 
        {'cep':'87654321','cidade':'Rio de Janeiro','estado':'RJ'},
        {'cep':'23456789','cidade':'Belo Horizonte','estado':'MG'}]

for ceps in lista_ceps:
    insert_ceps(ceps.get('cep'),ceps.get('cidade'),ceps.get('estado'))

def insert_pedido(endereco, frete,valor_pedido,data):
    val =  (endereco, frete, valor_pedido, data)
    sql = "INSERT INTO venda_pedido (endereco, frete, valorTotal, data) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, val)