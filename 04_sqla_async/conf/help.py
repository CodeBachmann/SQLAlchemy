import random
import string
from datetime import datetime as dt, timedelta

# Retorna uma string aleatória
def gerar_string(tamanho=8):
    return ''.join(random.choices(string.ascii_letters, k=tamanho))

# Retorna um inteiro aleatório entre dois valores
def gerar_int(min_val=0, max_val=100):
    return random.randint(min_val, max_val)

# Retorna um float aleatório entre dois valores
def gerar_float(min_val=0.0, max_val=100.0, precisao=2):
    valor = random.uniform(min_val, max_val)
    return round(valor, precisao)

# Retorna uma data aleatória entre duas datas
def gerar_data(inicio="2000-01-01", fim="2030-12-31"):
    data_inicio = dt.strptime(inicio, "%Y-%m-%d")
    data_fim = dt.strptime(fim, "%Y-%m-%d")
    intervalo = data_fim - data_inicio
    dias_aleatorios = random.randint(0, intervalo.days)
    return data_inicio + timedelta(days=dias_aleatorios)

# Retorna uma cor aleatória em formato hexadecimal
def gerar_cor():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def print_objeto(obj, id=False, data_criacao=False):
    print("=== // ===")


    ignorar = { "metadata", "registry", "_sa_instance_state"}
    if not id:
        ignorar.add('id')

    if not data_criacao:
        ignorar.add('data_criacao')

    nome_classe = obj.__class__.__name__.lower()

    for attr, valor in obj.__dict__.items():
        if attr in ignorar or attr.lower() == nome_classe:
            continue

        if isinstance(valor, dt):
            valor = valor.strftime("%d/%m/%Y %H:%M:%S")

        nome_formatado = attr.replace("_", " ").capitalize()
        print(f"{nome_formatado}: {valor}")