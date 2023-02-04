import os
from os import path
import pymysql.cursors
# LOCAL DA PASTA C:\USERS\'NOME DO USER'
pasta_user = path.join(path.expanduser("~"))


class Con:
    ##############################################################################################################
    # INICIANDO AS VARIÁVEIS DE CONEXÃO
    # O sistema inicia as variáveis de conexão sem a conexão e host definidos
    ##############################################################################################################
    def __init__(self):
        self.admin = "system"
        self.admin_pass = "conexao_3pel_pm"
        self.database = "sql_admin_pm"
        self.conexao = None
        self.host = None

    # DEFINE FUNÇÃO DE CONEXÃO E RETORNA A CONEXÃO
    def con(self):
        # VERIFICA SE PASTA __conf_ait existe
        if path.exists(f'{pasta_user}\\conf_admin_pm'):
            # Se a pasta '__conf_ait existir no diretório 'user da máquina executada',
            # fará a leitura do arquivo 'config.conf' que irá conter o caminho para o banco de dados 'MariaDB'
            # após, irá alterar a variável self.host com o caminho do banco
            with open(f'{pasta_user}\\conf_admin_pm\\config.conf') as leitura:
                self.host = leitura.read()
        else:
            # caso não exista a pasta de configuração chama função que irá criar a pasta.
            self.file_conf()
        # print(self.host)
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                database=self.database,
                user=self.admin,
                password=self.admin_pass,
                cursorclass=pymysql.cursors.DictCursor
            )

            # print("Conectado ao banco")
            return self.conexao
        except SystemError:
            print("Erro de conexão MARIA DB")
            return False

    # FUNÇÃO CHAMADA SE NÃO HOUVER PASTA DE CONFIGURAÇÃO
    def file_conf(self):
        # CRIA PASTA PARA ARQUIVO CONF
        os.makedirs(f'{pasta_user}\\conf_admin_pm')
        # Cria e Abre o arquivo 'config.conf', após, define a variável 'self.host como 'localhost' (COMO PADRÃO)
        with open(f'{pasta_user}\\conf_admin_pm\\config.conf', 'w') as cofigurarLocal:
            cofigurarLocal.write("localhost")
            self.host = "localhost"
        # APÓS CRIAR ARQUIVO CONF CHAMA A FUNÇÃO PARA CRIAR DATABASE,
        # SE FOR A PRIMEIRA EXECUÇÃO DO BANCO IRÁ CRIAR AS TABELAS
        self.create_database()

    # FUNÇÃO CHAMADA PARA CRIAR O DATABASE E TABELAS
    def create_database(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                user=self.admin,
                password=self.admin_pass,
                cursorclass=pymysql.cursors.DictCursor
            )
        except SystemError:
            print("Erro na criação do 'DATABASE'")

        with self.conexao.cursor() as c:
            # CRIA DATABASE
            c.execute("CREATE DATABASE IF NOT EXISTS sql_admin_pm")

        try:
            self.conexao = pymysql.connect(
                host=self.host,
                database=self.database,
                user=self.admin,
                password=self.admin_pass,
                cursorclass=pymysql.cursors.DictCursor
            )
        except SystemError:
            print("Erro na entrada de criação das tabelas!!!!")

        with self.conexao.cursor() as c:
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


Con().create_database()
