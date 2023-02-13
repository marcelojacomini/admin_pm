from functions.functions import pass_converter
from data_base.data_base import con


def create_database():
    """
    try:
        conexao = pymysql.connect(
            host=host,
            user=user_system,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        with conexao.cursor() as c:
            # CRIA DATABASE
            c.execute("CREATE DATABASE IF NOT EXISTS sql_admin_pm")
    except SystemError:
        print("Erro na criação do 'DATABASE'")

    try:
        conexao = pymysql.connect(
            host=host,
            database='sql_admin_pm',
            user=user_system,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
    """
    try:
        cnx = con()
        with cnx.cursor() as c:
            # cria tabela de clientes
            tabela_clientes = "CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY, " \
                              "re VARCHAR(6)," \
                              "dc VARCHAR(1)," \
                              "nome VARCHAR (255)," \
                              "tarja VARCHAR (50)," \
                              "graduacao INT," \
                              "graduacao_txt VARCHAR(30)," \
                              "admissao DATE," \
                              "promocao DATE," \
                              "ativo VARCHAR(10)" \
                              ");"
            c.execute(tabela_clientes)

            tabela_contatos = "CREATE TABLE IF NOT EXISTS cl_contatos (id_contato INT AUTO_INCREMENT PRIMARY KEY, " \
                              "re VARCHAR(6), " \
                              "tipo VARCHAR(20), " \
                              "contato VARCHAR(100) " \
                              ");"
            c.execute(tabela_contatos)

            # CRIA TABELA DADOS PESSOAIS
            tabela_tdados_pessoais = "CREATE TABLE IF NOT EXISTS cl_dados_pessoais ( " \
                                     "id_dados_pessoais INT AUTO_INCREMENT PRIMARY KEY, " \
                                     "re VARCHAR(6)," \
                                     "cpf VARCHAR(15), " \
                                     "rg VARCHAR(15), " \
                                     "nascimento DATE, " \
                                     "cnh VARCHAR (20), " \
                                     "validade DATE, " \
                                     "categoria VARCHAR(5), " \
                                     "sat VARCHAR(5), " \
                                     "nat VARCHAR(100), " \
                                     "uf VARCHAR(4), " \
                                     "rua VARCHAR(100), " \
                                     "numero VARCHAR(10), " \
                                     "complemento VARCHAR(30), " \
                                     "bairro VARCHAR(100), " \
                                     "cidade VARCHAR(100)" \
                                     ");"
            c.execute(tabela_tdados_pessoais)

            tabela_epi = "CREATE TABLE IF NOT EXISTS cl_epi ( " \
                         "id_epi INT AUTO_INCREMENT PRIMARY KEY, " \
                         "re VARCHAR(6), " \
                         "arma VARCHAR(15)," \
                         "colete VARCHAR(15), " \
                         "validade_colete DATE, " \
                         "algemas VARCHAR (15), " \
                         "tonfa VARCHAR(5), " \
                         "espargidor VARCHAR(15), " \
                         "validade_espargidor DATE " \
                         ");"
            c.execute(tabela_epi)

            tabela_info = "CREATE TABLE IF NOT EXISTS cl_info (id_info INT AUTO_INCREMENT PRIMARY KEY, " \
                          "re VARCHAR(6), " \
                          "data_info DATE, " \
                          "descricao VARCHAR(255) " \
                          ");"
            c.execute(tabela_info)

            tabela_eap = "CREATE TABLE IF NOT EXISTS cl_eap (id_eap INT AUTO_INCREMENT PRIMARY KEY, " \
                         "re VARCHAR(6), " \
                         "periodo_ead VARCHAR(30), " \
                         "data_eap DATE ," \
                         "send_mail DATE" \
                         ");"
            c.execute(tabela_eap)

            tabela_mail = "CREATE TABLE IF NOT EXISTS fn_mail (id_mail INT AUTO_INCREMENT PRIMARY KEY, " \
                          "password VARCHAR(255), " \
                          "msg_from VARCHAR(255), " \
                          "mail_smtp VARCHAR(255)" \
                          ");"
            c.execute(tabela_mail)

            # CRIA TABELA extrato banco
            tabela_banco = "CREATE TABLE IF NOT EXISTS bh_banco (id_banco INT AUTO_INCREMENT PRIMARY KEY, " \
                           "re VARCHAR(6)," \
                           "data DATE," \
                           "hora INT," \
                           "motivo VARCHAR(255));"
            c.execute(tabela_banco)

            # CRIA TABELA saldo banco
            tabela_tsaldo = "CREATE TABLE IF NOT EXISTS bh_saldo (id_saldo INT AUTO_INCREMENT PRIMARY KEY, " \
                            "re VARCHAR(6)," \
                            "saldo INT);"
            c.execute(tabela_tsaldo)

            tabela_ait = "CREATE TABLE IF NOT EXISTS tr_ait (id_ait INT AUTO_INCREMENT PRIMARY KEY, " \
                         "numero VARCHAR(255)," \
                         "placa VARCHAR(255)," \
                         "condutor VARCHAR(255)," \
                         "local VARCHAR(255)," \
                         "dia DATE," \
                         "hora VARCHAR(10)," \
                         "re VARCHAR(10)," \
                         "codigo INT," \
                         "competencia VARCHAR(255)," \
                         "artigo VARCHAR(255)," \
                         "crr VARCHAR(255)," \
                         "remocao VARCHAR(255)," \
                         "cnh VARCHAR(255)," \
                         "alcoolemia VARCHAR(255)," \
                         "obs VARCHAR(255)," \
                         "talao VARCHAR(255)," \
                         "valor FLOAT);"
            c.execute(tabela_ait)
            # CRIA TABELA INFRA
            tabela_inf = "CREATE TABLE IF NOT EXISTS tr_infra (id_infra INT AUTO_INCREMENT PRIMARY KEY, " \
                         "codigo INT," \
                         "artigo VARCHAR(255)," \
                         "competencia VARCHAR(255)," \
                         "valor FLOAT," \
                         "gravidade VARCHAR(255)," \
                         "fator INT);"
            c.execute(tabela_inf)

            tabela_logradouro = "CREATE TABLE IF NOT EXISTS tr_logradouros " \
                                "(id_logradouro INT AUTO_INCREMENT PRIMARY KEY, " \
                                "logradouro VARCHAR(255));"
            c.execute(tabela_logradouro)

            tabela_talonario = "CREATE TABLE IF NOT EXISTS tr_talao " \
                               "(id_talao INT AUTO_INCREMENT PRIMARY KEY, " \
                               "re VARCHAR(6), " \
                               "mi VARCHAR(15), " \
                               "mf VARCHAR(15), " \
                               "ei VARCHAR(15), " \
                               "ef VARCHAR(15));"
            c.execute(tabela_talonario)

            tabela_users = "CREATE TABLE IF NOT EXISTS users " \
                           "(id_user INT AUTO_INCREMENT PRIMARY KEY, " \
                           "user VARCHAR(20), " \
                           "password VARCHAR(255));"
            c.execute(tabela_users)
            c.execute("SELECT * FROM users WHERE user = 'admin'")
            if not c.fetchone():
                password_admin = pass_converter('1234')
                c.execute(f"INSERT INTO users (user, password) VALUES ('admin', '{password_admin}')")
                cnx.commit()

    except Exception as e:
        print("Erro na entrada de criação das tabelas!!!!", e)


create_database()
