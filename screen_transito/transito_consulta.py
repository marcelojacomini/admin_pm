from imports import *
from screen_transito.transito_edicao import *


class TransitoConsulta(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 850, 650)
        self.geometry(geo)
        self.title("ADMIN Trânsito - CONSULTAS")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        #############################################################################################################
        # VARIAVEIS
        self.pesquisa_select = tk.StringVar(self, "Todos")
        self.ait_select = None

        #############################################################################################################
        header = ttk.Frame(self)
        header.pack(fill='x', pady=10)
        lb_header = ttk.Label(header, text="CONSULTAS", font=('', 12, 'bold'))
        lb_header.pack(anchor='w', padx=15)

        #############################################################################################################
        fr_options = ttk.Frame(self)
        fr_options.pack(fill='x', pady=10)
        # radio button
        self.todos = ttk.Radiobutton(fr_options, text="Todos", value="Todos", variable=self.pesquisa_select)
        self.todos.grid(row=0, column=0, padx=15)
        self.municipio = ttk.Radiobutton(fr_options, text="Municipio", value="Municipio", variable=self.pesquisa_select)
        self.municipio.grid(row=0, column=1, padx=15)
        self.estado = ttk.Radiobutton(fr_options, text="Estado", value="Estado", variable=self.pesquisa_select)
        self.estado.grid(row=0, column=2, padx=15)
        # datas
        lb_de = ttk.Label(fr_options, text="  DE:", font=('', 10, 'bold'))
        lb_de.grid(row=0, column=3)
        self.data_de = DateEntry(fr_options, width=10)
        self.data_de.grid(row=0, column=4)
        lb_ate = ttk.Label(fr_options, text="  ATÉ:", font=('', 10, 'bold'))
        lb_ate.grid(row=0, column=5)
        self.data_ate = DateEntry(fr_options, width=10)
        self.data_ate.grid(row=0, column=6)

        bt_pesquisar = ttk.Button(fr_options, text="Pesquisar", command=self.consulta_filtros)
        bt_pesquisar.grid(row=0, column=7, padx=15)

        #############################################################################################################
        linha1 = ttk.Frame(self)
        linha1.pack(fill='x')

        colunas = ['ait', 'placa', 'condutor', 'local', 'data', 're', 'codigo', 'talao', 'valor']
        largura = [60, 80, 150, 150, 80, 60, 60, 80, 80]
        ancora = ("e", "w", "w", "w", "center", "center", "center", "w", "e")

        i = 0
        self.t_consulta = ttk.Treeview(linha1, columns=colunas, show='headings',
                                       height=25, selectmode='browse')
        for cols in colunas:
            self.t_consulta.column(cols, width=largura[i], anchor=ancora[i])
            i = i + 1
        for cols in colunas:
            self.t_consulta.heading(cols, text=cols.upper())
        self.t_consulta.grid(row=0, column=0, pady=3, padx=10)
        # SCROOLBAR DA TREEVIEW
        self.scrool = ttk.Scrollbar(linha1, orient=tk.VERTICAL, command=self.t_consulta.yview)
        self.t_consulta.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=1, row=0, sticky='ns', pady=3)

        #############################################################################################################
        linha2 = ttk.Frame(self)
        linha2.pack(fill='x')
        self.lb_contador = ttk.Label(linha2, text="", font=('', 7, 'bold'))
        self.lb_contador.pack(fill='x', anchor='center')

        #############################################################################################################
        linha3 = ttk.Frame(self)
        linha3.pack(fill='x', pady=10)
        lb_texto = ttk.Label(linha3, text="Pesquisa por texto:", font=('', 11, 'bold'), foreground='Blue')
        lb_texto.grid(row=0, column=0, padx=15, sticky='w')
        self.texto = ttk.Entry(linha3, width=50)
        self.texto.grid(row=1, column=0, padx=15, pady=3, sticky='w')
        lb_obs = ttk.Label(linha3, text="* A pesquisa por texto anula as opções selecionadas e datas!",
                           font=('', 11, 'bold'), foreground='#FF9900')
        lb_obs.grid(row=2, column=0, padx=15, sticky='w')

        ld_divide = ttk.Label(linha3, text='')
        ld_divide.grid(row=0, column=1, padx=65)

        self.bt_editar = ttk.Button(linha3, text='EDITAR SELECIONADO', state='disabled', command=TransitoEdicao)
        self.bt_editar.grid(row=0, column=2)

        #############################################################################################################
        self.atualiza_t_consulta()
        #############################################################################################################
        self.t_consulta.bind('<<TreeviewSelect>>', self.habilitar_edicao)
        self.texto.bind('<KeyRelease>', lambda event: self.consulta_texto(self.texto.get()))

    #################################################################################################################
    def atualiza_t_consulta(self):
        for ait in self.t_consulta.get_children():
            self.t_consulta.delete(ait)
        lista_ait = lista_ait_padrao()
        contador = 0
        valor = 0.0
        for i in lista_ait:
            a = [str(i['numero']), i['placa'], i['condutor'], i['local'], data_pt(i['dia']), i['re'], i['codigo'],
                 i['talao'], f"R$ {i['valor']}"]
            self.t_consulta.insert('', tk.END, values=a)
            contador = contador + 1
            valor = valor + i['valor']
        valor = formatar_moeda(valor)
        self.lb_contador['text'] = f"     Total de registros exibidos: {contador}   -   " \
                                   f"Valor total das infrações: R$ {valor}"

    def consulta_filtros(self):
        for ait in self.t_consulta.get_children():
            self.t_consulta.delete(ait)
        self.texto.delete(0, 'end')
        ##########################################
        lista_ait = lista_ait_fitros(self.pesquisa_select.get(),
                                     data_us(self.data_de.entry.get()),
                                     data_us(self.data_ate.entry.get()))
        ##########################################
        contador = 0
        valor = 0.0
        for i in lista_ait:
            a = [str(i['numero']), i['placa'], i['condutor'], i['local'], data_pt(i['dia']), i['re'], i['codigo'],
                 i['talao'], f"R$ {i['valor']}"]
            self.t_consulta.insert('', tk.END, values=a)
            contador = contador + 1
            valor = valor + i['valor']
        valor = formatar_moeda(valor)
        self.lb_contador['text'] = f"     Total de registros exibidos: {contador}   -   " \
                                   f"Valor total das infrações: R$ {valor}"

    def consulta_texto(self, texto):
        for ait in self.t_consulta.get_children():
            self.t_consulta.delete(ait)
        ##########################################
        lista_ait = lista_ait_texto(texto)
        ##########################################
        contador = 0
        valor = 0.0
        for i in lista_ait:
            a = [str(i['numero']), i['placa'], i['condutor'], i['local'], data_pt(i['dia']), i['re'], i['codigo'],
                 i['talao'], f"R$ {i['valor']}"]
            self.t_consulta.insert('', tk.END, values=a)
            contador = contador + 1
            valor = valor + i['valor']
        valor = formatar_moeda(valor)
        self.lb_contador['text'] = f"     Total de registros exibidos: {contador}   -   " \
                                   f"Valor total das infrações: R$ {valor}"

    def habilitar_edicao(self, x):
        print(x)
        it = self.t_consulta.focus()
        try:
            dados = self.t_consulta.item(it).get('values')[0]
            self.ait_select = Ait()
            self.ait_select.set_ait(str(dados))
            if not self.ait_select.id_ait:
                self.ait_select = Ait()
                dados = f"0{dados}"
                self.ait_select.set_ait(dados)
        except Exception as e:
            print(e)
        AIT.set_ait(self.ait_select.numero)
        self.bt_editar['state'] = 'enabled'
