from imports import *
from data_base.data_base import *
from screen_config.cf_usuarios import *
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
        fr_1.pack(padx=30, pady=30, fill='x')

        # SERVER
        fr_server = ttk.Frame(fr_1)
        fr_server.pack(fill='x', padx=10, pady=15)

        lb_host = ttk.Label(fr_server, text='Host (endereço do servidor):', width=30, anchor='e')
        lb_host.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.server_host = ttk.Entry(fr_server)
        self.server_host.grid(row=0, column=1, sticky='w', padx=3, pady=5)

        bt_host = ttk.Button(fr_server, text='Atualizar "HOST" e Testar Conexão', command=self.atualizar_host)
        bt_host.grid(row=0, column=3, sticky='we', padx=15)

        with open(f'{PASTA_USER}\\conf_admin_pm\\config.conf', 'r') as conf_atual:
            self.server_host.insert(0, conf_atual.read())

        ##########################################################################################################
        # SENHA ADMIN
        fr_2 = ttk.Frame(self, borderwidth=1, relief='solid')
        fr_2.pack(padx=30, fill='x')

        fr_admin = ttk.Frame(fr_2)
        fr_admin.pack(fill='x', padx=10, pady=15)
        lb_admin = ttk.Label(fr_admin, text='Alterar Senha "admin": ')
        lb_admin.grid(row=0, column=0, padx=10, pady=10)

        lb_sa = ttk.Label(fr_admin, text='Senha atual: ')
        lb_sa.grid(row=0, column=1, sticky='e')
        self.senha_atual = ttk.Entry(fr_admin, show='*')
        self.senha_atual.grid(row=0, column=2, sticky='w')
        lb_ns = ttk.Label(fr_admin, text='Nova senha: ')
        lb_ns.grid(row=0, column=3, padx=5, sticky='e')
        self.nova_senha = ttk.Entry(fr_admin, show='*')
        self.nova_senha.grid(row=0, column=4, sticky='w', pady=10)

        bt_altera_admin = ttk.Button(fr_admin, text='Alterar Senha Admin', command=self.atualizar_senha_admin)
        bt_altera_admin.grid(row=0, column=5, padx=10)

        ##########################################################################################################
        # USUÁRIOS
        fr_3 = ttk.Frame(self, borderwidth=1, relief='solid')
        fr_3.pack(padx=30, fill='x', pady=10)
        bt_usuarios = ttk.Button(fr_3, text="GERENCIAR USUÁRIOS", command=Usuarios)
        bt_usuarios.grid(row=0, column=0, padx=5, pady=10)

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

    def atualizar_senha_admin(self):
        try:
            senha_atual = pass_converter(self.senha_atual.get())
            nova_senha = pass_converter(self.nova_senha.get())
            cnx = con()
            with cnx.cursor() as c:
                c.execute(f"SELECT * FROM users WHERE (user = 'admin') AND (password = '{senha_atual}')")
                if c.fetchone():
                    c.execute(f"UPDATE users SET password = '{nova_senha}' WHERE user = 'admin'")
                    cnx.commit()
                    self.lb_msg['text'] = "Senha atualizada!!!"
                    self.lb_msg['foreground'] = "green"
                else:
                    self.lb_msg['text'] = "Não foi possível alterar a senha do administrador!!!"
        except Exception as e:
            print(e)
