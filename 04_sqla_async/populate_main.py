import asyncio
import random
from sqlalchemy import select

from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.tipo_picole import TipoPicole
from models.tipo_embalagem import TipoEmbalagem
from models.revendedor import Revendedor
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole
from conf import help


# === FUNÇÕES DE POPULAÇÃO === #

async def popular_aditivo_nutritivo():
    an = AditivoNutritivo(
        nome=help.gerar_string(10),
        formula_quimica=help.gerar_string(15)
    )
    async with create_session() as session:
        session.add(an)
        await session.commit()


async def popular_sabor():
    sabor = Sabor(nome=help.gerar_string(8))
    async with create_session() as session:
        session.add(sabor)
        await session.commit()


async def popular_conservante():
    c = Conservante(nome=help.gerar_string(9))
    async with create_session() as session:
        session.add(c)
        await session.commit()


async def popular_ingrediente():
    ing = Ingrediente(nome=help.gerar_string(7))
    async with create_session() as session:
        session.add(ing)
        await session.commit()


async def popular_tipo_picole():
    tp = TipoPicole(nome=help.gerar_string(6))
    async with create_session() as session:
        session.add(tp)
        await session.commit()


async def popular_tipo_embalagem():
    te = TipoEmbalagem(nome=help.gerar_string(6))
    async with create_session() as session:
        session.add(te)
        await session.commit()


async def popular_revendedor():
    rev = Revendedor(
        cnpj=str(help.gerar_int(10000000000000, 99999999999999)),
        razao_social=help.gerar_string(12),
        contato=str(help.gerar_int(1000000000, 9999999999))
    )
    async with create_session() as session:
        session.add(rev)
        await session.commit()


async def popular_lote():
    async with create_session() as session:
        result = await session.execute(select(TipoPicole))
        tipos = result.scalars().all()
        if not tipos:
            return
        tipo_escolhido = random.choice(tipos)
        lote = Lote(
            id_tipo_picole=tipo_escolhido.id,
            quantidade=help.gerar_int(10, 200)
        )
        session.add(lote)
        await session.commit()


async def popular_nota_fiscal():
    async with create_session() as session:
        # Revendedor
        result = await session.execute(select(Revendedor))
        revendedores = result.scalars().all()
        if not revendedores:
            return
        revendedor = random.choice(revendedores)

        nf = NotaFiscal(
            data=help.gerar_data(),
            numero_serie=help.gerar_string(10),
            valor=help.gerar_float(10.0, 1000.0),
            descricao=help.gerar_string(20),
            id_revendedor=revendedor.id
        )

        # Lotes vinculados
        result_tipos = await session.execute(select(TipoPicole))
        tipos = result_tipos.scalars().all()
        if not tipos:
            return

        for _ in range(2):
            tipo = random.choice(tipos)
            lote = Lote(
                id_tipo_picole=tipo.id,
                quantidade=help.gerar_int(20, 500)
            )
            nf.lotes.append(lote)

        session.add(nf)
        await session.commit()


async def popular_picole():
    async with create_session() as session:
        tipos = (await session.execute(select(TipoPicole))).scalars().all()
        sabores = (await session.execute(select(Sabor))).scalars().all()
        embalagens = (await session.execute(select(TipoEmbalagem))).scalars().all()
        ingredientes = (await session.execute(select(Ingrediente))).scalars().all()
        aditivos = (await session.execute(select(AditivoNutritivo))).scalars().all()
        conservantes = (await session.execute(select(Conservante))).scalars().all()

        if not all([tipos, sabores, embalagens, ingredientes, aditivos, conservantes]):
            return

        picole = Picole(
            preco=help.gerar_float(1.5, 10.0),
            id_tipo_picole=random.choice(tipos).id,
            id_sabor=random.choice(sabores).id,
            id_tipo_embalagem=random.choice(embalagens).id,
        )

        picole.ingredientes.extend(random.sample(ingredientes, 2))
        picole.aditivos_nutritivos.append(random.choice(aditivos))
        picole.conservantes.append(random.choice(conservantes))

        session.add(picole)
        await session.commit()


# === FUNÇÃO PRINCIPAL === #

async def main():
    print("Populando dados automaticamente...\n")
    for _ in range(100):
        await popular_aditivo_nutritivo()
        await popular_sabor()
        await popular_conservante()
        await popular_ingrediente()
        await popular_tipo_picole()
        await popular_tipo_embalagem()
        await popular_revendedor()
        await popular_lote()
        await popular_nota_fiscal()
        await popular_picole()
    print("✅ Banco populado com sucesso.")


# === EXECUÇÃO === #

if __name__ == "__main__":
    asyncio.run(main())
