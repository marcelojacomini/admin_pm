import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import DateEntry

from functions.tk_center import tk_center
from data_base.data_base import Con

from classes_transito.tr_logradouros import *


class TransitoCadastro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 800, 700)
        self.geometry(geo)
        self.title("ADMIN Trânsito - NOVO AUTO DE INFRAÇÃO")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        ##############################################################################################################
        # VARIÁVEIS DE INICIALIZAÇÃO
        ##############################################################################################################
        self.talao_select = tk.StringVar(self, "Municipio")

        ##############################################################################################################
        # FORMULÁRIO DE CADASTRO DE AIT
        ##############################################################################################################
        self.header = ttk.Frame(self)
        self.header.pack(fill='x', padx=20, pady=20)
        self.lb_header = ttk.Label(self.header, text="CADASTRAR AUTO DE INFRAÇÃO", font=('', 14, 'bold'))
        self.lb_header.pack()

        self.linha1 = ttk.Frame(self)
        self.linha1.pack(fill='x', padx=20)
        self.lb_talao = ttk.Label(self.linha1, text="Informe o talão: ", font=('', 10, 'bold'))
        self.lb_talao.grid(column=0, row=0)

        self.municipal = ttk.Radiobutton(self.linha1, text="Municipal   | ", value="Municipio",
                                         variable=self.talao_select)
        self.municipal.grid(row=0, column=1, pady=5, padx=5)
        self.estadual = ttk.Radiobutton(self.linha1, text="Estadual", value="Estado",
                                        variable=self.talao_select)
        self.estadual.grid(row=0, column=2, pady=5, padx=5)

        self.linha2 = ttk.Frame(self)
        self.linha2.pack(fill='x', padx=20, pady=15)
        self.lb_ait = ttk.Label(self.linha2, text="Nº AIT", font=('', 10, 'bold'))
        self.lb_ait.grid(row=0, column=0, sticky='w')
        self.ait = ttk.Entry(self.linha2, width=12, style="success")
        self.ait.grid(row=1, column=0)

        self.lb_condutor = ttk.Label(self.linha2, text="CONDUTOR", font=('', 10, 'bold'))
        self.lb_condutor.grid(row=0, column=1, sticky='w', padx=15)
        self.condutor = ttk.Entry(self.linha2, width=35)
        self.condutor.grid(row=1, column=1, padx=15)

        self.lb_local = ttk.Label(self.linha2, text="LOCAL", font=('', 10, 'bold'))
        self.lb_local.grid(row=0, column=2, sticky='w')
        self.local = ttk.Entry(self.linha2, width=45)
        self.local.grid(row=1, column=2)

        self.linha3 = ttk.Frame(self)
        self.linha3.pack(fill='x', padx=20)

        self.linha4 = ttk.Frame(self)
        self.linha4.pack(fill='x', padx=20)

        self.linha5 = ttk.Frame(self)
        self.linha5.pack(fill='x', padx=20)

        ##############################################################################################################
        # BIND
        ##############################################################################################################
        self.local.bind('<KeyRelease>', (lambda event: preenche_logradouro(self.local, self.local.get())))
