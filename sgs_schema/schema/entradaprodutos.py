from datetime import datetime

from sqlalchemy import Column, Integer, Sequence, Date, SmallInteger, String, TIMESTAMP, ForeignKey, Float
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, backref

from sgs_schema.declarative_base import Base
from sgs_schema.schema.produto import Produto


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

    produtos = association_proxy("entrada_itens", "produto")

    def __init__(self, *args, **kw):
        super(EntradaProduto, self).__init__(*args, **kw)
        self.createat = datetime.now()


class EntradaProdutoItens(Base):

    __tablename__ = "ENTRADA_ITENS"

    id = Column(Integer, Sequence("ID_MANAGER"), primary_key=True)
    id_entrada = Column(Integer, ForeignKey(EntradaProduto.id))
    entrada_produto = relationship(EntradaProduto, backref=backref("entrada_itens", cascade="all, delete-orphan"))
    id_produto = Column(Integer, ForeignKey(Produto.id))
    produto = relationship(Produto)
    quantidade = Column(Float("DOUBLE PRECISION"))
    valor = Column(Float("DOUBLE PRECISION"))
    fator_unidade = Column(Float("DOUBLE PRECISION"), default=1)
    desconto = Column(Float("DOUBLE PRECISION"), default=0)
    id_valorat1 = Column(Integer, nullable=False)
    id_valorat2 = Column(Integer, nullable=False)
    createat = Column(TIMESTAMP)
    updateat = Column(TIMESTAMP)
    classname = Column(String(100))


    def __init__(self, produto=None, entrada_produto=None, quantidade=1):
        self.produto = produto
        self.entrada_produto = entrada_produto
        self.quantidade = quantidade
        self.id_valorat1 = -1
        self.id_valorat2 = -1
        self.createat = datetime.now()
