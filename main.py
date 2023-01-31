import ttkbootstrap

from screen_cliente.clientegeral import ClienteGeral
from screen_cliente.clientes_contatos_geral import *
from screen_cliente.clientes_cnh_geral import *
from screen_cliente.clientes_eap_geral import *

from screen_banco_horas.banco_horas_geral import *

from screen_transito.transito_cadastro import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 900, 600)
        self.geometry(geo)
        self.title("ADMIN - POLICIA MILITAR")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.st = ttkbootstrap.Style()
        self.st.theme_use("new_silver")

        ######################################################################################################
        # menu
        ######################################################################################################
        self.options = ttk.Frame(self)
        self.options.pack(fill='x', pady=25, padx=10)

        self.bt_cliente = ttk.Button(self.options, text="GERENCIAR EFETIVO", width=40, command=ClienteGeral)
        self.bt_cliente.grid(row=0, column=0, sticky='w', pady=15)

        self.bt_cliente_contatos = ttk.Button(self.options, text="EFETIVO CONTATOS",
                                              width=40, command=ClientesContatosGeral)
        self.bt_cliente_contatos.grid(row=1, column=0, sticky='w', pady=15)

        self.bt_cliente_cnh = ttk.Button(self.options, text="DADOS CNH",
                                         width=40, command=ClientesCnhGeral)
        self.bt_cliente_cnh.grid(row=2, column=0, sticky='w')

        self.bt_cliente_eap = ttk.Button(self.options, text="DADOS EAP",
                                         width=40, style='info', command=ClientesEapGeral)
        self.bt_cliente_eap.grid(row=3, column=0, sticky='w', pady=15)

        self.bt_bco_horas = ttk.Button(self.options, text="BANCO DE HORAS",
                                       width=40, style='dark', command=BancoHorasGeral)
        self.bt_bco_horas.grid(row=4, column=0, sticky='w')

        self.bt_cad_ait = ttk.Button(self.options, text="CADASTRAR AIT",
                                     width=40, style='dark', command=TransitoCadastro)
        self.bt_cad_ait.grid(row=0, column=1, sticky='w', padx=20, pady=25)


##############################################
# SE MAIN CARREGA TELA INICIAL
##############################################
if __name__ == "__main__":
    app = App()
    app.mainloop()
