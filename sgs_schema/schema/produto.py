from sqlalchemy import Column, Integer, String, Sequence, SmallInteger
from sgs_schema.declarative_base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Float


class Produto(Base):

    __tablename__ = "PRODUTO"

    id = Column(Integer, Sequence("PRODUTO_ID_GEN"), primary_key=True)
    codigo = Column(String(20))
    codbarra = Column(String(50))
    descricao = Column(String(250))
    id_categoria = Column(Integer, ForeignKey("CATPRODUTO.id"), nullable=False)
    categoria = relationship("CategoriaProduto")
    id_unidade = Column(Integer)
    #TODO: unity = relationship("ItemUnity")
    custo = Column(Float)
    precovenda = Column(Float, default=0)
    precovenda2 = Column(Float, default=0)
    precovenda3 = Column(Float, default=0)
    id_unidade_venda = Column(Float)
    #TODO: unity_sell = relationship("ItemUnity")
    vende_sem_estoque = Column(Integer, default=0)
    #TODO: balanca = None
    fator_un_venda = Column(Integer, default=1)
    marca = Column(String(50))
    para_revenda = Column(SmallInteger)
    id_moeda = Column(Integer, default=1)
    inativo = Column(Integer, default=0)



class CategoriaProduto(Base):

    __tablename__ = "CATPRODUTO"

    id = Column(Integer, Sequence('id_manager'), primary_key=True)
    descricao = Column(String(50))
    tem_aprovacao = Column(Integer, default=0)