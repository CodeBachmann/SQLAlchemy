from conf.db_session import create_session
from models.picole import Picole
from models.sabor import Sabor
from select_main import select_filter_picole, select_filter_revendedor
from models.revendedor import Revendedor
from typing import Optional
from sqlalchemy import select
from conf.help import print_objeto
import asyncio

async def deletar_picole(id_picole: int) -> None:
    async with create_session() as session:

        picole: Picole = await session.execute(select(Picole).where(Picole.id == id_picole))
        picole: Picole = picole.unique().scalar_one_or_none()


        if picole:
            await session.delete(picole)
            print_objeto(picole)
            await session.commit()
        else:
            print("Picole não encontrado!")

async def deletar_revendedor(id_revendedor: int) -> None:
    async with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            session.delete(revendedor)
            
            session.commit()


if __name__ == "__main__":
    pass
    # select_filter_picole(21)
    asyncio.run(deletar_picole(21))
    # select_filter_picole(21)

