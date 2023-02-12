from imports import *
from functions.functions import inicio_mes_pt, data_us
from classes_transito.tr_ait import *


class TransitoRelatorios(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        self.geometry(tk_center(self, 850, 650))
        self.title("ADMIN Trânsito - CONSULTAS")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        #############################################################################################################
        # VARIAVEIS
        self.pesquisa_select = tk.StringVar(self, "Todos")

        #############################################################################################################
        header = ttk.Frame(self)
        header.pack(fill='x', pady=10)
        lb_header = ttk.Label(header, text="RELATÓRIOS", font=('', 12, 'bold'))
        lb_header.pack(anchor='w', padx=15)

        #############################################################################################################
        fr_options = ttk.Frame(self)
        fr_options.pack(fill='x', pady=10, padx=15)
        # datas
        lb_de = ttk.Label(fr_options, text="  DE: ", font=('', 10, 'bold'))
        lb_de.grid(row=0, column=0)
        self.data_de = DateEntry(fr_options, width=10)
        self.data_de.grid(row=0, column=1)
        self.data_de.entry.delete(0, 'end')
        self.data_de.entry.insert(0, inicio_mes_pt())
        lb_ate = ttk.Label(fr_options, text="  ATÉ: ", font=('', 10, 'bold'))
        lb_ate.grid(row=0, column=2)
        self.data_ate = DateEntry(fr_options, width=10)
        self.data_ate.grid(row=0, column=3)

        bt_pesquisar = ttk.Button(fr_options, text="Pesquisar", command=self.consulta_filtros)
        bt_pesquisar.grid(row=0, column=4, padx=15)

        #############################################################################################################
        self.linha1 = ttk.Frame(self)
        self.linha1.pack(fill='x')

        self.lb_resumo = ttk.Label
        self.t_resumo = ttk.Treeview()

        self.lb_resumo_individual = ttk.Label()
        self.t_individual_pm = ttk.Treeview()
        self.scrool = ttk.Scrollbar()
        """
        # SCROOLBAR DA TREEVIEW
        self.scrool = ttk.Scrollbar(self.linha1, orient=tk.VERTICAL, command=self.t_consulta.yview)
        self.t_consulta.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=1, row=0, sticky='ns', pady=3)
        """

        #############################################################################################################
        self.tabela_resumo()
        #############################################################################################################

    #################################################################################################################
    def tabela_resumo(self):
        for widget in self.linha1.winfo_children():
            widget.destroy()

        ####################################################################################
        # TABELA DE RESUMO
        ####################################################################################
        self.lb_resumo = ttk.Label(self.linha1, text='RESUMO GERAL', font=('', 12, 'bold'))

        colunas = ['competencia', 'quantidade', 'valores']
        largura = [140, 90, 100]
        ancora = ("w", "center", "e")
        self.t_resumo = ttk.Treeview(self.linha1)

        i = 0
        self.t_resumo = ttk.Treeview(self.linha1, columns=colunas, show='headings',
                                     height=3, selectmode='none', style='dark')
        for cols in colunas:
            self.t_resumo.column(cols, width=largura[i], anchor=ancora[i])
            i = i + 1
        for cols in colunas:
            self.t_resumo.heading(cols, text=cols.upper())
        ####################################################################################
        lista_resumo = lista_ait_resumo_fitros(data_us(self.data_de.entry.get()),
                                               data_us(self.data_ate.entry.get()))
        ####################################################################################
        for i in lista_resumo:
            self.t_resumo.insert('', tk.END, values=i, tags='normal')

        self.t_resumo.grid(row=1, column=0, padx=15, pady=5, sticky='n')
        self.lb_resumo.grid(row=0, column=0, padx=15, pady=15, sticky='n')
        self.t_resumo.tag_configure('normal', foreground='black', background='white', font=('', 9, 'bold'))

        ####################################################################################
        # TABELA DE RESUMO INDIVIDUAL
        ####################################################################################
        self.lb_resumo_individual = ttk.Label(self.linha1, text='RESUMO INDIVIDUAL', font=('', 12, 'bold'))

        colunas = ['re', 'nome', 'municipal', 'estadual', 'total']
        largura = [78, 110, 80, 80, 80]
        ancora = ('w', 'w', 'center', 'center', 'center')
        self.t_individual_pm = ttk.Treeview(self.linha1)

        i = 0
        self.t_individual_pm = ttk.Treeview(self.linha1, columns=colunas, show='headings',
                                            height=30, selectmode='none', style='dark')
        for cols in colunas:
            self.t_individual_pm.column(cols, width=largura[i], anchor=ancora[i])
            i = i + 1
        for cols in colunas:
            self.t_individual_pm.heading(cols, text=cols.upper())
        ####################################################################################
        resumo_individual = lista_ait_resumo_individual(data_us(self.data_de.entry.get()),
                                                        data_us(self.data_ate.entry.get()))
        
        ####################################################################################
        for i in resumo_individual:
            self.t_individual_pm.insert('', tk.END, values=i, tags='normal')

        self.t_individual_pm.grid(row=1, column=1, pady=5)
        self.lb_resumo_individual.grid(row=0, column=1, padx=15, pady=15)
        self.t_individual_pm.tag_configure('normal', foreground='black', background='white', font=('', 9, 'bold'))
        self.scrool = ttk.Scrollbar(self.linha1, orient=tk.VERTICAL, command=self.t_individual_pm.yview)
        self.t_individual_pm.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=2, row=1, sticky='ns', pady=3)

    def consulta_filtros(self):
        for widget in self.linha1.winfo_children():
            widget.destroy()
        self.tabela_resumo()
