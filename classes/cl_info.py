from data_base.data_base import con


class Info:
    def __init__(self):
        self.id_info = None
        self.re = None
        self.data_info = None
        self.descricao = None

    def set_info(self, info):
        cnx = con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM cl_info  WHERE (id_info = {info}) OR re = '{info}'")
            dados = c.fetchone()
            if dados:
                self.id_info = dados['id_info']
                self.re = dados['re']
                self.data_info = dados['data_info']
                self.descricao = dados['descricao']
                return self
            else:
                return False

    def insert_info(self):
        cnx = con()
        with cnx.cursor() as c:
            c.execute(f"INSERT INTO cl_info "
                      f"(re, data_info, descricao) "
                      f"VALUES ("
                      f"'{self.re}', "
                      f"'{self.data_info}', "
                      f"'{self.descricao}'"
                      f")")
            cnx.commit()

    def delete_info(self):
        cnx = con()
        with cnx.cursor() as c:
            c.execute(f"DELETE FROM cl_info WHERE id_info = {self.id_info}")
            cnx.commit()


def lista_info(re):
    cnx = con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM cl_info WHERE re = '{re}' ORDER BY data_info DESC")
        return c.fetchall()


def pesquisa_info_texto(re, texto):
    cnx = con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM cl_info WHERE (re = '{re}') "
                  f"AND (descricao LIKE '{texto}%') ORDER BY data_info DESC")
        resultado = c.fetchall()
        return resultado
