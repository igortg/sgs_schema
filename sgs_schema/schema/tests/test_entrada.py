from datetime import date, datetime

from sgs_schema.schema.entradaprodutos import EntradaProduto, EntradaProdutoItens
from sgs_schema.schema.produto import Produto, CategoriaProduto


def test_entrada_produto(db_session):
    entrada = EntradaProduto()
    entrada.id_empresa = 1
    entrada.data = date(2017, 6, 17)
    entrada.tipo = 2
    entrada.status = 0
    entrada.numero = 1
    entrada.historico = "Watching 24h of LeMans"
    entrada.createat = datetime(2017, 6, 17, 11, 00)

    db_session.add(entrada)
    db_session.commit()

    produtos = cria_produtos(db_session)

    entrada.produtos.append(produtos[0])
    entrada.produtos.append(produtos[1])
    EntradaProdutoItens(produtos[2], entrada, 2)
    # Testa que o association_proxy está funcionando
    assert entrada.produtos == [produtos[0], produtos[1], produtos[2]]


    db_session.add(entrada)
    db_session.commit()

    rentrada = db_session.query(EntradaProduto).filter(entrada.numero == 1).first()
    assert rentrada.id_empresa == 1
    assert rentrada.data == date(2017, 6, 17)
    assert rentrada.tipo == 2
    assert rentrada.status == 0
    assert rentrada.numero == 1
    assert rentrada.historico == entrada.historico
    assert rentrada.createat == datetime(2017, 6, 17, 11, 00)

    rproduto = rentrada.produtos[0]
    rproduto.codbarra = "00213"
    rproduto.codigo = "AN00213"


def test_entrada_produto_itens(db_session):
    produtos = cria_produtos(db_session)

    entrada_itens = EntradaProdutoItens()
    entrada_itens.produto = produtos[0]
    db_session.add(entrada_itens)
    db_session.commit()

    r_entrada_itens = db_session.query(EntradaProdutoItens).filter(EntradaProdutoItens.id == entrada_itens.id).first()
    assert r_entrada_itens.produto == entrada_itens.produto


def cria_produtos(db_session):
    categoria = CategoriaProduto()
    categoria.description = "Anel"
    db_session.add(categoria)
    db_session.commit()

    dados = [
        ("00213", "AN00213", "Anel Zirconia"),
        ("00214", "BR00214", "Brinco Pedra"),
        ("00215", "PS00215", "Pulseira Infantil"),
    ]

    produtos = [Produto(codbarra=item[0], codigo=item[1], descricao=item[2], categoria=categoria) for item in dados]
    db_session.add_all(produtos)
    db_session.commit()
    return produtos
