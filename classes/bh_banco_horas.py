from classes.cl_cliente import *


class SaldoHoras:
    def __init__(self):
        self.id_saldo = None
        self.re = None
        self.saldo = None

    def set_cliente_saldo(self, re):
        cnx = Con().con()
        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM bh_saldo WHERE re = '{re}'")
            cliente = c.fetchone()
            if cliente:
                self.id_saldo = cliente['id_saldo']
                self.re = cliente['re']
                self.saldo = cliente['saldo']
                return self
            else:
                self.re = re
                self.saldo = 0
                c.execute(f"INSERT INTO bh_saldo (re, saldo) VALUES ('{self.re}', {self.saldo})")
                cnx.commit()
                return self

    def altera_saldo(self):
        try:
            cnx = Con().con()
            with cnx.cursor() as c:
                c.execute(f"UPDATE bh_saldo SET saldo = {self.saldo} WHERE re = '{self.re}'")
                cnx.commit()
            return True
        except:
            return False


class BancoHoras:
    def __init__(self):
        self.id_banco = None
        self.re = None
        self.data = None
        self.hora = None
        self.motivo = None

    def cria_banco(self, re, data, hora, motivo):
        self.re = re
        self.data = data
        self.hora = hora
        self.motivo = motivo
        return self

    def insert_banco(self):
        try:
            cnx = Con().con()
            with cnx.cursor() as c:
                c.execute(f"INSERT INTO bh_banco (re, data, hora, motivo) "
                          f"VALUES ('{self.re}', '{self.data}', {self.hora}, '{self.motivo}')")
                cnx.commit()
                confere_horas(self.re)
            return True
        except:
            return False


def extrato_horas(re):
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute(f"SELECT * FROM bh_banco WHERE re = '{re}' ORDER BY data DESC")
        return c.fetchall()


def confere_horas(re):
    cliente = SaldoHoras().set_cliente_saldo(re)
    extrato = extrato_horas(re)
    resultado = 0
    for i in extrato:
        resultado = resultado + i['hora']
    cliente.saldo = resultado
    cliente.altera_saldo()
