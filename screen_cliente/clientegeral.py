from screen_cliente.clientenovo import *
from screen_cliente.clienteedita import *
from screen_cliente.clientecontato import *
from screen_cliente.cliente_dados_pessoais import *
from screen_cliente.cliente_epi import *
from screen_cliente.cliente_info import *
from screen_cliente.cliente_talao import *


class ClienteGeral(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 800, 700)
        self.geometry(geo)
        self.title("ADMIN - POLÍCIA MILITAR")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        ###############################################################################################################
        # LISTA DE CLIENTES CADASTRADOS (ATIVOS)
        ###############################################################################################################

        # FRAME LISTA
        self.lista = ttk.Frame(self)
        self.lista.place(relx=0.03, rely=0.06, relwidth=0.64, relheight=0.77)
        # TREEVIEW DA LISTA
        self.colunas = ['grad', 're', 'nome']
        self.largura = [80, 70, 290]
        ancora = ("w", "center", "w")
        i = 0
        self.t_cliente = ttk.Treeview(self.lista, columns=self.colunas, show='headings',
                                      height=33, selectmode='browse')
        for cols in self.colunas:
            self.t_cliente.column(cols, width=self.largura[i], anchor=ancora[i])
            i = i + 1
        for cols in self.colunas:
            self.t_cliente.heading(cols, text=cols.upper())
        self.t_cliente.grid(row=0, column=0, pady=3, padx=3)
        # SCROOLBAR DA TREEVIEW
        self.scrool = ttk.Scrollbar(self.lista, orient=tk.VERTICAL, command=self.t_cliente.yview)
        self.t_cliente.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=1, row=0, sticky='ns', pady=3)

        # CHAMA FUNÇÃO PARA PREENCHIMENTO DA TREEVIEW
        self.atualiza_t_cliente()
        # BIND PARA SETAR OS DADOS DO CLIENTE SELECIONADO
        self.t_cliente.bind('<<TreeviewSelect>>', self.seleciona_cliente)

        ###############################################################################################################
        # MENU DE BOTÕES COM AS FUNÇÕES PARA GERENCIAMENTO DE CLIENTES
        ###############################################################################################################
        self.menu = ttk.Frame(self)
        self.menu.place(relx=0.69, rely=0.07, relwidth=0.27, relheight=0.98)
        # BOTÃO ATUALIZAR TABELA
        self.bt_atualizar = ttk.Button(self.menu, text='ATUALIZAR LISTA',
                                       width=60, style='info', command=self.atualiza_t_cliente)
        self.bt_atualizar.pack(pady=3)
        # BOTÃO NOVO REGISTRO DE CLIENTE (DADOS FUNCIONAIS)
        self.bt_novo = ttk.Button(self.menu, text='CADASTRAR NOVO', width=60, command=ClienteNovo, style='success')
        self.bt_novo.pack(pady=3)
        self.divide = ttk.Label(self.menu, text='OPÇÕES', width=60, style='light')
        self.divide.pack(pady=15)

        # BOTÃO EDITAR DADOS FUNCIONAIS
        self.bt_funcionais = ttk.Button(self.menu, text='EDITAR DADOS FUNCIONAIS', width=60, command=ClienteEdita,
                                        style='light', state='disabled')
        self.bt_funcionais.pack(pady=3)

        # BOTÃO CONTATOS DO CLIENTE SELECIONADO
        self.bt_contato = ttk.Button(self.menu, text='EDITAR DADOS DE CONTATO', width=60, command=ClienteContato,
                                     style='primary', state='disabled')
        self.bt_contato.pack(pady=3)
        # BOTÃO DADOS DE ENDEREÇO DO CLIENTE
        self.bt_endereco = ttk.Button(self.menu, text='EDITAR DADOS PESSOAIS', width=60,
                                      command=ClienteDadosPessoais, state='disabled', style='primary')
        self.bt_endereco.pack(pady=3)
        self.bt_epi = ttk.Button(self.menu, text='DADOS DE "EPI"', width=60,
                                 command=ClienteEpi, state='disabled', style='primary')
        self.bt_epi.pack(pady=3)
        self.bt_info = ttk.Button(self.menu, text='INFORMAÇÕES GERAIS', width=60,
                                  command=ClienteInfo, state='disabled', style='primary')
        self.bt_info.pack(pady=3)
        self.bt_talonario = ttk.Button(self.menu, text="TALONÁRIO AIT'S", width=60,
                                       command=ClienteTalao, state='disabled', style='primary')
        self.bt_talonario.pack(pady=3)

    # FUNÇÃO PARA ATUALIZAÇÃO DA LISTA DE CLIENTES ( * COM ERRO QUE NÃO INFLUENCIA )
    def atualiza_t_cliente(self):
        for cliente in self.t_cliente.get_children():
            self.t_cliente.delete(cliente)
        cliente = lista_clientes()
        for i in cliente:
            i = [i['graduacao_txt'], f"{i['re']}-{i['dc']}", i['nome']]
            self.t_cliente.insert('', tk.END, values=i)

    # FUNÇÃO QUE RECEBE OS DADOS DO CLIENTE SELECIONADO E SETA NO OBJ_CLIENTE_GLOBAL
    def seleciona_cliente(self, x):
        try:
            it = self.t_cliente.focus()
            dados = self.t_cliente.item(it)
            dados = dados.get('values')
            cliente_global.set_cliente(dados[2])
            self.bt_funcionais['state'] = 'normal'
            self.bt_contato['state'] = 'normal'
            self.bt_endereco['state'] = 'normal'
            self.bt_epi['state'] = 'normal'
            self.bt_info['state'] = 'normal'
            self.bt_talonario['state'] = 'normal'
        except IndexError:
            print('')
