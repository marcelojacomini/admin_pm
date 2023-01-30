from os import path
from fpdf import FPDF
from relatorios.rel_cnh import *

from screen_cliente.cliente_dados_pessoais import *


class ClientesCnhGeral(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 800, 720)
        self.geometry(geo)
        self.title("ADMIN - INFORMAÇÕES DE CNH")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        ###############################################################################################################
        # LISTA DE CLIENTES CADASTRADOS (ATIVOS)
        ###############################################################################################################
        self.header = ttk.Frame(self)
        self.header.pack(fill='x', padx=10)
        self.lb_header = ttk.Label(self.header, text="LISTA DE CONSULTA", font=('', 14))
        self.lb_header.pack(pady=20)

        # FRAME LISTA
        self.lista = ttk.Frame(self)
        self.lista.pack(fill='x', padx=10)
        # TREEVIEW DA LISTA
        self.colunas = ['grad', 're', 'nome', 'CNH', 'Validade', 'CAT', 'SAT', 'Sit.CNH']
        self.largura = [75, 70, 290, 80, 70, 40, 40, 80]
        ancora = ("w", "center", "w", "w", "center", "center", "center", "center")
        i = 0
        self.t_cnh = ttk.Treeview(self.lista, columns=self.colunas, show='headings',
                                  height=33, selectmode='browse')
        for cols in self.colunas:
            self.t_cnh.column(cols, width=self.largura[i], anchor=ancora[i])
            i = i + 1
        for cols in self.colunas:
            self.t_cnh.heading(cols, text=cols.upper())
        self.t_cnh.grid(row=0, column=0)
        # SCROOLBAR DA TREEVIEW
        self.scrool = ttk.Scrollbar(self.lista, orient=tk.VERTICAL, command=self.t_cnh.yview)
        self.t_cnh.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=1, row=0, sticky='ns')

        # CHAMA FUNÇÃO PARA PREENCHIMENTO DA TREEVIEW
        self.atualiza_t_cnh()
        # BIND PARA SETAR OS DADOS DO CLIENTE SELECIONADO
        self.t_cnh.bind('<<TreeviewSelect>>', self.seleciona_cliente)

        self.menus = ttk.Frame(self)
        self.menus.pack(fill='x', padx=10, pady=15)
        self.lb_cliente = ttk.Label(self.menus, text='', width=50)
        self.lb_cliente.grid(row=0, column=0, sticky='w')

        self.bt_cliente = ttk.Button(self.menus, text='Acessar Cliente Selecionado',
                                     style='info', state='disabled', command=ClienteDadosPessoais)
        self.bt_cliente.grid(row=1, column=0, pady=5, sticky='w')

        self.bt_exporta_xlsx = ttk.Button(self.menus, text='Exportar Dados CNH (xlsx)',
                                          style='success', command=lambda: exportar_cnh_xlsx(self.lb_msg))
        self.bt_exporta_xlsx.grid(row=1, column=1, padx=5, pady=5)

        self.bt_exporta_pdf = ttk.Button(self.menus, text='Exportar Dados CNH (PDF)',
                                         style='danger', command=lambda: exportar_cnh_pdf(self.lb_msg))
        self.bt_exporta_pdf.grid(row=1, column=2, padx=5, pady=5)

        self.lb_msg = ttk.Label(self.menus, text='')
        self.lb_msg.grid(row=3, column=1, columnspan=2, sticky='w', pady=5, padx=2)

        self.t_cnh.tag_configure('vencida', foreground='#FF0000', font=('', 9, 'bold'))

    # FUNÇÃO PARA ATUALIZAÇÃO DA LISTA DE CLIENTES ( * COM ERRO QUE NÃO INFLUENCIA )
    def atualiza_t_cnh(self):
        for cliente in self.t_cnh.get_children():
            self.t_cnh.delete(cliente)
        cliente = relatorio_cnh()
        cliente = cliente.values.tolist()
        for i in cliente:
            if i[7] == "Vencida":
                self.t_cnh.insert('', tk.END, values=i, tags='vencida')
            else:
                self.t_cnh.insert('', tk.END, values=i)

    # FUNÇÃO QUE RECEBE OS DADOS DO CLIENTE SELECIONADO E SETA NO OBJ_CLIENTE_GLOBAL
    def seleciona_cliente(self, x):
        try:
            it = self.t_cnh.focus()
            dados = self.t_cnh.item(it)
            dados = dados.get('values')
            cliente_global.set_cliente(dados[1][:6])
            self.lb_cliente['text'] = cliente_global.nome
            self.bt_cliente['state'] = 'normal'
        except IndexError:
            print('')


