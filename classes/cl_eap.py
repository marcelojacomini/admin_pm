from data_base.data_base import con


class Eap:
    def __init__(self):
        self.id_eap = None
        self.re = None
        self.periodo_ead = None
        self.data_eap = None
        self.send_mail = None

    def set_eap(self, texto):
        cnx = con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM cl_eap  WHERE (id_eap = {texto}) OR re = '{texto}'")
            dados = c.fetchone()
            if dados:
                self.id_eap = dados['id_eap']
                self.re = dados['re']
                self.periodo_ead = dados['periodo_ead']
                self.data_eap = dados['data_eap']
                self.send_mail = dados['send_mail']
                return self
            else:
                return False


def insert_eap(re, periodo, data, send_mail):
    eap = Eap()
    eap = eap.set_eap(re)
    if not eap:
        cnx = con()
        with cnx.cursor() as c:
            c.execute(f"INSERT INTO cl_eap "
                      f"(re, periodo_ead, data_eap, send_mail) "
                      f"VALUES ("
                      f"'{re}', "
                      f"'{periodo}', "
                      f"'{data}', "
                      f"'1950-01-01'"
                      f"'{send_mail}')")
            cnx.commit()
    else:
        cnx = con()
        with cnx.cursor() as c:
            c.execute(f"UPDATE cl_eap SET "
                      f"periodo_ead = '{periodo}', "
                      f"data_eap = '{data}' "
                      f"WHERE re = '{re}'")
            cnx.commit()


def edita_aviso_eap(re, aviso):
    cnx = con()
    with cnx.cursor() as c:
        c.execute(f"UPDATE cl_eap SET "
                  f"send_mail = '{aviso}'"
                  f"WHERE re = '{re}'")
        cnx.commit()
