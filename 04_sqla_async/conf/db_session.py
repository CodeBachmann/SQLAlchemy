from pathlib import Path
from typing import Optional
import asyncio

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from models.model_base import ModelBase

__async_engine: Optional[AsyncEngine] = None

def create_engine(sqlite: bool = False) -> AsyncEngine:
    """
    Função para configurar a conexão ao banco de dados.
    """
    global __async_engine

    if __async_engine:
        return
    else:
        conn_str = "postgresql+asyncpg://postgres:123456@localhost:5432"
        __async_engine = create_async_engine(
            url=conn_str,
            echo=False
        )
        return __async_engine

def create_session() -> AsyncSession:
    """
    Função para criar a sessão de conexão ao banco de dados.
    """
    global __async_engine
    if not __async_engine:
        create_engine()

    __async_session = sessionmaker(
        __async_engine,
        expire_on_commit=False,
        class_=AsyncSession
    )

    session: AsyncSession = __async_session()

    return session

async def create_tables() -> None:
    global __async_engine

    if not __async_engine:
        create_engine()

    import models._all_models

    async with __async_engine.begin() as conn:
        await conn.run(ModelBase.metadata.drop_all)
        await conn.run(ModelBase.metadata.create_all)
