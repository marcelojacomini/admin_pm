from classes.bh_banco_horas import *
import pandas as pd


def relatorio_saldo_bh():
    relatorio = []
    clientes = lista_clientes()
    for cl in clientes:
        saldo_cl = SaldoHoras()
        saldo_cl.set_cliente_saldo(cl['re'])
        dados = [
            cl['graduacao_txt'],
            f"{cl['re']}-{cl['dc']}",
            cl['tarja'],
            saldo_cl.saldo
        ]
        relatorio.append(dados)

    df = pd.DataFrame(columns=['Graduação', 'RE', 'Nome', 'Saldo'],
                      data=relatorio)

    return df
