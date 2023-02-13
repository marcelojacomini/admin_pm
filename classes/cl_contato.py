from classes.cl_cliente import *
from data_base.data_base import con
import pandas as pd


class Contato(Cliente):
    def __init__(self):
        super(Contato, self).__init__()
        self.id_contato = None
        self.tipo = None
        self.contato = None

    def insert_contato(self):
        cnx = con()
        with cnx.cursor() as c:
            c.execute(f"INSERT INTO cl_contatos (re, tipo, contato) "
                      f"VALUES ('{self.re}', '{self.tipo}', '{self.contato}')")
            cnx.commit()


def delete_contato(contato):
    cnx = con()
    with cnx.cursor() as c:
        try:
            c.execute(f"DELETE FROM cl_contatos WHERE contato = '{contato}'")
            cnx.commit()
        except SystemError:
            print('erro')


def lista_contatos(re):
    cnx = con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM cl_contatos WHERE re = '{re}' ORDER BY tipo")
        return c.fetchall()


def retorna_contatos():
    cnx = con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM cl_contatos ORDER BY tipo, contato DESC")
        return c.fetchall()


def get_email_funcional(re):
    cnx = con()
    with cnx.cursor() as c:
        c.execute(f"SELECT contato FROM cl_contatos WHERE re = '{re}' AND tipo = '2-e-mail funcional'")
        return c.fetchone()


def telefones():
    ctt = retorna_contatos()
    cli = lista_clientes()
    lista = []
    df = pd.DataFrame(data={'Graduação': [], 'RE': [], 'Nome': [], 'Telefone 1': [], 'Telefone 2': [], '...': []})
    for cl in cli:
        dados = Cliente().dados_para_lista(cl['re'])
        for ct in ctt:
            if ct['re'] == cl['re']:
                if ct['tipo'] == '1-Telefone':
                    if len(dados) < 5:
                        dados.append(ct['contato'])
                    elif len(dados) == 5:
                        dados.append("Mais...")
        lista.append(dados)
    for i in lista:
        if len(i) == 3:
            i.append("__")
            i.append("__")
            i.append('...')
        if len(i) == 4:
            i.append("__")
            i.append('...')
        if len(i) == 5:
            i.append("...")
        df2 = pd.DataFrame({'Graduação': [i[0]], 'RE': [i[1]], 'Nome': [i[2]],
                            'Telefone 1': [i[3]], 'Telefone 2': [i[4]], '...': [i[5]]})
        df = pd.concat([df, df2], ignore_index=True)

    return df


def e_mails():
    ctt = retorna_contatos()
    cli = lista_clientes()
    lista = []
    df = pd.DataFrame(data={'Graduação': [], 'RE': [], 'Nome': [], 'Mail_1': [], 'Mail_2': [], '...': []})
    for cl in cli:
        dados = Cliente().dados_para_lista(cl['re'])
        for ct in ctt:
            if ct['re'] == cl['re']:
                if ct['tipo'] == '2-e-mail funcional' or ct['tipo'] == '3-e-mail pessoal':
                    if len(dados) < 5:
                        dados.append(ct['contato'])
                    elif len(dados) == 5:
                        dados.append("Mais...")
        lista.append(dados)
    for i in lista:
        if len(i) == 3:
            i.append("__")
            i.append("__")
            i.append('...')
        if len(i) == 4:
            i.append("__")
            i.append('...')
        if len(i) == 5:
            i.append('...')
        df2 = pd.DataFrame({'Graduação': [i[0]], 'RE': [i[1]], 'Nome': [i[2]],
                            'Mail_1': [i[3]], 'Mail_2': [i[4]], '...': [i[5]]})
        df = pd.concat([df, df2], ignore_index=True)
    return df
