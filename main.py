import ttkbootstrap

from screen_cliente.clientegeral import ClienteGeral
from screen_cliente.clientes_contatos_geral import *
from screen_cliente.clientes_cnh_geral import *
from screen_cliente.clientes_eap_geral import *

from screen_banco_horas.banco_horas_geral import *

from screen_transito.transito_cadastro import *
from screen_transito.transito_consulta import *
from screen_transito.transito_relatorios import *

from screen_config.cf_config import *


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
        # self.st.theme_use("admin_brown")
        self.st.theme_use("darkly")

        ######################################################################################################
        # menu (flat, groove, raised, ridge, solid, or sunken)
        ######################################################################################################
        frame_efetivo = ttk.Frame(self, borderwidth=2, relief='groove')
        frame_efetivo.place(relx=0.05, rely=0.05, relwidth=0.30)

        self.bt_cliente = ttk.Button(frame_efetivo, text="EFETIVO - GERENCIAMENTO GERAL", width=40,
                                     command=ClienteGeral)
        self.bt_cliente.pack(fill='x', pady=5, padx=2)

        self.bt_cliente_contatos = ttk.Button(frame_efetivo, text="EFETIVO - CONTATOS", style="secondary",
                                              command=ClientesContatosGeral)
        self.bt_cliente_contatos.pack(fill='x', pady=5, padx=2)

        self.bt_cliente_cnh = ttk.Button(frame_efetivo, text="EFETIVO - DADOS DE CNH",
                                         style='secondary', command=ClientesCnhGeral)
        self.bt_cliente_cnh.pack(fill='x', pady=5, padx=2)

        self.bt_cliente_eap = ttk.Button(frame_efetivo, text="EFETIVO - CONTROLE DE EAP", style="secondary",
                                         command=ClientesEapGeral)
        self.bt_cliente_eap.pack(fill='x', pady=5, padx=2)

        self.bt_bco_horas = ttk.Button(frame_efetivo, text="EFETIVO - BANCO DE HORAS",
                                       width=40, style="secondary", command=BancoHorasGeral)
        self.bt_bco_horas.pack(fill='x', pady=5, padx=2)

        ######################################################################################################
        frame_transito = ttk.Frame(self, borderwidth=2, relief='solid')
        frame_transito.place(relx=0.40, rely=0.05, relwidth=0.30)

        self.bt_cad_ait = ttk.Button(frame_transito, text="TRÂNSITO - CADASTRAR AIT", style='info',
                                     command=TransitoCadastro)
        self.bt_cad_ait.pack(fill='x', pady=5, padx=2)

        self.bt_consluta_ait = ttk.Button(frame_transito, text="TRÂNSITO - CONSULTAS", style='info',
                                          command=TransitoConsulta)
        self.bt_consluta_ait.pack(fill='x', pady=5, padx=2)

        self.bt_relatorios_ait = ttk.Button(frame_transito, text="TRÂNSITO - RELATÓRIOS", style='info',
                                            command=TransitoRelatorios)
        self.bt_relatorios_ait.pack(fill='x', pady=5, padx=2)

        frame_config = ttk.Frame(self, borderwidth=2, relief='solid')
        frame_config.place(relx=0.75, rely=0.05, relwidth=0.20)
        bt_config = ttk.Button(frame_config, text='CONFIGURAÇÕES', style='dark', command=Configuracoes)
        bt_config.pack(fill='x', pady=5, padx=2)

##############################################
# SE MAIN CARREGA TELA INICIAL
##############################################
if __name__ == "__main__":
    app = App()
    app.mainloop()
