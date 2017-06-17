from sqlalchemy import Column, Integer, Sequence, Date, SmallInteger, String, TIMESTAMP

from sgs_schema.declarative_base import Base


class EntradaProduto(Base):
    """
    Cria uma Entrada de Produtos. Não executa movimentação no estoque (ver tabela MOVIMENTAÇÃO para estoque)
    """

    __tablename__ = "ENTRADA"

    id = Column(Integer, Sequence("ID_MANAGER"), primary_key=True)
    id_empresa = Column(Integer)
    data = Column(Date)
    tipo = Column(SmallInteger, nullable=False, default=0)
    status = Column(SmallInteger, nullable=False, default=0)
    numero = Column(Integer)
    historico = Column(String(100))
    id_colaborador = Column(Integer)
    observacao = Column(String(2000))
    id_almoxarifado = Column(Integer)
    createat = Column(TIMESTAMP)
    updateat = Column(TIMESTAMP)
    classname = Column(String(100))
    id_mov = Column(Integer)

