from conf.db_session import create_session
from models.sabor import Sabor
from models.picole import Picole

def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:

    with create_session() as session:
        # Passo 1
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        if sabor:
            sabor.nome = novo_nome

            session.commit()
        else:
            print("Valor não encontrado!")

def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
    with create_session() as session:
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()

        if picole:
            picole.preco = novo_preco
            if novo_sabor != None:
                picole.id_sabor = novo_sabor
        else:
            print("Picole não encontrado!")


if __name__ == "__main__":
    
    # 1 Atualizar Sabor
    # atualizar_sabor(1, "Groselha")

    # 2 Atualizar Picole
    atualizar_picole(1, 5.99, 2)