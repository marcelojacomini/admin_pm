from classes.cl_cliente import *


class Talao:
    def __init__(self):
        self.id_talao = None
        self.re = None
        self.mi = None
        self.mf = None
        self.ei = None
        self.ef = None

    def set_talonario(self, re):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM tr_talao WHERE "
                      f"re = '{re}'")
            cliente = c.fetchone()
            if cliente:
                self.id_talao = cliente['id_talao']
                self.re = cliente['re']
                self.mi = cliente['mi']
                self.mf = cliente['mf']
                self.ei = cliente['ei']
                self.ef = cliente['ef']
                return self
            else:
                self.id_talao = None
                self.re = re
                self.mi = 0
                self.mf = 0
                self.ei = 0
                self.ef = 0
                return self

    def insert_talao(self):
        existe = Talao().set_talonario(self.re)
        try:
            if existe.id_talao:
                cnx = Con().con()
                with cnx.cursor() as c:
                    c.execute(f"UPDATE tr_talao SET "
                              f"mi = '{self.mi}', "
                              f"mf = '{self.mf}', "
                              f"ei = '{self.ei}', "
                              f"ef = '{self.ef}' WHERE re = '{self.re}'")
                    cnx.commit()
            else:
                cnx = Con().con()
                with cnx.cursor() as c:
                    c.execute(f"INSERT INTO tr_talao (re, mi, mf, ei, ef) VALUES "
                              f"('{self.re}', '{self.mi}', '{self.mf}', '{self.ei}', '{self.ef}')")
                    cnx.commit()
            return True
        except Exception as e:
            print(e)
            return False


def talao_range(re):
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM tr_talao WHERE "
                  f"re = '{re}'")
        talonario = c.fetchone()
        if talonario:
            t_mun = range(int(talonario['mi']), int(talonario['mf']) + 1)
            t_est = range(int(talonario['ei']), int(talonario['ef']) + 1)
            return list(t_mun) + list(t_est)
        else:
            return False


def lista_talonario_geral():
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute("SELECT re FROM clientes WHERE ativo = 'ATIVO' ORDER BY graduacao, promocao, admissao, re")
        clientes = c.fetchall()

    lista_talonarios = []
    for cliente in clientes:
        taloes = Talao().set_talonario(cliente['re'])
        lista_talonarios.append([taloes.re, talao_range(taloes.re)])

    return lista_talonarios
