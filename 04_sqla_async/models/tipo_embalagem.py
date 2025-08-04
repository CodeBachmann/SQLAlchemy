import sqlalchemy as sa

from datetime import datetime as dt
from models.model_base import ModelBase
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TipoEmbalagem(ModelBase):
    __tablename__ = "tipos_embalagem"

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[dt] = mapped_column(sa.DateTime, default=dt.now, index=True)
    nome: Mapped[str] = mapped_column(sa.String(45), unique=True,nullable=False)

    def __repr__(self) -> str:
        return f'<TIPO_EMBALAGEM: {self.nome}>'