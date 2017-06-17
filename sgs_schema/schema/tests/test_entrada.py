from datetime import date, datetime

from sgs_schema.schema.entradaprodutos import EntradaProduto


def test_entrada_produtos(db_session):
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

    rentrada = db_session.query(EntradaProduto).filter(entrada.id == 1).first()
    assert rentrada.id_empresa == 1
    assert rentrada.data == date(2017, 6, 17)
    assert rentrada.tipo == 2
    assert rentrada.status == 0
    assert rentrada.numero == 1
    assert rentrada.historico == entrada.historico
    assert rentrada.createat == datetime(2017, 6, 17, 11, 00)