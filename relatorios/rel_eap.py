from classes.cl_cliente import *
from classes.cl_eap import *
import pandas as pd
from functions.functions import data_pt


def lista_eap():
    cnx = con()
    with cnx.cursor() as c:
        c.execute("SELECT * FROM cl_eap")
        return c.fetchall()


def relatorio_eap():
    relatorio = []
    clientes = lista_clientes()
    dados_eap = lista_eap()
    for cl in clientes:
        dados = [
            cl['graduacao_txt'],
            f"{cl['re']}-{cl['dc']}",
            cl['nome'],
            '',
            '',
            ''
        ]
        for eap in dados_eap:
            if cl['re'] == eap['re']:
                dados = [
                    cl['graduacao_txt'],
                    f"{cl['re']}-{cl['dc']}",
                    cl['nome'],
                    eap['periodo_ead'],
                    data_pt(eap['data_eap']),
                    data_pt(eap['send_mail']),
                    ]
        relatorio.append(dados)

    df = pd.DataFrame(columns=['Graduação', 'RE', 'Nome', 'Periodo', 'Data EAP', 'E-mail (aviso)'],
                      data=relatorio)

    return df
