import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import DateEntry
from functions.tk_center import tk_center
from functions.functions import data_pt, data_us, data_mask
from functions.globals import cliente_global
from relatorios.rel_saldo_bh import *


class BancoHorasGeral(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 900, 800)
        self.geometry(geo)
        self.title("ADMIN - BANCO DE HORAS")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        self.header = ttk.Frame(self)
        self.header.place(relx=0.02, rely=0.02, relwidth=0.9, relheight=0.08)
        self.lb_header = ttk.Label(self.header, text='CONTROLE DE BANCO DE HORAS', font=('', 16, 'bold'))
        self.lb_header.grid(row=0, column=0)

        style = ttk.Style()
        style.configure("Linha.Treeview", rowheight=18)

        ###################################################################################################
        # lista de saldos
        ###################################################################################################
        self.lista_saldo = ttk.Frame(self)
        self.lista_saldo.place(relx=0.02, rely=0.08, relwidth=0.40, relheight=0.65)

        colunas_saldo = ['grad', 're', 'nome', 'saldo']
        largura_saldo = [80, 70, 100, 70]
        ancora = ["w", "center", "w", "center"]
        i = 0
        self.t_saldo = ttk.Treeview(self.lista_saldo, columns=colunas_saldo, show='headings',
                                    height=25, selectmode='browse', style='Linha.Treeview')
        for coluna in colunas_saldo:
            self.t_saldo.column(coluna, width=largura_saldo[i], anchor=ancora[i])
            i = i + 1
        for coluna in colunas_saldo:
            self.t_saldo.heading(coluna, text=coluna.upper())
        self.t_saldo.grid(row=0, column=0)
        self.t_saldo.bind('<<TreeviewSelect>>', self.seleciona_cliente)
        # SCROOLBAR DA TREEVIEW
        self.scrool = ttk.Scrollbar(self.lista_saldo, orient=tk.VERTICAL, command=self.t_saldo.yview)
        self.t_saldo.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=1, row=0, sticky='ns')
        # PREENCHE LISTA DE SALDOS
        self.atualiza_t_saldo()

        self.t_saldo.tag_configure('excedente', foreground='#FF0000', font=('', 9, 'bold'))
        self.t_saldo.tag_configure('alerta', foreground='#D2691E', font=('', 9, 'bold'))
        self.t_saldo.tag_configure('normal', foreground='#006400', font=('', 9, 'bold'))

        ###################################################################################################
        # extrato individual
        ###################################################################################################
        self.extrato = ttk.Frame(self)
        self.extrato.place(relx=0.42, rely=0.08, relwidth=0.56, relheight=0.65)

        colunas_ext = ['data', 'horas', 'motivo']
        largura_ext = [100, 100, 275]
        ancora_ext = ["center", "center", "w"]
        i = 0
        self.t_ext = ttk.Treeview(self.extrato, columns=colunas_ext, show='headings',
                                  height=31, selectmode='none')
        for coluna in colunas_ext:
            self.t_ext.column(coluna, width=largura_ext[i], anchor=ancora_ext[i])
            i = i + 1
        for coluna in colunas_ext:
            self.t_ext.heading(coluna, text=coluna.upper())
        self.t_ext.grid(row=0, column=0)
        # self.t_ext.bind('<<TreeviewSelect>>', self.seleciona_ext)
        # SCROOLBAR DA TREEVIEW
        self.scrool_ext = ttk.Scrollbar(self.extrato, orient=tk.VERTICAL, command=self.t_ext.yview)
        self.t_ext.configure(yscrollcommand=self.scrool_ext.set)
        self.scrool_ext.grid(column=1, row=0, sticky='ns')

        self.t_ext.tag_configure('negativo', foreground='#FF0000', font=('', 9, 'bold'))
        # self.t_ext.tag_configure('alerta', foreground='#D2691E', font=('', 9, 'bold'))
        self.t_ext.tag_configure('normal', foreground='#006400', font=('', 9, 'bold'))

        ###################################################################################################
        # formulário
        ###################################################################################################
        self.form = ttk.Frame(self)
        self.form.place(relx=0.02, rely=0.72, relwidth=0.96, relheight=0.25)

        self.lb_selecionado = ttk.Label(self.form, text='', font=('Arial', 14, 'bold'))
        self.lb_selecionado.grid(row=0, column=0, columnspan=4, sticky='w')

        self.lb_data = ttk.Label(self.form, text='Data', font=('', 10, 'bold'))
        self.lb_data.grid(row=1, column=0, sticky='w')
        self.data = DateEntry(self.form)
        self.data.grid(row=2, column=0, pady=5)
        self.data.entry.bind('<KeyRelease>', lambda event: data_mask(self.data, self.data.entry.get()))

        self.lb_hora = ttk.Label(self.form, text='Horas', font=('', 10, 'bold'))
        self.lb_hora.grid(row=1, column=1, padx=10, sticky='w')
        self.hora = ttk.Entry(self.form, width=10)
        self.hora.grid(row=2, column=1, pady=5, padx=10)

        self.lb_motivo = ttk.Label(self.form, text='Motivo', font=('', 10, 'bold'))
        self.lb_motivo.grid(row=1, column=2, sticky='w')
        self.motivo = ttk.Entry(self.form, width=60)
        self.motivo.grid(row=2, column=2, pady=5)

        self.bt_salva = ttk.Button(self.form, text='ADICIONAR / DESCONTAR', style='warning',
                                   state='disabled', command=self.salva_horas)
        self.bt_salva.grid(row=2, column=3, padx=10)

        self.lb_msg = ttk.Label(self.form, text='', font=('Arial', 12, 'bold'), style='secondary')
        self.lb_msg.grid(row=3, column=0, columnspan=4, pady=10, sticky='w')

    def atualiza_t_saldo(self):
        for cliente in self.t_saldo.get_children():
            self.t_saldo.delete(cliente)
        saldos_clientes = relatorio_saldo_bh()
        saldos_clientes = saldos_clientes.values.tolist()
        for i in saldos_clientes:
            if i[3] >= 12:
                self.t_saldo.insert('', tk.END, values=i, tags='excedente')
            elif 12 > i[3] >= 8:
                self.t_saldo.insert('', tk.END, values=i, tags='alerta')
            elif i[3] < 8:
                self.t_saldo.insert('', tk.END, values=i, tags='normal')

    def seleciona_cliente(self, x):
        try:
            it = self.t_saldo.focus()
            dados = self.t_saldo.item(it)
            dados = dados.get('values')
            cliente_global.set_cliente(dados[1][:6])
            self.atualiza_t_ext()
            self.lb_selecionado['text'] = cliente_global.nome
            self.bt_salva['state'] = 'normal'
            self.lb_msg['text'] = ''
        except IndexError:
            print('')

    def atualiza_t_ext(self):
        for ex in self.t_ext.get_children():
            self.t_ext.delete(ex)
        extrato_individual = extrato_horas(cliente_global.re)
        for i in extrato_individual:
            dados = [data_pt(i['data']), i['hora'], i['motivo']]
            if dados[1] < 0:
                self.t_ext.insert('', tk.END, values=dados, tags='negativo')
            else:
                self.t_ext.insert('', tk.END, values=dados, tags='normal')

    def salva_horas(self):
        dados = BancoHoras()
        dados.cria_banco(cliente_global.re, data_us(self.data.entry.get()), self.hora.get(), self.motivo.get().upper())
        if dados.hora == '' or dados.motivo == '':
            self.lb_msg['text'] = "Dados não podem ficar em branco (vazios)"
        else:
            if dados.insert_banco():
                self.lb_msg['foreground'] = 'green'
                self.lb_msg['text'] = f"Alterado saldo em {dados.hora} hora(s) para {self.lb_selecionado['text']}"
                self.atualiza_t_saldo()
                self.atualiza_t_ext()
                self.bt_salva['state'] = 'disabled'
                self.hora.delete(0, 'end')
                self.motivo.delete(0, 'end')
            else:
                self.lb_msg['foreground'] = 'red'
                self.lb_msg['text'] = "Houve um erro ao salvar os dados!!!"
