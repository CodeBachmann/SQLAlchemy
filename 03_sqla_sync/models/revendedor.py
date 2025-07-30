import sqlalchemy as sa

from datetime import datetime as dt
from models.model_base import ModelBase
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Revendedor(ModelBase):
    __tablename__ = "revendedores"

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[dt] = mapped_column(sa.DateTime, default=dt.now, index=True)
    cnpj: Mapped[str] = mapped_column(sa.String(45), unique=True, nullable=False)
    razao_social: Mapped[str] = mapped_column(sa.String(100), unique=True, nullable=False)
    contato: Mapped[str] = mapped_column(sa.String(100), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<REVENDEDOR: {self.cnpj}>'