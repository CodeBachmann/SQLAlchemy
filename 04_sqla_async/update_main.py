from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole
from typing import List
from sqlalchemy import func, select, update
import asyncio
from conf.help import print_objeto

async def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:

    async with create_session() as session:
        # Passo 1
        resultado = await session.execute(update(Sabor).where(Sabor.id == id_sabor).values(nome = novo_nome))
        print(resultado._real_result())
        await session.commit()


async def atualizar_sabor_diferente(id_sabor: int, novo_nome: str) -> None:

    async with create_session() as session:
        # Passo 1
        query = select(Sabor).where(Sabor.id == id_sabor)
        sabor: Sabor = await session.execute(query)
        sabor: Sabor = sabor.scalar_one_or_none()
        if sabor:
            print_objeto(sabor)
            sabor.nome = novo_nome
        else:
            print("Não encontrado")
            
        await session.commit()

async def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
    async with create_session() as session:
        await session.execute(update(Picole).where(Picole.id == id_picole).values(preco = novo_preco, id_sabor = novo_sabor))

        await session.commit()

async def atualizar_picole_diferente(id_picole: int, novo_preco: float, novo_sabor: int = None):
    async with create_session() as session:
        query = select(Picole).where(Picole.id == id_picole)
        picole: Picole = await session.execute(query)
        picole: Picole = picole.unique().scalar_one_or_none()

        if picole:
            print_objeto(picole)
            picole.preco = novo_preco
            picole.id_sabor = novo_sabor
        else:
            print("Deu Ruim!")


        await session.commit()


if __name__ == "__main__":
    
    # 1 Atualizar Sabor
    #asyncio.run(atualizar_sabor(3812093, "Mornasuida"))

    # 1.1 Atualizar Sabor
    # asyncio.run(atualizar_sabor_diferente(1, "Mornasuida"))

    # 2 Atualizar Picole
    # asyncio.run(atualizar_picole(1, 5.99, 2))

    # 2.1 Atualizar Picole
    asyncio.run(atualizar_picole_diferente(2, 8.99, 2))