from classes.cl_cliente import *
from data_base.data_base import Con
import pandas as pd


class Contato(Cliente):
    def __init__(self):
        super(Contato, self).__init__()
        self.id_contato = None
        self.tipo = None
        self.contato = None

    def insert_contato(self):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"INSERT INTO cl_contatos (re, tipo, contato) "
                      f"VALUES ('{self.re}', '{self.tipo}', '{self.contato}')")
            cnx.commit()


def delete_contato(contato):
    cnx = Con().con()
    with cnx.cursor() as c:
        try:
            c.execute(f"DELETE FROM cl_contatos WHERE contato = '{contato}'")
            cnx.commit()
        except SystemError:
            print('erro')


def lista_contatos(re):
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM cl_contatos WHERE re = '{re}' ORDER BY tipo")
        return c.fetchall()


def retorna_contatos():
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM cl_contatos ORDER BY tipo, contato DESC")
        return c.fetchall()


def get_email_funcional(re):
    cnx = Con().con()
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


"""
li = telefones()
li = li.values.tolist()
print(li)
"""


"""
lista = [
['130611','1-Telefone','15-99721-8453'],
['991943','1-Telefone','15-99858-6028'],
['105935','1-Telefone','15-99724-2003'],
['133251','1-Telefone','15-98116-7368'],
['136250','1-Telefone','15-99700-3788'],
['120667','1-Telefone','15-99122-0815'],
['134910','1-Telefone','15-98100-0722'],
['120590','1-Telefone','15-99123-1264'],
['130585','1-Telefone','11-97355-2670'],
['128982','1-Telefone','15-99603-4500'],
['138614','1-Telefone','15-99845-4094'],
['129730','1-Telefone','15-98803-5667'],
['129143','1-Telefone','14-99655-5031'],
['131495','1-Telefone','15-98823-8977'],
['152244','1-Telefone','15-97402-4554'],
['133117','1-Telefone','15-99607-9788'],
['136821','1-Telefone','15-98126-2771'],
['138744','1-Telefone','15-99185-0828'],
['142168','1-Telefone','15-97401-8523'],
['150634','1-Telefone','15-99837-5886'],
['153584','1-Telefone','11-97688-7814'],
['153899','1-Telefone','11-95972-0154'],
['154126','1-Telefone','15-99614-7911'],
['160172','1-Telefone','15-99164-9815'],
['161685','1-Telefone','15-99602-8861'],
['170806','1-Telefone','15-99706-8000'],
['171809','1-Telefone','15-99781-3871'],
['180399','1-Telefone','15-98132-4422'],
['191685','1-Telefone','15-99668-1160']

]

for i in lista:
    cont = Contato()
    cont.re = i[0]
    cont.tipo = i[1]
    cont.contato = i[2]
    cont.insert_contato()
"""