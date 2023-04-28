import mysql.connector
from datetime import datetime

def insert_produtos(preco, imagemUrl, descricao):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    sql = f"BEGIN;INSERT INTO produto (preco, imagemUrl, descricao) VALUES ({preco}, '{imagemUrl}', '{descricao}');COMMIT;"
    print(sql)
    cursor.execute(sql)
    cursor.close()
    con.close()

def insert_usuarios(nome, cartao, email):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    sql = f"""BEGIN;
                INSERT INTO carrinho(id) values(null);
                INSERT INTO usuarios (nome, cartao, email,cod_carrinho) VALUES ('{nome}', {cartao}, '{email}', (SELECT max(id) FROM carrinho));
            COMMIT;
            """
    print(sql)
    cursor.execute(sql)
    cursor.close()
    con.close()

def insert_ceps(cep, cidade, estado):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    sql = f"BEGIN;INSERT INTO cep (cep, cidade, estado) VALUES ('{cep}', '{cidade}', '{estado}');COMMIT;"
    print(sql)
    cursor.execute(sql)
    cursor.close()
    con.close()

def insert_lista(nome,id):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    sql = f"BEGIN;INSERT INTO lista (nome,cod_produto) VALUES ('{nome}',{id});COMMIT;"
    cursor.execute(sql)
    cursor.close()
    con.close()


def insert_produto_no_carrinho(codigo_produto,usuario,quantidade):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    data = datetime.today().strftime('%Y-%m-%d')
    cursor.execute(f"""
        BEGIN;
        insert into produto_no_carrinho (cod_produto,cod_carrinho,quantidade) values (
            {codigo_produto},
            (select cod_carrinho from usuarios where id = {usuario}),
            {quantidade}
        );
        COMMIT;"""
    )

    cursor.close()
    con.close()



def insert_venda(endereco, frete,usuario):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    data = datetime.today().strftime('%Y-%m-%d')
    cursor.execute(f"""
        BEGIN;
        insert into venda_pedido (endereco,frete,valorTotal,data,id_user) values (
            '{endereco}',
            {frete},
            (select SUM(produto.preco*produto_no_carrinho.quantidade) from produto_no_carrinho
                join produto
                on produto_no_carrinho.cod_produto = produto.idProd
                and produto_no_carrinho.cod_carrinho = (select cod_carrinho from usuarios where id = {usuario})
            ),
            {data},
            {usuario}
        );
        update produto_no_carrinho 
        set cod_carrinho = null, cod_pedido = (select max(idTransaction) from venda_pedido)
        where cod_carrinho = (select cod_carrinho from usuarios where id = {usuario});
        COMMIT;"""
    )
    cursor.close()
    con.close()