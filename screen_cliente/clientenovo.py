import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import DateEntry

from functions.tk_center import tk_center
from functions.globals import *
from functions.functions import *
from classes.cl_cliente import *


class ClienteNovo(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 500, 450)
        self.geometry(geo)
        self.title("ADMIN - NOVO PM")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        self.header = ttk.Frame(self)
        self.header.pack(pady=15)
        self.lheader = ttk.Label(self.header, text='CADASTRAR NOVO PM', font=("", 20))
        self.lheader.grid()
        self.lheader2 = ttk.Label(self.header, text='DADOS FUNCIONAIS', font=("", 14))
        self.lheader2.grid()

        self.linha1 = ttk.Frame(self)
        self.linha1.pack(fill='x', pady=15, padx=15)
        self.lre = ttk.Label(self.linha1, text='RE')
        self.lre.grid(row=0, column=0, sticky='w', padx=5)
        self.re = ttk.Entry(self.linha1, width=8)
        self.re.grid(row=1, column=0, sticky='w', padx=5)
        self.ldc = ttk.Label(self.linha1, text='DC')
        self.ldc.grid(row=0, column=1, sticky='w', padx=5)
        self.dc = ttk.Entry(self.linha1, width=2)
        self.dc.grid(row=1, column=1, sticky='w', padx=5)
        self.lnome = ttk.Label(self.linha1, text='NOME')
        self.lnome.grid(row=0, column=2, sticky='w', padx=5)
        self.nome = ttk.Entry(self.linha1, width=50)
        self.nome.grid(row=1, column=2, sticky='w', padx=5)

        self.linha2 = ttk.Frame(self)
        self.linha2.pack(fill='x', pady=15, padx=15)
        self.ladmissao = ttk.Label(self.linha2, text='DATA ADMISSÃO')
        self.ladmissao.grid(row=0, column=0, sticky='w', padx=5)
        self.admissao = DateEntry(self.linha2, width=12)
        self.admissao.grid(row=1, column=0, sticky='w', padx=5)
        self.lpromocao = ttk.Label(self.linha2, text='DATA PROMOÇÃO')
        self.lpromocao.grid(row=0, column=1, sticky='w', padx=5)
        self.promocao = DateEntry(self.linha2, width=12)
        self.promocao.grid(row=1, column=1, sticky='w', padx=5)
        self.lgraduacao = ttk.Label(self.linha2, text='POSTO/GRADUAÇÃO')
        self.lgraduacao.grid(row=0, column=3, sticky='w', padx=5)
        self.graduacao = ttk.Combobox(self.linha2, values=list_grad, state='readonly')
        self.graduacao.set("SD PM")
        self.graduacao.grid(row=1, column=3, sticky='w', padx=5)

        self.linha3 = ttk.Frame(self)
        self.linha3.pack(fill='x', pady=15, padx=15)
        self.ltarja = ttk.Label(self.linha3, text='NOME DE GUERRA')
        self.ltarja.grid(row=0, column=0, sticky='w', padx=5)
        self.tarja = ttk.Entry(self.linha3, width=25)
        self.tarja.grid(row=1, column=0, sticky='w', padx=5)

        self.linha4 = ttk.Frame(self)
        self.linha4.pack(fill='x', pady=15, padx=15)
        self.bt_salvar = ttk.Button(self.linha4, text="SALVAR", style='success', command=self.salvar)
        self.bt_salvar.pack(fill='x')

        self.linha5 = ttk.Frame(self)
        self.linha5.pack(fill='x', padx=10)
        self.lb_msg = ttk.Label(self.linha5, text='')
        self.lb_msg.pack()

        ###################################################################################################
        # BIND
        ###################################################################################################
        self.re.bind("<KeyRelease>", (lambda event: re_mask(self.re, self.re.get())))
        self.re.bind("<FocusOut>", lambda event: verifica_re(self.re, self.re.get()))
        self.dc.bind("<KeyRelease>", (lambda event: dc_mask(self.dc, self.dc.get())))
        self.admissao.entry.bind("<KeyRelease>", (lambda event: data_mask(self.admissao, self.admissao.entry.get())))
        self.promocao.entry.bind("<KeyRelease>", (lambda event: data_mask(self.promocao, self.promocao.entry.get())))
        ###################################################################################################

    def salvar(self):
        dados = [self.re.get(),
                 self.dc.get().upper(),
                 self.nome.get().upper(),
                 self.tarja.get().upper(),
                 indice_grad(self.graduacao.get()),
                 self.graduacao.get(),
                 data_us(self.admissao.entry.get()),
                 data_us(self.promocao.entry.get())
                 ]
        if "" in dados:
            self.lb_msg['text'] = "Erro!", "Existem dados em branco"
        else:
            grava = insert_cliente(self.re.get(),
                                   self.dc.get().upper(),
                                   self.nome.get().upper(),
                                   self.tarja.get().upper(),
                                   indice_grad(self.graduacao.get()),
                                   self.graduacao.get(),
                                   data_us(self.admissao.entry.get()),
                                   data_us(self.promocao.entry.get())
                                   )
            if grava:
                self.destroy()
            else:
                self.lb_msg['text'] = "Erro", "Houve um erro ao gravar os dados!"