def exportar_cnh_xlsx(lb_msg):
    pasta_user = path.join(path.expanduser("~"), "Documents/Lista de CNH.xlsx")
    try:
        with pd.ExcelWriter(pasta_user) as writer:
            lista_cnh = relatorio_cnh()
            lista_cnh.to_excel(writer, sheet_name="CNH")
            lb_msg['text'] = "Arquivo exportado para pasta 'Documentos'"
    except:
        lb_msg['text'] = "Houve um erro ao exportar arquivo!!!'"


def exportar_cnh_pdf(lb_msg):
    lista_cnh = relatorio_cnh()
    lista_cnh = lista_cnh.values.tolist()

    pdf = FPDF(format="A4", orientation='landscape')

    pdf.add_page()

    pdf.set_font('helvetica', size=14, style='b')
    pdf.set_draw_color(200, 100, 30)
    pdf.set_text_color(200, 50, 50)
    pdf.cell(200, 10, "Conferência de CNH", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font('helvetica', size=10, style='b')
    pdf.set_text_color(0, 0, 0)
    a = 8
    pdf.cell(20, a, "GRAD", 1)
    pdf.cell(20, a, "RE", 1)
    pdf.cell(85, a, "NOME", 1)
    pdf.cell(30, a, "Nº CNH", 1)
    pdf.cell(30, a, "VALIDADE", 1)
    pdf.cell(20, a, "CAT.", 1, align='C')
    pdf.cell(20, a, "SAT", 1, align='C')
    pdf.cell(30, a, "Situação", 1, new_x="LMARGIN", new_y="NEXT", align='C')

    pdf.set_font('helvetica', size=10, style="")
    a = 5
    for i in lista_cnh:
        if i[7] == 'Vencida':
            pdf.set_text_color(200, 0, 0)
            pdf.cell(20, a, i[0], 1)
            pdf.cell(20, a, i[1], 1)
            pdf.cell(85, a, i[2], 1)
            pdf.cell(30, a, i[3], 1)
            pdf.cell(30, a, i[4], 1)
            pdf.cell(20, a, i[5], 1, align='C')
            pdf.cell(20, a, i[6], 1, align='C')
            pdf.cell(30, a, i[7], 1, new_x="LMARGIN", new_y="NEXT", align='C')
        else:
            pdf.set_text_color(0, 0, 0)
            pdf.cell(20, a, i[0], 1)
            pdf.cell(20, a, i[1], 1)
            pdf.cell(85, a, i[2], 1)
            pdf.cell(30, a, i[3], 1)
            pdf.cell(30, a, i[4], 1)
            pdf.cell(20, a, i[5], 1, align='C')
            pdf.cell(20, a, i[6], 1, align='C')
            pdf.cell(30, a, i[7], 1, new_x="LMARGIN", new_y="NEXT", align='C')

    pasta_user = path.join(path.expanduser("~"), "Documents/Lista de CNH.pdf")
    try:
        pdf.output(pasta_user)
        lb_msg['text'] = "Arquivo exportado para pasta 'Documentos'"
    except:
        lb_msg['text'] = "Houve um erro ao exportar arquivo!!!'"
