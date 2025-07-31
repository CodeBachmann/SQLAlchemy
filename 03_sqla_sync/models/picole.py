import sqlalchemy as sa
from sqlalchemy import orm

from datetime import datetime as dt

from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.model_base import ModelBase

from models.tipo_picole import TipoPicole
from models.tipo_embalagem import TipoEmbalagem
from models.sabor import Sabor
from models.ingrediente import Ingrediente
from models.aditivo_nutritivo import AditivoNutritivo
from models.conservante import Conservante

from typing import List, Optional

picoles_ingredientes = sa.Table(
    'ingredientes_picoles',
    ModelBase.metadata,
    sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey('ingredientes.id')),
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id'))
)

picoles_aditivos_nutritivos = sa.Table(
    'picoles_aditivos_nutritivos',
    ModelBase.metadata,
    sa.Column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey('aditivos_nutritivos.id')),
    sa.Column('id_picole',sa.Integer, sa.ForeignKey('picoles.id'))
)

picoles_conservantes = sa.Table(
    'picoles_conservantes',
    ModelBase.metadata,
    sa.Column('id_conservante', sa.Integer, sa.ForeignKey('conservantes.id')),
    sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id'))
)

class Picole(ModelBase):
    __tablename__ = "picoles"

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[dt] = mapped_column(sa.DateTime, default=dt.now, index=True)
    preco: Mapped[int] = mapped_column(sa.DECIMAL(8,2), nullable=False)
    
    id_tipo_picole: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_picole.id'), nullable=False)
    tipo_picole: Mapped[TipoPicole] = orm.relationship(lazy='joined')

    id_tipo_embalagem: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('tipos_embalagem.id'), nullable=False)
    tipo_embalagem: Mapped[TipoEmbalagem] = orm.relationship(lazy='joined')
    
    id_sabor: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('sabores.id'), nullable=False)
    sabor: Mapped[Sabor] = orm.relationship('Sabor', lazy='joined')

    ingredientes: Mapped[List[Ingrediente]] = orm.relationship('Ingrediente', secondary=picoles_ingredientes, backref='ingrediente', lazy='joined')

    aditivos_nutritivos: Mapped[Optional[List[AditivoNutritivo]]] = orm.relationship('AditivoNutritivo', secondary=picoles_aditivos_nutritivos, backref='aditivo_nutritivo', lazy='joined')

    conservantes: Mapped[Optional[List[Conservante]]]= orm.relationship('Conservante', secondary=picoles_conservantes, backref='conservante', lazy='joined')

    def __repr__(self) -> str:
        return f'<PICOLE: {self.tipo_picole.nome} e sabor {self.sabor.nome} e preço {self.preco}>'