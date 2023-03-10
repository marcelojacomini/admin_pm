from imports import *

from functions.functions import data_mask, data_pt, data_us

from relatorios.rel_saldo_bh import *


class BancoHorasGeral(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 880, 650)
        self.geometry(geo)
        self.title("ADMIN - BANCO DE HORAS")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        self.header = ttk.Frame(self)
        self.header.pack(fill='x', padx=10)
        self.lb_header = ttk.Label(self.header, text='CONTROLE DE BANCO DE HORAS', font=('', 16, 'bold'))
        self.lb_header.grid(row=0, column=0, pady=5)

        linha = ttk.Frame(self, borderwidth=4, relief='solid')
        linha.pack(fill='x')

        ###################################################################################################
        # formulário
        ###################################################################################################
        self.form = ttk.Frame(self)
        self.form.pack(fill='x', padx=10)

        self.lb_data = ttk.Label(self.form, text='Data', font=('', 10, 'bold'))
        self.lb_data.grid(row=0, column=0, sticky='w')
        self.data = DateEntry(self.form)
        self.data.grid(row=1, column=0, pady=5)
        self.data.entry.bind('<KeyRelease>', lambda event: data_mask(self.data, self.data.entry.get()))
        self.lb_hora = ttk.Label(self.form, text='Horas', font=('', 10, 'bold'))
        self.lb_hora.grid(row=0, column=1, padx=10, sticky='w')
        self.hora = ttk.Entry(self.form, width=10)
        self.hora.grid(row=1, column=1, pady=5, padx=10)

        self.lb_motivo = ttk.Label(self.form, text='Motivo', font=('', 10, 'bold'))
        self.lb_motivo.grid(row=0, column=2, sticky='w')
        self.motivo = ttk.Entry(self.form, width=60)
        self.motivo.grid(row=1, column=2, pady=5)

        self.bt_salva = ttk.Button(self.form, text='ADICIONAR / DESCONTAR', style='warning',
                                   state='disabled', command=self.salva_horas)
        self.bt_salva.grid(row=1, column=3, padx=10)

        self.lb_selecionado = ttk.Label(self.form, text='', font=('Arial', 14, 'bold'))
        self.lb_selecionado.grid(row=2, column=0, columnspan=4, sticky='w')

        self.lb_msg = ttk.Label(self.form, text='', font=('Arial', 12, 'bold'))
        self.lb_msg.grid(row=3, column=0, columnspan=4, sticky='w')

        ###################################################################################################
        # lista de saldos
        ###################################################################################################
        self.lista_saldo = ttk.Frame(self)
        self.lista_saldo.pack(fill='x', padx=10)

        colunas_saldo = ['grad', 're', 'nome', 'saldo']
        largura_saldo = [80, 70, 100, 70]
        ancora = ["w", "center", "w", "center"]
        i = 0
        self.t_saldo = ttk.Treeview(self.lista_saldo, columns=colunas_saldo, show='headings',
                                    height=30, selectmode='browse')
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
        self.scrool.grid(row=0, column=1, sticky='ns')
        # PREENCHE LISTA DE SALDOS
        self.atualiza_t_saldo()

        self.t_saldo.tag_configure('excedente', foreground='red', font=('', 9, 'bold'))
        self.t_saldo.tag_configure('alerta', foreground='#FFD700', font=('', 9, 'bold'))
        self.t_saldo.tag_configure('normal', foreground='#E0FFFF', font=('', 9, 'bold'))

        separador = ttk.Label(self.lista_saldo, text='')
        separador.grid(row=0, column=2, padx=5)

        ###################################################################################################
        # extrato individual
        ###################################################################################################
        colunas_ext = ['data', 'horas', 'motivo']
        largura_ext = [100, 100, 275]
        ancora_ext = ["center", "center", "w"]
        i = 0
        self.t_ext = ttk.Treeview(self.lista_saldo, columns=colunas_ext, show='headings',
                                  height=30, selectmode='none')
        for coluna in colunas_ext:
            self.t_ext.column(coluna, width=largura_ext[i], anchor=ancora_ext[i])
            i = i + 1
        for coluna in colunas_ext:
            self.t_ext.heading(coluna, text=coluna.upper())
        self.t_ext.grid(row=0, column=3)
        # self.t_ext.bind('<<TreeviewSelect>>', self.seleciona_ext)
        # SCROOLBAR DA TREEVIEW
        self.scrool_ext = ttk.Scrollbar(self.lista_saldo, orient=tk.VERTICAL, command=self.t_ext.yview)
        self.t_ext.configure(yscrollcommand=self.scrool_ext.set)
        self.scrool_ext.grid(row=0, column=4, sticky='ns')

        self.t_ext.tag_configure('negativo', foreground='red', font=('', 9, 'bold'))
        self.t_ext.tag_configure('normal', foreground='#E0FFFF', font=('', 9, 'bold'))

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
            CLIENTE.set_cliente(dados[1][:6])
            self.atualiza_t_ext()
            self.lb_selecionado['text'] = CLIENTE.nome
            self.bt_salva['state'] = 'normal'
            self.lb_msg['text'] = ''
        except Exception as e:
            print(e, x)

    def atualiza_t_ext(self):
        for ex in self.t_ext.get_children():
            self.t_ext.delete(ex)
        extrato_individual = extrato_horas(CLIENTE.re)
        for i in extrato_individual:
            dados = [data_pt(i['data']), i['hora'], i['motivo']]
            if dados[1] < 0:
                self.t_ext.insert('', tk.END, values=dados, tags='negativo')
            else:
                self.t_ext.insert('', tk.END, values=dados, tags='normal')

    def salva_horas(self):
        dados = BancoHoras()
        dados.cria_banco(CLIENTE.re, data_us(self.data.entry.get()), self.hora.get(), self.motivo.get().upper())
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
