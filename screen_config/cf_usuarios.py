from imports import *
from data_base.data_base import *
from classes.cl_cliente import *
PASTA_USER = path.join(path.expanduser("~"))


class Usuarios(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        self.geometry(tk_center(self, 880, 650))
        self.title("ADMIN - USUÁRIOS")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        # HEADER
        header = ttk.Frame(self)
        header.pack(fill='x', padx=10)
        lb_header = ttk.Label(header, text='Configurações - USUÁRIOS', font=('', 16, 'bold'))
        lb_header.grid(row=0, column=0, pady=5)

        fr_1 = ttk.Frame(self, borderwidth=1, relief='solid')
        fr_1.pack(padx=30, pady=30, fill='x')

        # USER
        fr_user = ttk.Frame(fr_1)
        fr_user.pack(fill='x', padx=10, pady=15)

        lb_form = ttk.Label(fr_user, text='AUTORIZAR USUÁRIO PARA USO DO SISTEMA')
        lb_form.grid(row=0, column=0, sticky='w', padx=10, pady=10, columnspan=3)

        lb_nome = ttk.Label(fr_user, text='Usuário: ', width=30, anchor='e')
        lb_nome.grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.usuario = ttk.Combobox(fr_user, values=lista_tarjas())
        self.usuario.grid(row=1, column=1, sticky='w', padx=3, pady=5)

        bt_salvar = ttk.Button(fr_user, text='Salvar', command=self.salvar)
        bt_salvar.grid(row=1, column=2, sticky='we', padx=15)

        ##########################################################################################################
        #
        fr_2 = ttk.Frame(self, borderwidth=1, relief='solid')
        fr_2.pack(padx=30, fill='x')

        fr_admin = ttk.Frame(fr_2)
        fr_admin.pack(fill='x', padx=10, pady=15)

        # MENSAGEM
        self.lb_msg = ttk.Label(self, text='', font=('', 12, 'bold'), foreground='red')
        self.lb_msg.pack(side='bottom', fill='x', pady=25, padx=25)

    def salvar(self):
        pass
