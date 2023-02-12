from imports import *
from datetime import timedelta
from functions.functions import data_mask, data_us, ano_atual, data_atual_pt
from classes.cl_contato import *
from classes.fn_mails import *
from relatorios.rel_eap import *


class ClientesEapGeral(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        self.geometry(tk_center(self, 800, 740))
        self.title("ADMIN - INFORMAÇÕES DE EAP")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        self.eap_selecionado = None

        ###############################################################################################################
        # LISTA DE CLIENTES CADASTRADOS (ATIVOS)
        ###############################################################################################################
        self.header = ttk.Frame(self)
        self.header.pack(fill='x', padx=10)
        self.lb_header = ttk.Label(self.header, text="LISTA DE CONSULTA EAP", font=('', 14))
        self.lb_header.pack(pady=20)

        self.form = ttk.Frame(self)
        self.form.pack(fill='x', padx=10)
        self.lb_periodo = ttk.Label(self.form, text="Período EAD")
        self.lb_periodo.grid(row=0, column=1, sticky='w')
        self.periodo = ttk.Combobox(self.form, values=list_periodo_ead)
        self.periodo.set('Não Informado')
        self.periodo.grid(row=1, column=1)
        self.lb_data_eap = ttk.Label(self.form, text='Data do EAP')
        self.lb_data_eap.grid(row=0, column=2, sticky='w', padx=5)
        self.data_eap = DateEntry(self.form)
        self.data_eap.grid(row=1, column=2, padx=5)
        self.data_eap.entry.bind('<KeyRelease>', lambda event: data_mask(self.data_eap, self.data_eap.entry.get()))
        self.bt_altera_eap = ttk.Button(self.form, text='Alterar', style='warning',
                                        state='disabled', command=self.altera_eap)
        self.bt_altera_eap.grid(row=1, column=3)

        # FRAME LISTA
        self.lista = ttk.Frame(self)
        self.lista.pack(fill='x', padx=10)
        # TREEVIEW DA LISTA
        self.colunas = ['grad', 're', 'nome', 'EAD', 'DATA EAP', 'Enviado E_mail de Aviso']
        self.largura = [75, 70, 290, 80, 80, 160]
        ancora = ("w", "w", "w", "w", "center", 'center')
        i = 0
        self.t_eap = ttk.Treeview(self.lista, columns=self.colunas, show='headings',
                                  height=33, selectmode='browse', style='warning')
        for cols in self.colunas:
            self.t_eap.column(cols, width=self.largura[i], anchor=ancora[i])
            i = i + 1
        for cols in self.colunas:
            self.t_eap.heading(cols, text=cols.upper())
        self.t_eap.grid(row=0, column=0)
        # SCROOLBAR DA TREEVIEW
        self.scrool = ttk.Scrollbar(self.lista, orient=tk.VERTICAL, command=self.t_eap.yview)
        self.t_eap.configure(yscrollcommand=self.scrool.set)
        self.scrool.grid(column=1, row=0, sticky='ns')

        # CHAMA FUNÇÃO PARA PREENCHIMENTO DA TREEVIEW
        self.atualiza_t_eap()
        # BIND PARA SETAR OS DADOS DO CLIENTE SELECIONADO
        self.t_eap.bind('<<TreeviewSelect>>', self.seleciona_cliente)

        self.menus = ttk.Frame(self)
        self.menus.pack(fill='x', padx=10, pady=15)
        self.lb_cliente = ttk.Label(self.menus, text='', width=50)
        self.lb_cliente.grid(row=1, column=0, sticky='w')

        self.bt_cliente = ttk.Button(self.menus, text='Gerar E-mail de aviso',
                                     style='info', state='disabled', command=self.gerar_email_eap)
        self.bt_cliente.grid(row=2, column=0, pady=5, sticky='w')
        """
        self.bt_exporta_xlsx = ttk.Button(self.menus, text='Exportar Dados CNH (xlsx)',
                                          style='success', command=lambda: exportar_cnh_xlsx(self.lb_msg))
        self.bt_exporta_xlsx.grid(row=1, column=1, padx=5, pady=5)

        self.bt_exporta_pdf = ttk.Button(self.menus, text='Exportar Dados CNH (PDF)',
                                         style='danger', command=lambda: exportar_cnh_pdf(self.lb_msg))
        self.bt_exporta_pdf.grid(row=1, column=2, padx=5, pady=5)

        """
        self.lb_msg = ttk.Label(self.menus, text='')
        self.lb_msg.grid(row=3, column=1, columnspan=2, sticky='w', pady=5, padx=2)

    # FUNÇÃO PARA ATUALIZAÇÃO DA LISTA DE CLIENTES ( * COM ERRO QUE NÃO INFLUENCIA )
    def atualiza_t_eap(self):
        for cliente in self.t_eap.get_children():
            self.t_eap.delete(cliente)
        cliente = relatorio_eap()
        cliente = cliente.values.tolist()
        for i in cliente:
            if i[5] == '01/01/1950':
                i[5] = "Não informado!"
            self.t_eap.insert('', tk.END, values=i)

    # FUNÇÃO QUE RECEBE OS DADOS DO CLIENTE SELECIONADO E SETA NO OBJ_CLIENTE_GLOBAL
    def seleciona_cliente(self, x):
        try:
            it = self.t_eap.focus()
            dados = self.t_eap.item(it)
            dados = dados.get('values')
            CLIENTE.set_cliente(dados[1][:6])
            self.lb_cliente['text'] = CLIENTE.nome
            self.bt_cliente['state'] = 'normal'
            self.eap_selecionado = Eap().set_eap(CLIENTE.re)
            if self.eap_selecionado:
                self.periodo.set(self.eap_selecionado.periodo_ead)
                self.data_eap.entry.delete(0, 'end')
                self.data_eap.entry.insert(0, data_pt(self.eap_selecionado.data_eap))
            self.bt_altera_eap['state'] = 'normal'
        except Exception as e:
            print(e, x)

    def altera_eap(self):
        insert_eap(CLIENTE.re, self.periodo.get(), data_us(self.data_eap.entry.get()), '')
        self.lb_msg['text'] = "Alterações Salvas"
        self.atualiza_t_eap()
        # except:
        #    print('erro ao alterar eap selecionado')

    def gerar_email_eap(self):
        e_mail = get_email_funcional(CLIENTE.re)
        Mails().send_mail(e_mail['contato'],
                          f"Aviso de Programação para o EAP {ano_atual()}",
                          f"Olá {CLIENTE.nome}\n"
                          f"Lembrando que não é necessário responder esse e_mail...\n\n"
                          f"Seu EAP está programado em {ano_atual()}: \n\n"
                          f"Período do EAD: 2ª quinzena de {self.eap_selecionado.periodo_ead}\n\n"
                          f"Data do EAP presencial:\n"
                          f"-> dias {data_pt(self.eap_selecionado.data_eap)} e "
                          f"{data_pt(self.eap_selecionado.data_eap + timedelta(days=1))} "
                          f"\n\nAtenciosamente: Equipe ADM")

        edita_aviso_eap(CLIENTE.re, data_us(data_atual_pt()))
        self.atualiza_t_eap()


"""
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
"""
