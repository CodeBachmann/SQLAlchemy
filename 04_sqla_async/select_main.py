from conf.db_session import create_session
from typing import List
from sqlalchemy import func, select

# Help
from conf.help import print_objeto

# Select Simples
from models.revendedor import Revendedor
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
import asyncio

# Select Complexo

from models.picole import Picole

async def select_todos_aditivos_nutritivos() -> None:
    async with create_session() as session:
        result = await session.execute(select(AditivoNutritivo))
        aditivos_nutritivos: List[AditivoNutritivo] = result.scalars().all()

        for an in aditivos_nutritivos:
            print_objeto(an, id=True, data_criacao=False)

async def select_com_filter_todos_sabores(id_sabor) -> None:
    async with create_session() as session:
        result = await session.execute(select((Sabor)).filter(Sabor.id == id_sabor)) #.one_or_none() // .one()
        sabor: Sabor = result.scalars().first()
    
    print_objeto(sabor, True, True)

async def select_complexo_picole() -> None:
    async with create_session() as session:
        result = await session.execute(select(Picole))
        picole: List[Picole] = result.scalars().unique()

        for pc in picole:
            print_objeto(pc, True, True)

async def select_complexo_picole_order_by() -> None:
    async with create_session() as session:
        result = await session.execute(select(Picole).order_by(Picole.data_criacao.desc(), Picole.id.desc()))
        picole: List[Picole] = result.scalars().unique().all()
    
    for pc in picole:
        print_objeto(pc, True, True)


async def select_picole_sabor() -> None:
    async with create_session() as session:
        result = await session.execute(select(Picole).group_by(Picole.id, Picole.id_tipo_picole))
        picoles: List[Picole] = result.scalars().unique().all()
        for picole in picoles:
            print_objeto(picole, True, True)  # prints both Picole and its Sabor

async def conta_tipo_embalagem() -> None:
    async with create_session() as session:
        conta_tipo_embalagem = await session.execute(select(TipoEmbalagem))
        result = len(conta_tipo_embalagem.all()) 
        
        print(result)

async def func_picoles() -> None:
    async with create_session() as session:
        resultado: List = await session.execute(select(
            func.sum(Picole.preco).label("Soma"),
            func.min(Picole.preco).label("Minimo"),
            func.max(Picole.preco).label("Maximo"),
            func.avg(Picole.preco).label("Media")
        ))
        soma, minimo, maximo, media = resultado.one()
        
        print(f"Soma: {soma}")
        print(f"Mínimo: {minimo}")
        print(f"Máximo: {maximo}")
        print(f"Média: {media}")


async def select_filter_picole(id_picole: int) -> None:
    async with create_session() as session:

        result = session.execute(select(Picole).filter(Picole.id == id_picole))
        picole: Picole = result.scalars().one_or_none()

        if picole:
            print_objeto(picole)
        else:
            print("Picole não encontrado!")

async def select_filter_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:

        result = await session.execute(select(Revendedor).filter(Revendedor.id == id_revendedor))
        revendedor: Revendedor = result.scalars().one_or_none()

        if revendedor:
            print_objeto(revendedor)
        else:
            print("Revendedor não encontrado!")

if __name__ == "__main__":
    
    # asyncio.run(select_todos_aditivos_nutritivos())

    # asyncio.run(select_com_filter_todos_sabores(1))

    asyncio.run(select_complexo_picole())

    # asyncio.run(select_complexo_picole_order_by())

    # asyncio.run(select_picole_sabor())

    # asyncio.run(conta_tipo_embalagem())

    # asyncio.run(func_picoles())

    # asyncio.run(select_filter_revendedor(1))