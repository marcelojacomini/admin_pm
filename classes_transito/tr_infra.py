# CLASSE INFRAÇÕES DE TRÂNSITO (DESCRIÇÃO ARTIGO VALOR COMPENTENCIA)
from data_base.data_base import Con


class Infra:
    def __init__(self):
        self.id_infra = None
        self.codigo = None
        self.artigo = None
        self.competencia = None
        self.valor = None
        self.gravidade = None
        self.fator = None

    def set_infra(self, parametro):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM tr_infra WHERE "
                      f"(id_infra = {parametro}) OR "
                      f"(codigo = {parametro})")
            infra = c.fetchone()
            if infra:
                self.id_infra = infra['id_infra']
                self.codigo = infra['codigo']
                self.artigo = infra['artigo']
                self.competencia = infra['competencia']
                self.valor = infra['valor']
                self.gravidade = infra['gravidade']
                self.fator = infra['fator']
                return self
            else:
                return False
