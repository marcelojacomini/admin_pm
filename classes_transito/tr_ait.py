from data_base.data_base import Con


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
                      f"(id = {parametro}) OR "
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


