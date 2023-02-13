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
        self.admin_pass = "O1u&ZV0qvouA4OQ1ZBt*F@V98"
        self.database = "sql_admin_pm"
        self.conexao = None
        self.host = None

        # VERIFICA SE PASTA __conf_ait existe
        if path.exists(f'{pasta_user}\\conf_admin_pm'):
            with open(f'{pasta_user}\\conf_admin_pm\\config.conf') as leitura:
                self.host = leitura.read()
        else:
            # caso não exista a pasta de configuração chama função que irá criar a pasta.
            # CRIA PASTA PARA ARQUIVO CONF
            os.makedirs(f'{pasta_user}\\conf_admin_pm')
            # Cria e Abre o arquivo 'config.conf', após, define a variável 'self.host como 'localhost' (COMO PADRÃO)
            with open(f'{pasta_user}\\conf_admin_pm\\config.conf', 'w') as cofigurarLocal:
                cofigurarLocal.write("localhost")
                self.host = "localhost"

        # CHAMA A FUNÇÃO PARA RETORNAR A CONEXÃO

    def conectar(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                database=self.database,
                user=self.admin,
                password=self.admin_pass,
                cursorclass=pymysql.cursors.DictCursor
                )
            return self.conexao
        except Exception as e:
            print("Erro de conexão MARIA DB", e)
            return False

    def teste_de_conexao(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                database=self.database,
                user=self.admin,
                password=self.admin_pass,
                cursorclass=pymysql.cursors.DictCursor
                )
            return self.conexao
        except Exception as e:
            print("Erro de conexão MARIA DB", e)
            return False


def con():
    return Con().conectar()


def con_test():
    return Con().teste_de_conexao()
