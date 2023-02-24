# CLIENTES
from screen_cliente.clientegeral import *
from screen_cliente.clientes_contatos_geral import *
from screen_cliente.clientes_cnh_geral import *
from screen_cliente.clientes_eap_geral import *
# BANCO DE HORAS
from screen_banco_horas.banco_horas_geral import *
# TRANSITO
from screen_transito.transito_cadastro import *
from screen_transito.transito_consulta import *
from screen_transito.transito_relatorios import *
# CONFIGURAÇÕES
from screen_config.cf_config import *
from functions.functions import pass_converter


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        self.geometry(tk_center(self, 900, 600))
        self.title("ADMIN - POLICIA MILITAR")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.st = ttk.Style()
        # self.st.theme_use("admin_brown")
        self.st.theme_use("darkly")

        #######
        # TESTE
        #######
        SESSION_USER.user = None

        ######################################################################################################
        # LOGIN
        ######################################################################################################

        self.tela_login = ttk.Frame(self)
        self.tela_login.pack(fill='both', expand=True)

        self.logo = ttk.PhotoImage(file='img/pm.png')
        self.frame_img = ttk.Label(self.tela_login, image=self.logo)
        self.frame_img.pack(fill='y', side='left', expand=True)

        self.area_login = ttk.Frame(self.tela_login, borderwidth=1, relief='sunken')
        self.area_login.pack(fill='y', side='right', expand=True, pady=125)
        self.lb_login = ttk.Label(self.area_login, text='LOGIN - SISTEMA ADMIN-PM', font=('', 12, 'bold'),
                                  foreground='#FFFF00')
        self.lb_login.grid(row=0, column=0, padx=45, columnspan=2, pady=45)

        self.lb_user = ttk.Label(self.area_login, text='USUÁRIO:', font=('', 10, 'bold'), foreground='#FDF5E6')
        self.lb_user.grid(row=1, column=0, padx=15, sticky='e')
        self.user = ttk.Entry(self.area_login)
        self.user.grid(row=1, column=1, sticky='w')

        self.lb_senha = ttk.Label(self.area_login, text='SENHA:', font=('', 10, 'bold'), foreground='#FDF5E6')
        self.lb_senha.grid(row=2, column=0, padx=15, sticky='e')
        self.senha = ttk.Entry(self.area_login, show='*')
        self.senha.grid(row=2, column=1, sticky='w', pady=15)

        self.bt_pass = ttk.Button(self.area_login, text='ENTRAR', style='info', command=self.logar)
        self.bt_pass.grid(row=3, column=0, columnspan=2, pady=15, sticky='we', padx=45)

        self.lb_msg = ttk.Label(self.area_login, text='', foreground='#FFFF00')
        self.lb_msg.grid(row=4, column=0, columnspan=2, pady=15, sticky='we', padx=45)

        ######################################################################################################
        # MENU
        ######################################################################################################
        self.tela_inicial = ttk.Frame(self)
        # self.tela_inicial.pack(fill='both', expand=True)

        self.frame_efetivo = ttk.Frame(self.tela_inicial, borderwidth=2, relief='groove')
        self.frame_efetivo.place(relx=0.05, rely=0.05, relwidth=0.30)

        self.bt_cliente = ttk.Button(self.frame_efetivo, text="EFETIVO - GERENCIAMENTO GERAL", width=40,
                                     command=ClienteGeral)
        self.bt_cliente.pack(fill='x', pady=5, padx=2)

        self.bt_cliente_contatos = ttk.Button(self.frame_efetivo, text="EFETIVO - CONTATOS", style="secondary",
                                              command=ClientesContatosGeral)
        self.bt_cliente_contatos.pack(fill='x', pady=5, padx=2)

        self.bt_cliente_cnh = ttk.Button(self.frame_efetivo, text="EFETIVO - DADOS DE CNH",
                                         style='secondary', command=ClientesCnhGeral)
        self.bt_cliente_cnh.pack(fill='x', pady=5, padx=2)

        self.bt_cliente_eap = ttk.Button(self.frame_efetivo, text="EFETIVO - CONTROLE DE EAP", style="secondary",
                                         command=ClientesEapGeral)
        self.bt_cliente_eap.pack(fill='x', pady=5, padx=2)

        self.bt_bco_horas = ttk.Button(self.frame_efetivo, text="EFETIVO - BANCO DE HORAS",
                                       width=40, style="secondary", command=BancoHorasGeral)
        self.bt_bco_horas.pack(fill='x', pady=5, padx=2)

        ######################################################################################################
        self.frame_transito = ttk.Frame(self.tela_inicial, borderwidth=1, relief='groove')
        self.frame_transito.place(relx=0.40, rely=0.05, relwidth=0.30)

        self.bt_cad_ait = ttk.Button(self.frame_transito, text="TRÂNSITO - CADASTRAR AIT", style='info',
                                     command=TransitoCadastro)
        self.bt_cad_ait.pack(fill='x', pady=5, padx=2)

        self.bt_consluta_ait = ttk.Button(self.frame_transito, text="TRÂNSITO - CONSULTAS", style='info',
                                          command=TransitoConsulta)
        self.bt_consluta_ait.pack(fill='x', pady=5, padx=2)

        self.bt_relatorios_ait = ttk.Button(self.frame_transito, text="TRÂNSITO - RELATÓRIOS", style='info',
                                            command=TransitoRelatorios)
        self.bt_relatorios_ait.pack(fill='x', pady=5, padx=2)

        self.frame_config = ttk.Frame(self.tela_inicial, borderwidth=2, relief='solid')

        bt_config = ttk.Button(self.frame_config, text='CONFIGURAÇÕES', style='dark', command=Configuracoes)
        bt_config.pack(fill='x', pady=5, padx=2)

        self.user.focus()

        self.bind('<Return>', self.enter_press)

        self.x_login = 0

    def logar(self):
        SESSION_USER.user = self.user.get()
        SESSION_USER.password = pass_converter(self.senha.get())
        if SESSION_USER.set_user():
            if SESSION_USER.user == 'admin':
                self.frame_config.place(relx=0.75, rely=0.05, relwidth=0.20)
            self.tela_login.destroy()
            self.tela_inicial.pack(fill='both', expand=True, pady=60)
        else:
            self.x_login = self.x_login + 1
            self.lb_msg['text'] = f'Usuário ou senha inválidos!!! - ({self.x_login})'

    def enter_press(self, event):
        try:
            self.logar()
        except Exception as e:
            print(event, e)


##############################################
# SE MAIN CARREGA TELA INICIAL
##############################################
if __name__ == "__main__":
    app = App()
    app.mainloop()
