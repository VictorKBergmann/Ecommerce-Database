import mysql.connector
from datetime import datetime
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/insert_produtos/")
async def insert_produtos(preco: float = Query(default=None), imagemUrl: str = Query(default=None), descricao: str = Query(default=None)):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    sql = f"BEGIN;INSERT INTO produto (preco, imagemUrl, descricao) VALUES ({preco}, '{imagemUrl}', '{descricao}');COMMIT;"
    print(sql)
    cursor.execute(sql)
    cursor.close()
    con.close()

@app.get("/insert_usuarios/")
async def insert_usuarios(nome: str = Query(default=None), cartao: str = Query(default=None), email: str = Query(default=None)):
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

@app.get("/insert_ceps/")
async def insert_ceps(cep: str = Query(default=None), cidade: str = Query(default=None), estado: str = Query(default=None)):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    sql = f"BEGIN;INSERT INTO cep (cep, cidade, estado) VALUES ('{cep}', '{cidade}', '{estado}');COMMIT;"
    print(sql)
    cursor.execute(sql)
    cursor.close()
    con.close()

@app.get("/insert_lista/")
async def insert_lista(nome: str = Query(default=None),id: int = Query(default=None)):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    sql = f"BEGIN;INSERT INTO lista (nome,cod_produto) VALUES ('{nome}',{id});COMMIT;"
    cursor.execute(sql)
    cursor.close()
    con.close()


@app.get("/insert_produto_no_carrinho/")
async def insert_produto_no_carrinho(codigo_produto: int = Query(default=None),usuario: str = Query(default=None),quantidade: int = Query(default=None)):
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



@app.get("/insert_produto_no_carrinho/")
async def insert_venda(endereco: str = Query(default=None), frete: float = Query(default=None),usuario: int = Query(default=None)):
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

@app.get("/")
def home():
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    cursor.execute(f"""
        select distinct nome from lista;"""
    )
    retorno = cursor.fetchall()
    cursor.close()
    con.close()
    return retorno

@app.get("/l/{lista}")
async def lista(lista: str = Query(default=None)):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    cursor.execute(f"""
        select preco, imagemUrl, descricao from produto 
        join
        (select distinct cod_produto from lista where nome = '{lista}') as prod
        on prod.cod_produto = produto.idProd
        ;"""
    )
    retorno = cursor.fetchall()
    cursor.close()
    con.close()
    return retorno


@app.get("/p/{produto}")
async def produto(produto: str = Query(default=None)):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    cursor.execute(f"""
        select preco, imagemUrl, descricao from produto 
        where {produto} = produto.idProd
        ;"""
    )
    retorno = cursor.fetchall()
    cursor.close()
    con.close()
    return retorno

@app.get("/carrinho/{user}")
async def carrinho(user: str = Query(default=None)):
    con = mysql.connector.connect(host='localhost',database='ecommerce',user='admin',password='admin')
    cursor = con.cursor()
    cursor.execute(f"""
        select imagemUrl from produto_no_carrinho
                join produto
                on produto_no_carrinho.cod_produto = produto.idProd
                and produto_no_carrinho.cod_carrinho = (select cod_carrinho from usuarios where id = {user})
        ;"""
    )
    retorno = cursor.fetchall()
    cursor.close()
    con.close()
    return retorno