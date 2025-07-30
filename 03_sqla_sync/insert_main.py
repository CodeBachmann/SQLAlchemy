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


def insert_aditivo_nutritivo() -> None:
    print('Cadastrando Aditivo Nutritivo')

    nome: str = input("Informe o nome do Aditivo Nutritivo: ")
    formula_quimica: str = input("Informe a formula química do Aditivo Nutritivo: ")

    an: AditivoNutritivo = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

    with create_session() as session:
        session.add(an)

        session.commit()

    print("Aditivo Nutritivo Cadastrado Com Sucesso!!!")
    print(f"ID: {an.id}\nData: {an.data_criacao}\nNome: {an.nome}\nFormula Quimica {an.formula_quimica}")

def insert_sabor() -> None:
    print('Cadastrando Sabor')

    nome: str = input("Informe o nome do Sabor: ")

    sabor: Sabor = Sabor(nome=nome)

    with create_session() as session:
        session.add(sabor)

        session.commit()

    print("Sabor Cadastrado Com Sucesso!!!")
    print(f"ID: {sabor.id}\nData: {sabor.data_criacao}\nNome: {sabor.nome}")

def insert_conservante() -> None:
    print('Cadastrando conservante')

    nome: str = input("Informe o nome do Conservante: ")

    conservante: Conservante = Conservante(nome=nome)

    with create_session() as session:
        session.add(conservante)

        session.commit()

    print("Conservante Cadastrado Com Sucesso!!!")
    print(f"ID: {conservante.id}\nData: {conservante.data_criacao}\nNome: {conservante.nome}")

def insert_ingrediente() -> None:
    print("Cadastrando Ingrediente")

    nome: str = input("Informe o nome do Ingrediente: ")

    ingrediente: Ingrediente = Ingrediente(nome=nome)

    with create_session() as session:
        session.add(ingrediente)
        
        session.commit()

def insert_tipo_picole() -> None:

    print('Inserindo Tipo de Picole')

    nome: str = input("Informe o nome do Tipo de Picole: ")

    tipo_picole: TipoPicole = TipoPicole(nome=nome)

    with create_session() as session:
        session.add(tipo_picole)

        session.commit()

def insert_tipo_embalagem():

    print('Inserindo Tipo de Embalagem')

    nome: str = input("Informe o Tipo de Embalagem: ")
    tipo_embalagem: TipoEmbalagem = TipoEmbalagem(nome=nome)

    with create_session() as session:
        session.add(tipo_embalagem)

        session.commit()

def insert_revendedor():

    print('Inserindo Revendedor: ')

    cnpj: str = input("Informe o cnpj")
    razao_social: str = input("Informe a razao social")
    contato: str = input("Informe o contato: ")


    revendedor: Revendedor = Revendedor(cnpj = cnpj, razao_social=razao_social, contato=contato)

def insert_lote() -> Lote:

    print("Inserindo Lote")

    id_tipo_picole: int = input("Informe o ID do Tipo do Picole: ")
    quantidade: int = input("Informe a Quantidade do Lote: ")

    lote: Lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:

        session.add(lote)
        session.commit()

    return Lote

if __name__ == "__main__":
    insert_tipo_picole()
    insert_lote()