from conf.db_session import create_session
from models.picole import Picole
from models.sabor import Sabor
from select_main import select_filter_picole, select_filter_revendedor
from models.revendedor import Revendedor
from typing import Optional

def deletar_picole(id_picole: int) -> None:
    with create_session() as session:

        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            session.delete(picole)

            session.commit()
        else:
            print("Picole não encontrado!")

def deletar_revendedor(id_revendedor: int) -> None:
    with create_session() as session:
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()

        if revendedor:
            session.delete(revendedor)
            
            session.commit()


if __name__ == "__main__":
    pass
    # select_filter_picole(21)
    # deletar_picole(21)
    # select_filter_picole(21)

