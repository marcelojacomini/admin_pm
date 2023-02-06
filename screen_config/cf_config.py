import tkinter as tk
from os import path

import ttkbootstrap as ttk

from functions.tk_center import tk_center


class Configuracoes(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 880, 650)
        self.geometry(geo)
        self.title("ADMIN - CONFIGURAÇÕES")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        header = ttk.Frame(self)
        header.pack(fill='x', padx=10)
        lb_header = ttk.Label(header, text='Configurações', font=('', 16, 'bold'))
        lb_header.grid(row=0, column=0, pady=5)

        fr_server = ttk.Frame(self)
        fr_server.pack(fill='x', padx=10, ipadx=3, pady=5)

        lb_host = ttk.Label(fr_server, text='Host (endereço do servidor):', width=30, anchor='e')
        lb_host.grid(row=0, column=0, sticky='w', padx=3, pady=5)
        self.server_host = ttk.Entry(fr_server)
        self.server_host.grid(row=0, column=1, sticky='w', padx=3, pady=5)

        lb_user_host = ttk.Label(fr_server, text='Usuário do Servidor:', width=30, anchor='e')
        lb_user_host.grid(row=1, column=0, sticky='e', padx=3, pady=5)
        self.user_host = ttk.Entry(fr_server)
        self.user_host.grid(row=1, column=1, sticky='w', padx=3, pady=5)

        lb_pass_host = ttk.Label(fr_server, text='Senha: ', width=30, anchor='e')
        lb_pass_host.grid(row=2, column=0, sticky='e', padx=3, pady=5)
        self.pass_host = ttk.Entry(fr_server, show='*')
        self.pass_host.grid(row=2, column=1, sticky='w', padx=3, pady=5)
        view_pass = ttk.Button(fr_server, text='View Pass', command=self.ver_pass)
        view_pass.grid(row=2, column=2, padx=3, pady=5)

        lb_data_base_name = ttk.Label(fr_server, text='Nome do Banco de Dados:', width=30, anchor='e')
        lb_data_base_name.grid(row=3, column=0, sticky='e', padx=3, pady=5)
        self.data_base_name = ttk.Entry(fr_server)
        self.data_base_name.grid(row=3, column=1, sticky='w', padx=3, pady=5)

    def atualizar_host(self):
        # LOCAL DA PASTA C:\USERS\'NOME DO USER'
        pasta_user = path.join(path.expanduser("~"))
        with open(f'{pasta_user}\\conf_admin_pm\\config.conf', 'w') as cofigurarLocal:
            cofigurarLocal.write(self.server_host.get())

    def ver_pass(self):
        if self.pass_host['show'] == '*':
            self.pass_host['show'] = ''
        else:
            self.pass_host['show'] = '*'
