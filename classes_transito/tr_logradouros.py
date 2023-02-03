from data_base.data_base import Con


class Logradouros:
    def __init__(self):
        self.id_logradouro = None
        self.logradouro = None

    def insert_logradouro(self):
        cnx = Con().con()
        with cnx.cursor() as c:
            try:
                c.execute(f"SELECT logradouro FROM tr_logradouros WHERE "
                          f"logradouro LIKE '{self.logradouro}%'")
                retorno = c.fetchone()
                if retorno:
                    pass
                else:
                    c.execute(f"INSERT INTO tr_logradouros (logradouro) VALUES ('{self.logradouro}')")
                    cnx.commit()
            except:
                pass


def lista_logradouros():
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute(f"SELECT logradouro FROM tr_logradouros ORDER BY logradouro")
        logr = c.fetchall()
        lista = []
        for i in logr:
            lista.append(i['logradouro'])
        return lista


def retorna_logradouro(parametro):
    cnx = Con().con()
    with cnx.cursor() as c:
        try:
            c.execute(f"SELECT logradouro FROM tr_logradouros WHERE "
                      f"logradouro LIKE '{parametro}%' ORDER BY logradouro")
            lista = c.fetchall()
            if len(lista) == 1:
                return lista[0]['logradouro']
            elif len(lista) > 1:
                return parametro
            elif len(lista) == 0:
                return parametro
        except:
            pass


# alimentar o autocomplete
def novo_logradouro(local):
    novo_local = Logradouros()
    novo_local.logradouro = local
    novo_local.insert_logradouro()
