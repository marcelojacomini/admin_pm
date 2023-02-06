from data_base.data_base import Con
from datetime import datetime


class Ait:
    def __init__(self):
        self.id_ait = None
        self.numero = None
        self.placa = None
        self.condutor = None
        self.local = None
        self.dia = None
        self.hora = None
        self.re = None
        self.codigo = None
        self.competencia = None
        self.artigo = None
        self.crr = None
        self.remocao = None
        self.cnh = None
        self.alcoolemia = None
        self.obs = None
        self.talao = None
        self.valor = None

    def set_ait(self, parametro):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM tr_ait WHERE "
                      f"(numero = '{parametro}')")
            ait = c.fetchone()
            if ait:
                self.id_ait = ait['id_ait']
                self.numero = ait['numero']
                self.placa = ait['placa']
                self.condutor = ait['condutor']
                self.local = ait['local']
                self.dia = ait['dia']
                self.hora = ait['hora']
                self.re = ait['re']
                self.codigo = ait['codigo']
                self.competencia = ait['competencia']
                self.artigo = ait['artigo']
                self.crr = ait['crr']
                self.remocao = ait['remocao']
                self.cnh = ait['cnh']
                self.alcoolemia = ait['alcoolemia']
                self.obs = ait['obs']
                self.talao = ait['talao']
                self.valor = ait['valor']
                return self
            else:
                return False

    def update_ait(self):
        cnx = Con().con()
        try:
            with cnx.cursor() as c:
                c.execute(
                    f"UPDATE tr_ait SET ("
                    f"numero = {self.numero}, "
                    f"placa = {self.placa}, "
                    f"condutor = {self.condutor}, "
                    f"local = {self.local}, "
                    f"dia = {self.dia}, "
                    f"hora = {self.hora}, "
                    f"re = {self.re}, "
                    f"codigo = {self.codigo}, "
                    f"competencia = {self.competencia}, "
                    f"artigo = {self.artigo}, "
                    f"crr = {self.crr}, "
                    f"remocao = {self.remocao}, "
                    f"cnh = {self.cnh}, "
                    f"alcoolemia = {self.alcoolemia}, "
                    f"obs = {self.obs}, "
                    f"talao = {self.talao}, "
                    f"valor = {self.valor} WHERE id_ait = {self.id_ait})")
                cnx.commit()
                return True
        except:
            return False


def insert_ait(a):
    cnx = Con().con()
    try:
        with cnx.cursor() as c:
            c.execute(f"INSERT INTO tr_ait (numero, placa, condutor, local, dia, hora, re, codigo, competencia, artigo, "
                      f"crr, remocao, cnh, alcoolemia, obs, talao, valor) VALUES ("
                      f"'{a[0]}' ,"
                      f"'{a[1]}' ,"
                      f"'{a[2]}' ,"
                      f"'{a[3]}' ,"
                      f"'{a[4]}' ,"
                      f"'{a[5]}' ,"
                      f"'{a[6]}' ,"
                      f"{a[7]} ,"
                      f"'{a[8]}' ,"
                      f"'{a[9]}' ,"
                      f"'{a[10]}' ,"
                      f"'{a[11]}' ,"
                      f"'{a[12]}' ,"
                      f"'{a[13]}' ,"
                      f"'{a[14]}' ,"
                      f"'{a[15]}' ,"
                      f"{a[16]}"
                      f")")
            cnx.commit()
            return True
    except:
        return False


def lista_ait_padrao():
    hoje = datetime.now()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    de = f"{ano}-{mes}-01"
    ate = f"{ano}-{mes}-{dia}"
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM tr_ait WHERE (dia >= '{de}') AND (dia <= '{ate}') ORDER BY dia DESC")
        return c.fetchall()


def lista_ait_fitros(seletor, dia_de, dia_ate):
    cnx = Con().con()
    with cnx.cursor() as c:
        if seletor == "Todos":
            c.execute(f"SELECT * FROM tr_ait WHERE (dia >= '{dia_de}') AND (dia <= '{dia_ate}') ORDER BY dia DESC")
            return c.fetchall()
        else:
            c.execute(f"SELECT * FROM tr_ait WHERE "
                      f"(talao = '{seletor}') AND "
                      f"(dia >= '{dia_de}') AND "
                      f"(dia <= '{dia_ate}') "
                      f"ORDER BY dia DESC")
            return c.fetchall()


def lista_ait_texto(texto):
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM tr_ait WHERE "
                  f"(numero LIKE '{texto}%') OR "
                  f"(placa LIKE '{texto}%') OR "
                  f"(condutor LIKE '{texto}%') OR "
                  f"(local LIKE '{texto}%') OR "
                  f"(re LIKE '{texto}%') OR "
                  f"(codigo LIKE '{texto}%') "
                  f"ORDER BY dia DESC")
        return c.fetchall()
