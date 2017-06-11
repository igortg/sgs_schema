import enum
from sqlalchemy import Column, Integer, String, Sequence, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import SmallInteger

from sgs_schema.declarative_base import Base
from sgs_schema.schema.cliente import Cliente
from sgs_schema.schema.produto import Produto


os_itens_table = Table("OS_ITENS", Base.metadata,
                       Column("ID_ORDEMSERVICO", Integer, ForeignKey("ORDEM_SERVICO.id")),
                       Column("ID_PRODUTO", Integer, ForeignKey("PRODUTO.id")),
                       Column("QUANTIDADE", Float),
                       )


class SituacaoFinanceira(enum.Enum):
    nao_faturado = 0
    faturado = 1
    recebido = 2


class OrdemServico(Base):

    __tablename__ = "ORDEM_SERVICO"

    id = Column(Integer, Sequence(""), primary_key=True)
    id_empresa = Column(nullable=False)
    numero = Column(Integer)
    status = Column(Integer)
    id_cliente = Column(ForeignKey(Cliente.id), nullable=False)
    cliente = relationship(Cliente)
    contrato = Column("NUMERO_CONTRATO", String(30))
    itens = relationship(Produto, secondary=os_itens_table)
    situacao_financeira = Column("SIT_RECEBIMENTO", SmallInteger)
    resumo_final = Column("RESUMO_FINAL", String(2000))
