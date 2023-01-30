from classes.cl_cliente import *
from data_base.data_base import Con


class DadosPessoais(Cliente):
    def __init__(self):
        super(DadosPessoais, self).__init__()
        self.id_dados_pessoais = None
        self.re = None
        self.cpf = None
        self.rg = None
        self.nascimento = None
        self.cnh = None
        self.validade = None
        self.categoria = None
        self.sat = None
        self.nat = None
        self.uf = None
        self.rua = None
        self.numero = None
        self.complemento = None
        self.bairro = None
        self.cidade = None

    def set_dados_pessoais(self, re):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM cl_dados_pessoais  WHERE re = '{re}'")
            dados = c.fetchone()
            if dados:
                self.id_dados_pessoais = dados['id_dados_pessoais']
                self.re = dados['re']
                self.cpf = dados['cpf']
                self.rg = dados['rg']
                self.nascimento = dados['nascimento']
                self.cnh = dados['cnh']
                self.validade = dados['validade']
                self.categoria = dados['categoria']
                self.sat = dados['sat']
                self.nat = dados['nat']
                self.uf = dados['uf']
                self.rua = dados['rua']
                self.numero = dados['numero']
                self.complemento = dados['complemento']
                self.bairro = dados['bairro']
                self.cidade = dados['cidade']
                return self
            else:
                return False

    def insert_dados_pessoais(self):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"INSERT INTO cl_dados_pessoais "
                      f"(re, cpf, rg, nascimento, cnh, validade, categoria, sat, "
                      f"nat, uf, rua, numero, complemento, bairro, cidade) "
                      f"VALUES ("
                      f"'{self.re}', "
                      f"'{self.cpf}', "
                      f"'{self.rg}', "
                      f"'{self.nascimento}', "
                      f"'{self.cnh}', "
                      f"'{self.validade}', "
                      f"'{self.categoria}', "
                      f"'{self.sat}', "
                      f"'{self.nat}', "
                      f"'{self.uf}', "
                      f"'{self.rua}', "
                      f"'{self.numero}', "
                      f"'{self.complemento}', "
                      f"'{self.bairro}', "
                      f"'{self.cidade}'"
                      f")")
            cnx.commit()

    def update_dados_pessoais(self):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"UPDATE cl_dados_pessoais SET "
                      f"cpf = '{self.cpf}', "
                      f"rg = '{self.rg}', "
                      f"nascimento = '{self.nascimento}', "
                      f"cnh = '{self.cnh}', "
                      f"validade = '{self.validade}', "
                      f"categoria = '{self.categoria}', "
                      f"sat = '{self.sat}', "
                      f"nat = '{self.nat}', "
                      f"uf = '{self.uf}', "
                      f"rua = '{self.rua}', "
                      f"numero = '{self.numero}', "
                      f"complemento = '{self.complemento}', "
                      f"bairro = '{self.bairro}', "
                      f"cidade = '{self.cidade}' "
                      f"WHERE re = '{self.re}'"
                      )
            cnx.commit()


def lista_dados_pessoais():
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute("SELECT re, cnh, validade, categoria, sat FROM cl_dados_pessoais")
        return c.fetchall()
