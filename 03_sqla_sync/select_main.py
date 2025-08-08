from conf.db_session import create_session
from typing import List
from sqlalchemy import func

# Help
from conf.help import print_objeto

# Select Simples
from models.revendedor import Revendedor
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem

# Select Complexo

from models.picole import Picole

def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)

        for an in aditivos_nutritivos:
            print_objeto(an, id=True, data_criacao=False)

def select_com_filter_todos_sabores(id_sabor) -> None:
    with create_session() as session:
        sabor: List[Sabor] = session.query(Sabor).filter(Sabor.id == id_sabor).first() #.one_or_none() // .one()
    
    print_objeto(sabor, True, True)

def select_complexo_picole() -> None:
    with create_session() as session:
        picole: List[Picole] = session.query(Picole)

        for pc in picole:
            print_objeto(pc, True, True)

def select_complexo_picole_order_by() -> None:
    with create_session() as session:
        picole: List[Picole] = session.query(Picole).order_by(Picole.data_criacao.desc(), Picole.id.desc()).all()
    
    for pc in picole:
        print_objeto(pc, True, True)


def select_picole_sabor() -> None:
    with create_session() as session:
        picoles = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()
        for picole in picoles:
            print_objeto(picole, True, True)  # prints both Picole and its Sabor

def conta_tipo_embalagem() -> None:
    with create_session() as session:
        conta_tipo_embalagem: int = session.query(TipoEmbalagem).count()

        print(conta_tipo_embalagem)

def func_picoles() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label("Soma"),
            func.min(Picole.preco).label("Minimo"),
            func.max(Picole.preco).label("Maximo"),
            func.avg(Picole.preco).label("Media")
        ).all()
        print(f"Soma: {resultado[0][0]}\nMinimo: {resultado[0][1]}\nMaximo: {resultado[0][2]}\nMédia: {resultado[0][3]}")

def select_filter_picole(id_picole: int) -> None:
    with create_session() as session:

        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            print_objeto(picole)
        else:
            print("Picole não encontrado!")

def select_filter_revendedor(id_revendedor: int) -> None:
    with create_session() as session:

        revendedor: Revendedor = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            print_objeto(revendedor)
        else:
            print("Revendedor não encontrado!")

if __name__ == "__main__":
    
    # select_todos_aditivos_nutritivos()

    # select_com_filter_todos_sabores(1)

    # select_complexo_picole()

    # select_complexo_picole_order_by()

    # select_picole_sabor()

    conta_tipo_embalagem()

    # func_picoles()