from imports import *
from data_base.data_base import *
PASTA_USER = path.join(path.expanduser("~"))


class Configuracoes(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        self.geometry(tk_center(self, 880, 650))
        self.title("ADMIN - CONFIGURAÇÕES")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        # HEADER
        header = ttk.Frame(self)
        header.pack(fill='x', padx=10)
        lb_header = ttk.Label(header, text='Configurações', font=('', 16, 'bold'))
        lb_header.grid(row=0, column=0, pady=5)

        fr_1 = ttk.Frame(self, borderwidth=1, relief='solid')
        fr_1.pack(padx=30, pady=30)

        # SERVER
        fr_server = ttk.Frame(fr_1)
        fr_server.pack(fill='x', padx=10, pady=15)

        lb_host = ttk.Label(fr_server, text='Host (endereço do servidor):', width=30, anchor='e')
        lb_host.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.server_host = ttk.Entry(fr_server)
        self.server_host.grid(row=0, column=1, sticky='w', padx=3, pady=5)

        bt_host = ttk.Button(fr_server, text='Atualizar "HOST" e Testar Conexão', command=self.atualizar_host)
        bt_host.grid(row=1, column=0, columnspan=2, sticky='we')

        with open(f'{PASTA_USER}\\conf_admin_pm\\config.conf', 'r') as conf_atual:
            self.server_host.insert(0, conf_atual.read())

        ##########################################################################################################
        # SENHA ADMIN
        fr_2 = ttk.Frame(self, borderwidth=1, relief='solid')
        fr_2.pack(padx=30)

        fr_admin = ttk.Frame(fr_2)
        fr_admin.pack(fill='x', padx=10, pady=15)
        lb_admin = ttk.Label(fr_admin, text='Alterar Senha "admin"')
        lb_admin.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        lb_sa = ttk.Label(fr_admin, text='Senha atual:')
        lb_sa.grid(row=1, column=0, sticky='e')
        self.senha_atual = ttk.Entry(fr_admin)
        self.senha_atual.grid(row=1, column=1, sticky='w')
        lb_ns = ttk.Label(fr_admin, text='Nova senha:')
        lb_ns.grid(row=2, column=0, sticky='e')
        self.nova_senha = ttk.Entry(fr_admin)
        self.nova_senha.grid(row=2, column=1, sticky='w', pady=10)

        # MENSAGEM
        self.lb_msg = ttk.Label(self, text='', font=('', 12, 'bold'), foreground='red')
        self.lb_msg.pack(side='bottom', fill='x', pady=25, padx=25)

    def atualizar_host(self):
        # LOCAL DA PASTA C:\USERS\'NOME DO USER'
        with open(f'{PASTA_USER}\\conf_admin_pm\\config.conf', 'w') as cofigurarLocal:
            cofigurarLocal.write(self.server_host.get())
        try:
            with con_test() as c:
                self.lb_msg['foreground'] = 'green'
                self.lb_msg['text'] = 'Conexão OK!\nReinicie o software para concluir as alterações!'
                print(c)
        except Exception as e:
            self.lb_msg['foreground'] = 'red'
            self.lb_msg['text'] = f"Conexão FALHOU!\n(O Servidor não foi encontrado!!!)"
            print(e)
