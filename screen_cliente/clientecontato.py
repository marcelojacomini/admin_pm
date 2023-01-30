import tkinter as tk
import ttkbootstrap as ttk
from functions.tk_center import tk_center

from functions.globals import *
from functions.functions import contato_mask, format_telefone

from classes.cl_contato import *


class ClienteContato(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 800, 450)
        self.geometry(geo)
        self.title("ADMIN - CONTATO PM")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        # AJUSTE PARA ELIMINAÇÃO DE ERRO
        self.bt_confirma = None
        self.bt_cancela = None

        # OBJETO CONTATO CRIADO PARA ARMAZENAR SELEÇÃO
        self.contato_selecionado = Contato()

        # INFO DO CLIENTE
        self.cliente = ttk.Frame(self)
        self.cliente.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.10)
        self.lcliente = ttk.Label(self.cliente, font=('', 14),
                                  text=f"Contatos de "
                                       f"{cliente_global.graduacao_txt} "
                                       f"{cliente_global.re}-{cliente_global.dc} "
                                       f"{cliente_global.nome}")
        self.lcliente.pack()

        # TREEVIEW LISTA DE CONTATOS CADASTRADOS PARA O CLIENTE
        self.lista = ttk.Frame(self)
        self.lista.place(relx=0.01, rely=0.12, relwidth=0.56, relheight=0.50)

        self.colunas = ['re', 'tipo', 'contato']
        self.largura = [60, 105, 255]
        ancora = ("center", "w", "w")
        i = 0
        self.t_contatos = ttk.Treeview(self.lista, columns=self.colunas, show='headings',
                                       height=10, selectmode='browse')
        for cols in self.colunas:
            self.t_contatos.column(cols, width=self.largura[i], anchor=ancora[i])
            i = i + 1
        for cols in self.colunas:
            self.t_contatos.heading(cols, text=cols.upper())
        self.t_contatos.grid(row=0, column=0)
        #   SCROOLBAR
        self.scrool = ttk.Scrollbar(self.lista, orient=tk.VERTICAL, command=self.t_contatos.yview)
        self.t_contatos.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=1, row=0, sticky='ns')

        # ATUALIZA A LISTA DE CONTATOS DO CLIENTE
        self.atualiza_t_contato()
        self.t_contatos.bind('<<TreeviewSelect>>', self.seleciona_contato)

        # FRAME DE EXCLUSÃO DO CONTATO
        self.exclusao = ttk.Frame(self, borderwidth=1, relief='solid')
        self.exclusao.place(relx=0.56, rely=0.12, relwidth=0.42, relheight=0.40)

        self.bt_delete = ttk.Button(self.exclusao, text="APAGAR CONTATO SELECIONADO",
                                    style='danger', width=50, state='disabled', command=self.deletar)
        self.bt_delete.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        self.ldelete = ttk.Label(self.exclusao, text=' ')
        self.ldelete.grid(row=1, column=0, pady=5, columnspan=2)

        # FORMULÁRIO PARA CADASTRO DE NOVO CONTATO
        self.form = ttk.Frame(self)
        self.form.place(relx=0.01, rely=0.55, relwidth=0.98, relheight=0.35)
        self.lform = ttk.Label(self.form, text="NOVO CONTATO", font=('', 12))
        self.lform.grid(row=1, column=0, sticky='w', pady=20)

        self.ltipo = ttk.Label(self.form, text='Tipo de Contato')
        self.ltipo.grid(row=2, column=0)
        self.tipo = ttk.Combobox(self.form, values=tipos_contato, state='readonly', font=('', 12))
        self.tipo.set('1-Telefone')
        self.tipo.grid(row=3, column=0)

        self.lcontato = ttk.Label(self.form, text='Contato')
        self.lcontato.grid(row=2, column=1)
        self.contato = ttk.Entry(self.form, width=60)
        self.contato.grid(row=3, column=1, padx=20)
        self.contato.bind('<KeyRelease>', lambda event: contato_mask(self.tipo.get(), self.contato, self.contato.get()))
        self.contato.bind('<FocusOut>', lambda event: format_telefone(self.tipo.get(),
                                                                      self.contato,
                                                                      self.contato.get()))

        self.bt_salvar = ttk.Button(self.form, text="SALVAR", style="success", command=self.salvar)
        self.bt_salvar.grid(row=3, column=2, padx=10)

    # FUNÇÕES
    # ATUALIZAR LISTA DE CONTATOS PARA O CLIENTE
    def atualiza_t_contato(self):
        for ct in self.t_contatos.get_children():
            self.t_contatos.delete(ct)
        contatos = lista_contatos(cliente_global.re)
        for i in contatos:
            i = [i['re'], i['tipo'], i['contato']]
            self.t_contatos.insert('', tk.END, values=i)

    # SELECIONA CONTATO
    def seleciona_contato(self, x):
        it = self.t_contatos.focus()
        dados = self.t_contatos.item(it)
        dados = dados.get('values')
        self.contato_selecionado.re = str(dados[0])
        self.contato_selecionado.tipo = dados[1]
        self.contato_selecionado.contato = dados[2]
        self.bt_delete['state'] = 'normal'


    # SALVA NOVO CONTATO
    def salvar(self):
        dados = [self.tipo.get(), self.contato.get().lower()]
        if "" in dados:
            print("O Contato deve ser preenchido")
        elif self.tipo.get() == 'Telefone' and len(self.contato.get()) < 8:
            print("Erro no telefone")
        else:
            print('pass')
        ct = Contato()
        ct.re = cliente_global.re
        ct.tipo = self.tipo.get()
        ct.contato = self.contato.get()
        ct.insert_contato()
        self.contato.delete(0, 'end')
        self.atualiza_t_contato()

    def deletar(self):
        self.ldelete['text'] = "CONFIRMA EXCLUSÃO DO CONTATO?"
        self.bt_confirma = ttk.Button(self.exclusao, text='CONFIRMAR', style='warning', width=18,
                                      command=(lambda: self.exclusao_confirmada(True)))
        self.bt_confirma.grid(row=2, column=0, pady=5)
        self.bt_cancela = ttk.Button(self.exclusao, text='CANCELA', style='info', width=18,
                                     command=(lambda: self.exclusao_confirmada(False)))
        self.bt_cancela.grid(row=2, column=1, pady=5)
        '''
        if confirma:
            '''

    def exclusao_confirmada(self, b):
        if b:
            delete_contato(self.contato_selecionado.contato)
            self.atualiza_t_contato()
            self.ldelete['text'] = 'Exclusão confirmada!'
            self.bt_confirma.destroy()
            self.bt_cancela.destroy()
        else:
            self.ldelete['text'] = 'Exclusão cancelada!'
            self.bt_confirma.destroy()
            self.bt_cancela.destroy()
