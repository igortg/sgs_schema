from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.sql.sqltypes import SmallInteger

from sgs_schema.declarative_base import Base


class Cliente(Base):

    __tablename__ = "CLIENTE"

    id = Column(Integer, Sequence(""), primary_key=True)
    tipo = Column("tipo", SmallInteger, default=0)
    pessoa = Column("pessoa", SmallInteger, default=0)
    nome = Column("nomefantasia", String(100))
    razao_social = Column("razaosocial",  String(100))
    cnpj = Column(String(20))