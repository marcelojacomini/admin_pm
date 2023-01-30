from data_base.data_base import Con


class Epi:
    def __init__(self):
        self.id_epi = None
        self.re = None
        self.arma = None
        self.colete = None
        self.validade_colete = None
        self.algemas = None
        self.tonfa = None
        self.espargidor = None
        self.validade_espargidor = None

    def set_epi(self, re):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM cl_epi  WHERE re = '{re}'")
            dados = c.fetchone()
            if dados:
                self.id_epi = dados['id_epi']
                self.arma = dados['arma']
                self.colete = dados['colete']
                self.validade_colete = dados['validade_colete']
                self.algemas = dados['algemas']
                self.tonfa = dados['tonfa']
                self.espargidor = dados['espargidor']
                self.validade_espargidor = dados['validade_espargidor']
                return self
            else:
                return False

    def insert_epi(self):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"INSERT INTO cl_epi "
                      f"(re, arma, colete, validade_colete, algemas, tonfa, espargidor, validade_espargidor) "
                      f"VALUES ("
                      f"'{self.re}', "
                      f"'{self.arma}', "
                      f"'{self.colete}', "
                      f"'{self.validade_colete}', "
                      f"'{self.algemas}', "
                      f"'{self.tonfa}', "
                      f"'{self.espargidor}', "
                      f"'{self.validade_espargidor}'"
                      f")")
            cnx.commit()

    def update_epi(self):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"UPDATE cl_epi SET "
                      f"arma = '{self.arma}', "
                      f"colete = '{self.colete}', "
                      f"validade_colete = '{self.validade_colete}', "
                      f"algemas = '{self.algemas}', "
                      f"espargidor = '{self.espargidor}', "
                      f"validade_espargidor = '{self.validade_espargidor}' "
                      f"WHERE re = '{self.re}'"
                      )
            cnx.commit()
