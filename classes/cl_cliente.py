from data_base.data_base import Con


class Cliente:
    def __init__(self):
        self.id = None
        self.re = None
        self.dc = None
        self.nome = None
        self.tarja = None
        self.graduacao = None
        self.graduacao_txt = None
        self.admissao = None
        self.promocao = None
        self.ativo = None

    def set_cliente(self, txt):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM clientes WHERE "
                      f"re = '{txt}' OR "
                      f"id = '{txt}' OR "
                      f"nome = '{txt}'")
            cliente = c.fetchone()
            if cliente is None:
                print("Nao encontrado")
                return False
            else:
                self.id = cliente['id']
                self.re = cliente['re']
                self.dc = cliente['dc']
                self.nome = cliente['nome']
                self.tarja = cliente['tarja']
                self.graduacao = cliente['graduacao']
                self.graduacao_txt = cliente['graduacao_txt']
                self.admissao = cliente['admissao']
                self.promocao = cliente['promocao']
                self.ativo = cliente['ativo']
                return self

    def dados_para_lista(self, txt):
        self.set_cliente(txt)
        dados = [self.graduacao_txt, f"{self.re}-{self.dc}", self.nome]
        return dados


def insert_cliente(re, dc, nome, tarja, graduacao, graduacao_txt, admissao, promocao):
    cnx = Con().con()
    with cnx.cursor() as c:
        try:
            c.execute(f"INSERT INTO clientes "
                      f"(re, dc, nome, tarja, graduacao, graduacao_txt, admissao, promocao, ativo)"
                      f"VALUES"
                      f"('{re}', '{dc}', '{nome}', '{tarja}', {graduacao}, '{graduacao_txt}', "
                      f"'{admissao}', '{promocao}', 'ATIVO')")
            cnx.commit()
            print("Cliente Novo Cadastrado")
            return True
        except SystemError:
            return False


def edita_cliente(cliente_id, re, dc, nome, tarja, graduacao, graduacao_txt, admissao, promocao, ativo):
    cnx = Con().con()
    with cnx.cursor() as c:

        c.execute(f"UPDATE clientes SET "
                  f"re = '{re}', dc = '{dc}', nome = '{nome}', tarja = '{tarja}', graduacao = {graduacao}, "
                  f"graduacao_txt = '{graduacao_txt}', admissao = '{admissao}', promocao = '{promocao}', "
                  f"ativo = '{ativo}' WHERE id = {cliente_id}")
        cnx.commit()
        print("Cliente EDITADO")
        return True


# FUNÇÃO UTILIZADA PARA FOCUSOUT DO CAMPO RE
def verifica_re(campo, re):
    cliente = Cliente().set_cliente(re)
    if cliente:
        # mensagem("Erro", "RE informado ja existe")
        campo.focus()


# FUNÇÃO PARA RETORNAR LISTA PADRAO POR ANTIGUIDADE
def lista_clientes():
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM clientes WHERE ativo = 'ATIVO' ORDER BY graduacao, promocao, admissao, re")
        cliente = c.fetchall()
        return cliente
