import sqlalchemy as sa
from datetime import datetime as dt
from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

# Tabela de associação entre notas fiscais e lotes
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id'), primary_key=True),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'), primary_key=True)
)

class NotaFiscal(ModelBase):
    __tablename__ = "notas_fiscais"

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[dt] = mapped_column(sa.DateTime, default=dt.now, index=True)
    
    data: Mapped[dt] = mapped_column(sa.DATE, index=True)
    valor: Mapped[int] = mapped_column(sa.DECIMAL(8,2), nullable=False)
    numero_serie: Mapped[str] = mapped_column(sa.String(45), nullable=False)
    descricao: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    
    id_revendedor: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey('revendedores.id', ondelete="CASCADE"))
    revendedor: Mapped["Revendedor"] = relationship('Revendedor', lazy='joined', cascade="delete")

    # Relacionamento muitos-para-muitos com a tabela de associação
    lotes: Mapped[List["Lote"]] = relationship(
        'Lote',
        secondary=lotes_nota_fiscal,
        backref='notas_fiscais'
    )

    def __repr__(self) -> str:
        return f'<NOTA_FISCAL: {self.id}>'
