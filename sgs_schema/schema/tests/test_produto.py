from sgs_schema.schema.produto import Produto, CategoriaProduto


def test_produto(db_session):
    categoria = CategoriaProduto()
    categoria.description = "Anel"
    db_session.add(categoria)
    db_session.commit()

    product = Produto()
    product.descricao = u"Anel Criança"
    product.codbarra = "ACN00200"
    product.categoria = categoria
    db_session.add(product)
    db_session.commit()

    read_product = db_session.query(Produto).filter(Produto.codbarra == "ACN00200").first()
    assert read_product.descricao == u"Anel Criança"
    assert read_product.codbarra == u"ACN00200"
    assert read_product.categoria.descricao == categoria.descricao
