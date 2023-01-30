from classes.cl_cliente import *
from classes.cl_dados_pessoais import *
import pandas as pd
from functions.functions import data_pt, verifica_validade


def relatorio_cnh():
    relatorio = []
    clientes = lista_clientes()
    dados_cnh = lista_dados_pessoais()
    for cl in clientes:
        for cnh in dados_cnh:
            if cl['re'] == cnh['re']:
                confere_validade = verifica_validade(cnh['validade'])
                dados = [
                    cl['graduacao_txt'],
                    f"{cl['re']}-{cl['dc']}",
                    cl['nome'],
                    cnh['cnh'],
                    data_pt(cnh['validade']),
                    cnh['categoria'],
                    cnh['sat'],
                    confere_validade
                    ]
                relatorio.append(dados)

    df = pd.DataFrame(columns=['Graduação', 'RE', 'Nome', 'CNH', 'Validade', 'CAT', 'SAT', 'Situação CNH'],
                      data=relatorio)

    return df



# relatorio_cnh()
