from imports import *
from classes.cl_cliente import *

from functions.functions import re_mask, dc_mask, data_mask, data_us, data_pt


class ClienteEdita(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        self.geometry(tk_center(self, 500, 450))
        self.title("ADMIN - EDITA PM")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        self.header = ttk.Frame(self)
        self.header.pack(pady=15)
        self.lheader = ttk.Label(self.header, text='EDITAR PM', font=("", 20))
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
        self.graduacao.grid(row=1, column=3, sticky='w', padx=5)

        self.linha3 = ttk.Frame(self)
        self.linha3.pack(fill='x', pady=15, padx=15)
        self.ltarja = ttk.Label(self.linha3, text='NOME DE GUERRA')
        self.ltarja.grid(row=0, column=0, sticky='w', padx=5)
        self.tarja = ttk.Entry(self.linha3, width=25)
        self.tarja.grid(row=1, column=0, sticky='w', padx=5)
        self.lativo = ttk.Label(self.linha3, text='NOME DE GUERRA')
        self.lativo.grid(row=0, column=1, sticky='w', padx=5)
        self.ativo = ttk.Combobox(self.linha3, values=['ATIVO', 'INATIVO'], state='readonly')
        self.ativo.grid(row=1, column=1, sticky='w', padx=5)

        self.linha4 = ttk.Frame(self)
        self.linha4.pack(fill='x', pady=15, padx=15)
        self.bt_salvar = ttk.Button(self.linha4, text="SALVAR ALTERAÇÕES", style='warning', command=self.salvar)
        self.bt_salvar.pack(fill='x')

        self.linha5 = ttk.Frame(self)
        self.linha5.pack(fill='x', pady=15, padx=15)
        self.lb_msg = ttk.Label(self.linha5, text="")
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
        self.preenche_form()

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
            self.lb_msg['text'] = "Dados não podem ficar em branco!"
        else:
            grava = edita_cliente(CLIENTE.id,
                                  self.re.get(),
                                  self.dc.get().upper(),
                                  self.nome.get().upper(),
                                  self.tarja.get().upper(),
                                  indice_grad(self.graduacao.get()),
                                  self.graduacao.get(),
                                  data_us(self.admissao.entry.get()),
                                  data_us(self.promocao.entry.get()),
                                  self.ativo.get()
                                  )
            if grava:
                self.destroy()
            else:
                self.lb_msg['text'] = "Houve um erro ao gravar os dados!"

    def preenche_form(self):
        self.re.insert(0, CLIENTE.re)
        self.dc.insert(0, CLIENTE.dc)
        self.nome.insert(0, CLIENTE.nome)
        self.admissao.entry.delete(0, 'end')
        self.admissao.entry.insert(0, data_pt(CLIENTE.admissao))
        self.promocao.entry.delete(0, 'end')
        self.promocao.entry.insert(0, data_pt(CLIENTE.promocao))
        self.graduacao.set(CLIENTE.graduacao_txt)
        self.tarja.insert(0, CLIENTE.tarja)
        self.ativo.set(CLIENTE.ativo.upper())
