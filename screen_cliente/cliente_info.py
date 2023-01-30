import tkinter as tk
import ttkbootstrap as ttk
from functions.tk_center import tk_center

from functions.globals import *
from functions.functions import data_pt, data_us, data_mask

from classes.cl_info import *


class ClienteInfo(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 800, 500)
        self.geometry(geo)
        self.title("ADMIN - INFO PM")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        # AJUSTE PARA ELIMINAÇÃO DE ERRO
        self.bt_confirma = None
        self.bt_cancela = None

        # OBJETO CONTATO CRIADO PARA ARMAZENAR SELEÇÃO
        self.info_selecionado = Info()

        # INFO DO CLIENTE
        self.cliente = ttk.Frame(self)
        self.cliente.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.10)
        self.lcliente = ttk.Label(self.cliente, font=('', 14),
                                  text=f"Informações / Publicações\n"
                                       f"{cliente_global.graduacao_txt} "
                                       f"{cliente_global.re}-{cliente_global.dc} "
                                       f"{cliente_global.nome}")
        self.lcliente.pack()
        # PESQUISAS
        self.pesquisa = ttk.Frame(self)
        self.pesquisa.place(relx=0.01, rely=0.14, relwidth=0.98, relheight=0.10)
        self.lb_texto = ttk.Label(self.pesquisa, text='Pesquisar por texto: ')
        self.lb_texto.grid(row=0, column=0, sticky='w')
        self.texto = ttk.Entry(self.pesquisa, width=70, style='success')
        self.texto.grid(row=0, column=1, sticky='w')
        self.texto.bind('<KeyRelease>', (lambda event: self.busca_info(self.texto.get())))

        # TREEVIEW LISTA DE CONTATOS CADASTRADOS PARA O CLIENTE
        self.lista = ttk.Frame(self)
        self.lista.place(relx=0.01, rely=0.25, relwidth=0.56, relheight=0.50)

        self.colunas = ['re', 'data', 'descrição']
        self.largura = [60, 80, 280]
        ancora = ("center", "w", "w")
        i = 0
        self.t_info = ttk.Treeview(self.lista, columns=self.colunas, show='headings',
                                   height=10, selectmode='browse')
        for cols in self.colunas:
            self.t_info.column(cols, width=self.largura[i], anchor=ancora[i])
            i = i + 1
        for cols in self.colunas:
            self.t_info.heading(cols, text=cols.upper())
        self.t_info.grid(row=0, column=0)
        #   SCROOLBAR
        self.scrool = ttk.Scrollbar(self.lista, orient=tk.VERTICAL, command=self.t_info.yview)
        self.t_info.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=1, row=0, sticky='ns')

        # ATUALIZA A LISTA DE CONTATOS DO CLIENTE
        self.atualiza_t_info()
        self.t_info.bind('<<TreeviewSelect>>', self.seleciona_info)

        # FRAME DE EXCLUSÃO DO CONTATO
        self.exclusao = ttk.Frame(self, borderwidth=1, relief='solid')
        self.exclusao.place(relx=0.56, rely=0.25, relwidth=0.42, relheight=0.36)

        self.bt_delete = ttk.Button(self.exclusao, text="APAGAR REGISTRO SELECIONADO",
                                    style='danger', width=50, state='disabled', command=self.deletar)
        self.bt_delete.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        self.ldelete = ttk.Label(self.exclusao, text=' ')
        self.ldelete.grid(row=1, column=0, pady=5, columnspan=2)

        # FORMULÁRIO PARA CADASTRO DE NOVO CONTATO
        self.form = ttk.Frame(self)
        self.form.place(relx=0.01, rely=0.63, relwidth=0.98, relheight=0.35)
        self.lform = ttk.Label(self.form, text="NOVO REGISTRO", font=('', 12))
        self.lform.grid(row=1, column=0, sticky='w', pady=20)

        self.ldata_info = ttk.Label(self.form, text='Data')
        self.ldata_info.grid(row=2, column=0)
        self.data_info = ttk.DateEntry(self.form, style="Info")
        self.data_info.grid(row=3, column=0)
        self.data_info.entry.bind('<KeyRelease>', lambda event: data_mask(self.data_info, self.data_info.entry.get()))

        self.ldescricao = ttk.Label(self.form, text='Descrição')
        self.ldescricao.grid(row=2, column=1)
        self.descricao = ttk.Entry(self.form, width=60)
        self.descricao.grid(row=3, column=1, padx=20)

        self.bt_salvar = ttk.Button(self.form, text="SALVAR", style="success", command=self.salvar)
        self.bt_salvar.grid(row=3, column=2, padx=10)

        self.msg = ttk.Frame(self)
        self.msg.place(relx=0.01, rely=0.88, relwidth=0.98, relheight=0.1)
        self.lb_msg = ttk.Label(self.msg, text="", style="warning", font=('', 12))
        self.lb_msg.grid(row=4, column=1, padx=10)

    # FUNÇÕES
    # ATUALIZAR LISTA DE CONTATOS PARA O CLIENTE
    def atualiza_t_info(self):
        for registro in self.t_info.get_children():
            self.t_info.delete(registro)
        info = lista_info(cliente_global.re)
        for i in info:
            i = [i['re'], data_pt(i['data_info']), i['descricao']]
            self.t_info.insert('', tk.END, values=i)

    # SELECIONA INFO
    def seleciona_info(self, x):
        it = self.t_info.focus()
        dados = self.t_info.item(it)
        dados = dados.get('values')
        try:
            self.info_selecionado.set_info(dados[0])
            self.bt_delete['state'] = 'normal'
        except:
            pass

    # PESQUISA INFO
    def busca_info(self, texto):
        for registro in self.t_info.get_children():
            self.t_info.delete(registro)
        info = pesquisa_info_texto(cliente_global.re, texto)
        for i in info:
            i = [i['re'], data_pt(i['data_info']), i['descricao']]
            self.t_info.insert('', tk.END, values=i)

    # SALVA NOVO INFO
    def salvar(self):
        dados = [self.data_info.entry.get(), self.descricao.get().upper()]
        if "" in dados:
            self.lb_msg['text'] = "A Descrição deve ser preenchida!!!"
        else:
            info = Info()
            info.re = cliente_global.re
            info.data_info = str(data_us(self.data_info.entry.get()))
            info.descricao = self.descricao.get().upper()
            info.insert_info()
            self.descricao.delete(0, 'end')
            self.atualiza_t_info()
            self.lb_msg['text'] = "Registro Salvo!"

    def deletar(self):
        self.ldelete['text'] = "CONFIRMA EXCLUSÃO DO REGISTRO?"
        self.bt_confirma = ttk.Button(self.exclusao, text='CONFIRMAR', style='warning', width=18,
                                      command=(lambda: self.exclusao_confirmada(True)))
        self.bt_confirma.grid(row=2, column=0, pady=5)
        self.bt_cancela = ttk.Button(self.exclusao, text='CANCELA', style='info', width=18,
                                     command=(lambda: self.exclusao_confirmada(False)))
        self.bt_cancela.grid(row=2, column=1, pady=5)

    def exclusao_confirmada(self, b):
        if b:
            self.info_selecionado.delete_info()
            self.atualiza_t_info()
            self.ldelete['text'] = 'Exclusão confirmada!'
            self.bt_confirma.destroy()
            self.bt_cancela.destroy()
            self.bt_delete['state'] = 'disabled'
            self.lb_msg['text'] = ''
        else:
            self.ldelete['text'] = 'Exclusão cancelada!'
            self.bt_confirma.destroy()
            self.bt_cancela.destroy()
            self.lb_msg['text'] = ''
