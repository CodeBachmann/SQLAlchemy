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

from conf import help  # importa gerar_string, gerar_float, gerar_data etc.

# === FUNÇÕES DE POPULAÇÃO AUTOMÁTICA === #

def popular_aditivo_nutritivo():
    an = AditivoNutritivo(
        nome=help.gerar_string(10),
        formula_quimica=help.gerar_string(15)
    )
    with create_session() as session:
        session.add(an)
        session.commit()
        print("Aditivo:", an.nome)

def popular_sabor():
    sabor = Sabor(nome=help.gerar_string(8))
    with create_session() as session:
        session.add(sabor)
        session.commit()
        print("Sabor:", sabor.nome)

def popular_conservante():
    c = Conservante(nome=help.gerar_string(9))
    with create_session() as session:
        session.add(c)
        session.commit()
        print("Conservante:", c.nome)

def popular_ingrediente():
    ing = Ingrediente(nome=help.gerar_string(7))
    with create_session() as session:
        session.add(ing)
        session.commit()
        print("Ingrediente:", ing.nome)

def popular_tipo_picole():
    tp = TipoPicole(nome=help.gerar_string(6))
    with create_session() as session:
        session.add(tp)
        session.commit()
        print("Tipo Picolé:", tp.nome)

def popular_tipo_embalagem():
    te = TipoEmbalagem(nome=help.gerar_string(6))
    with create_session() as session:
        session.add(te)
        session.commit()
        print("Tipo Embalagem:", te.nome)

def popular_revendedor():
    rev = Revendedor(
        cnpj=str(help.gerar_int(10000000000000, 99999999999999)),
        razao_social=help.gerar_string(12),
        contato=str(help.gerar_int(1000000000, 9999999999))
    )
    with create_session() as session:
        session.add(rev)
        session.commit()
        print("Revendedor:", rev.razao_social)

import random

def popular_lote():
    with create_session() as session:
        tipos = session.query(TipoPicole).all()
        if not tipos:
            print("⚠ Nenhum tipo de picolé encontrado para criar lote.")
            return

        tipo_escolhido = random.choice(tipos)
        lote = Lote(
            id_tipo_picole=tipo_escolhido.id,
            quantidade=help.gerar_int(10, 200)
        )
        session.add(lote)
        session.commit()
        print("Lote criado com ID:", lote.id)

def popular_nota_fiscal():
    with create_session() as session:
        revendedores = session.query(Revendedor).all()
        if not revendedores:
            print("⚠ Nenhum revendedor encontrado para criar nota fiscal.")
            return

        revendedor = random.choice(revendedores)

        nf = NotaFiscal(
            data=help.gerar_data(),
            numero_serie=help.gerar_string(10),
            valor=help.gerar_float(10.0, 1000.0),
            descricao=help.gerar_string(20),
            id_revendedor=revendedor.id
        )

        # Adiciona 2 lotes aleatórios
        tipos = session.query(TipoPicole).all()
        if not tipos:
            print("⚠ Nenhum tipo de picolé para associar lote.")
            return

        for _ in range(2):
            tipo = random.choice(tipos)
            lote = Lote(
                id_tipo_picole=tipo.id,
                quantidade=help.gerar_int(20, 500)
            )
            nf.lotes.append(lote)

        session.add(nf)
        session.commit()
        print("Nota Fiscal criada com ID:", nf.id)

def popular_picole():
    with create_session() as session:
        tipos = session.query(TipoPicole).all()
        sabores = session.query(Sabor).all()
        embalagens = session.query(TipoEmbalagem).all()
        ingredientes = session.query(Ingrediente).all()
        aditivos = session.query(AditivoNutritivo).all()
        conservantes = session.query(Conservante).all()

        if not all([tipos, sabores, embalagens, ingredientes, aditivos, conservantes]):
            print("⚠ Faltam registros para criar picolé. Verifique se todos os dados foram populados.")
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
        session.commit()
        print("Picolé criado com ID:", picole.id)


if __name__ == "__main__":
    print("Populando dados automaticamente usando conf.help e registros existentes...\n")
    cont = 0
    while cont < 100:
        cont += 1
        popular_aditivo_nutritivo()
        popular_sabor()
        popular_conservante()
        popular_ingrediente()
        popular_tipo_picole()
        popular_tipo_embalagem()
        popular_revendedor()
        popular_lote()
        popular_nota_fiscal()
        popular_picole()

    print("\n✅ Banco populado com sucesso.")
