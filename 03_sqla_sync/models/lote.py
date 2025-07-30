import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime as dt
from models.model_base import ModelBase
from models.tipo_picole import TipoPicole

class Lote(ModelBase):
    __tablename__ = "lotes"

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[dt] = mapped_column(sa.DateTime, default=dt.now, index=True)
    quantidade: Mapped[int] = mapped_column(sa.Integer, nullable=False)
    
    id_tipo_picole: Mapped[int] = mapped_column(sa.BigInteger, sa.ForeignKey("tipos_picole.id"), nullable=False)
    tipo_picole: Mapped["TipoPicole"] = relationship("TipoPicole", lazy="joined")

    def __repr__(self) -> str:
        return f'<LOTE: {self.id}>'
