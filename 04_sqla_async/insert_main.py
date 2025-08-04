import asyncio
from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole
from models.revendedor import Revendedor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from datetime import datetime as dt
from conf.help import print_objeto




async def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input("Informe o nome do Aditivo Nutritivo: ")
    formula_quimica: str = input("Informe a formula química do Aditivo Nutritivo: ")

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    async with create_session() as session:
        session.add(an)
        await session.commit()
        print_objeto(an)
        return an

async def insert_sabor() -> Sabor:
    print('Cadastrando Sabor')

    nome: str = input("Informe o nome do Sabor: ")

    sabor: Sabor = Sabor(nome=nome)

    async with create_session() as session:
        session.add(sabor)
        await session.commit()
        print_objeto(sabor)
        return sabor


async def insert_conservante() -> Conservante:
    print('Cadastrando conservante')

    nome: str = input("Informe o nome do Conservante: ")

    conservante: Conservante = Conservante(nome=nome)

    async with create_session() as session:
        session.add(conservante)
        await session.commit()
        print_objeto(conservante)
        return conservante

async def insert_ingrediente() -> Ingrediente:
    print("Cadastrando Ingrediente")

    nome: str = input("Informe o nome do Ingrediente: ")

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    print_objeto(ingrediente)

    async with create_session() as session:
        session.add(ingrediente)
        await session.commit()
        print_objeto(ingrediente)
        return ingrediente

async def insert_tipo_picole() -> TipoPicole:

    print('Inserindo Tipo de Picole')

    nome: str = input("Informe o nome do Tipo de Picole: ")

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    async with create_session() as session:
        session.add(tipo_picole)
        await session.commit()
        print_objeto(tipo_picole)
        return tipo_picole

async def insert_tipo_embalagem() -> TipoEmbalagem:

    print('Inserindo Tipo de Embalagem')

    nome: str = input("Informe o Tipo de Embalagem: ")
    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    async with create_session() as session:
        session.add(tipo_embalagem)
        await session.commit()
        print_objeto(tipo_embalagem)
        return tipo_embalagem

async def insert_revendedor() -> Revendedor:

    print('Inserindo Revendedor: ')

    cnpj: str = input("Informe o cnpj: ")
    razao_social: str = input("Informe a razao social: ")
    contato: str = input("Informe o contato: ")


    revendedor: Revendedor = Revendedor(cnpj = cnpj, razao_social=razao_social, contato=contato)
    async with create_session() as session:

        session.add(revendedor)
        await session.commit()
        print_objeto(revendedor)
        return revendedor

async def insert_lote() -> Lote:

    print("Inserindo Lote")

    id_tipo_picole: int = int(input("Informe o ID do Tipo do Picole: "))
    quantidade: int = int(input("Informe a Quantidade do Lote: "))

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    async with create_session() as session:

        session.add(lote)
        await session.commit()
        print_objeto(lote)
        return lote

async def insert_nota_fiscal() -> NotaFiscal:

    print("Inserindo NF")

    data_str = input("Informe a data (dd/mm/yyyy): ")
    data: dt = dt.strptime(data_str, "%d/%m/%Y")
    numero_serie: str = input("Informe o numero Serie: ")
    valor: float = float(input("Informe o Valor da NF: "))
    descricao: str = input("Informe a descrição: ")
    id_revendedor: int = int(input("Informe o ID do Revendedor: "))

    nota_fiscal: NotaFiscal = NotaFiscal(data=data, numero_serie=numero_serie, valor=valor, descricao=descricao, id_revendedor=id_revendedor)
    lote1 = await insert_lote()
    nota_fiscal.lotes.append(lote1)

    lote2 = await insert_lote()
    nota_fiscal.lotes.append(lote2)

    async with create_session() as session:

        session.add(nota_fiscal)
        await session.commit()
        print_objeto(nota_fiscal)
        return nota_fiscal

async def insert_picole() -> Picole:

    print('Inserindo Picole')

    preco: float = float(input("Informe o preço do picole: "))
    id_tipo_picole: int = int(input("Informe o ID do Tipo do Picole: "))
    id_tipo_embalagem: int = int(input("Informe o ID do Tipo de Embalagem: "))
    id_sabor: int = int(input("Informe o ID do Sabor"))
    picole: Picole = Picole(preco=preco, id_tipo_picole=id_tipo_picole, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem)
    
    ingrediente1 = await insert_ingrediente()
    picole.ingredientes.append(ingrediente1)

    ingrediente2 = await insert_ingrediente()
    picole.ingredientes.append(ingrediente2)

    an1 = await insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(an1)

    conservante1 = await insert_conservante()
    picole.conservantes.append(conservante1)

    async with create_session() as session:
        session.add(picole)
        await session.commit()
        print_objeto(picole)
        return picole



if __name__ == "__main__":

    # # 1 - Insert Aditivo Nutritivo
    # asyncio.run(insert_aditivo_nutritivo())

    # # 2 - Insert Sabor
    # asyncio.run(insert_sabor())

    # # 3 - Insert Revendedor
    # asyncio.run(insert_revendedor())
    
    # # 4 - Insert Ingrediente
    # asyncio.run(insert_ingrediente())
    
    # # 5 - Insert Tipo Embalagem
    # asyncio.run(insert_tipo_embalagem())

    # # 6 - Insert Tipo Picole
    # asyncio.run(insert_tipo_picole())

    # # 7 - Insert Conservante
    # asyncio.run(insert_conservante())

    # # 8 - Insert Lote
    # asyncio.run(insert_lote())

    # # 9 - Insert Nota Fiscal
    # asyncio.run(insert_nota_fiscal())

    # # 10 - Insert Picole
    asyncio.run(insert_picole())