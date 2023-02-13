from imports import *
from functions.functions import data_mask, hora_mask, data_us, is_number
from classes_transito.tr_talao import *
from classes_transito.tr_ait import *
from classes_transito.tr_logradouros import *
from classes_transito.tr_infra import *


class TransitoCadastro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 700, 600)
        self.geometry(geo)
        self.title("ADMIN Trânsito - NOVO AUTO DE INFRAÇÃO")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        ##############################################################################################################
        # VARIÁVEIS DE INICIALIZAÇÃO
        ##############################################################################################################
        self.talao_select = tk.StringVar(self, "Municipio")
        self.dados_form = []
        self.valor = None
        self.repetir = ttk.BooleanVar()
        self.taloes = lista_talonario_geral()

        ##############################################################################################################
        # FORMULÁRIO DE CADASTRO DE AIT
        ##############################################################################################################
        header = ttk.Frame(self)
        header.pack(fill='x', padx=20, pady=20)
        lb_header = ttk.Label(header, text="CADASTRAR AUTO DE INFRAÇÃO", font=('', 14, 'bold'))
        lb_header.pack()

        ##############################################################################################################
        linha1 = ttk.Frame(self)
        linha1.pack(fill='x', padx=20)
        lb_talao = ttk.Label(linha1, text="Informe o talão: ", font=('', 10, 'bold'))
        lb_talao.grid(column=0, row=0)

        municipal = ttk.Radiobutton(linha1, text="Municipal   | ", value="Municipio",
                                    variable=self.talao_select)
        municipal.grid(row=0, column=1, pady=5, padx=5)
        estadual = ttk.Radiobutton(linha1, text="Estadual", value="Estado",
                                   variable=self.talao_select)
        estadual.grid(row=0, column=2, pady=5, padx=5)

        ##############################################################################################################
        linha2 = ttk.Frame(self)
        linha2.pack(fill='x', padx=20, pady=25)
        lb_ait = ttk.Label(linha2, text="Nº AIT", font=('', 10, 'bold'))
        lb_ait.grid(row=0, column=0, sticky='w')
        self.ait = ttk.Entry(linha2, width=12, style="success")
        self.ait.grid(row=1, column=0)

        lb_placa = ttk.Label(linha2, text='Placa', font=('', 10, 'bold'))
        lb_placa.grid(row=0, column=1, sticky='w', padx=15)
        self.placa = ttk.Entry(linha2, width=10)
        self.placa.grid(row=1, column=1, padx=15)

        lb_condutor = ttk.Label(linha2, text="Condutor", font=('', 10, 'bold'))
        lb_condutor.grid(row=0, column=2, sticky='w')
        self.condutor = ttk.Entry(linha2, width=30)
        self.condutor.grid(row=1, column=2)

        lb_local = ttk.Label(linha2, text="LOCAL", font=('', 10, 'bold'))
        lb_local.grid(row=0, column=3, sticky='w', padx=15)
        self.local = ttk.Entry(linha2, width=35)
        self.local.grid(row=1, column=3, padx=15)

        ##############################################################################################################
        linha3 = ttk.Frame(self)
        linha3.pack(fill='x', padx=20)
        lb_data = ttk.Label(linha3, text='Data', font=('', 10, 'bold'))
        lb_data.grid(row=0, column=0, sticky='w')
        self.data = DateEntry(linha3, style='warning', width=12)
        self.data.grid(row=1, column=0)

        lb_hora = ttk.Label(linha3, text="Hora", font=('', 10, 'bold'))
        lb_hora.grid(row=0, column=1, sticky='w', padx=15)
        self.hora = ttk.Entry(linha3, width=6)
        self.hora.grid(row=1, column=1, padx=15)

        lb_re = ttk.Label(linha3, text="RE PM", font=('', 10, 'bold'))
        lb_re.grid(row=0, column=2, sticky='w')
        self.re = ttk.Entry(linha3, width=9)
        self.re.grid(row=1, column=2)

        lb_codigo = ttk.Label(linha3, text="Cód. Enq.", font=('', 10, 'bold'))
        lb_codigo.grid(row=0, column=3, sticky='w', padx=25)
        self.codigo = ttk.Entry(linha3, width=9, style='secondary')
        self.codigo.grid(row=1, column=3, padx=25)

        lb_competencia = ttk.Label(linha3, text='Competência', font=('', 10, 'bold'))
        lb_competencia.grid(row=0, column=4, sticky='w')
        self.competencia = ttk.Label(linha3, text='', background='#696969', width=20)
        self.competencia.grid(row=1, column=4, ipady=3)

        ##############################################################################################################
        linha4 = ttk.Frame(self)
        linha4.pack(fill='x', padx=20, pady=25)
        self.artigo = ttk.Label(linha4, text='', background='#696969', width=90)
        self.artigo.pack(fill='x', ipady=3)

        ##############################################################################################################
        linha5 = ttk.Frame(self)
        linha5.pack(fill='x', padx=20)
        lb_crr = ttk.Label(linha5, text="CRR", font=('', 10, 'bold'))
        lb_crr.grid(row=0, column=0, sticky='w')
        self.crr = ttk.Entry(linha5, width=10)
        self.crr.grid(row=1, column=0)

        lb_recolha = ttk.Label(linha5, text="Veíc. Rec.", font=('', 10, 'bold'))
        lb_recolha.grid(row=0, column=1, padx=15, sticky='w')
        self.recolha = ttk.Combobox(linha5, width=10, values=['NÃO', 'SIM'], state='readonly')
        self.recolha.grid(row=1, column=1, padx=15)
        self.recolha.set('NÃO')

        lb_cnh = ttk.Label(linha5, text="CNH Recolhida", font=('', 10, 'bold'))
        lb_cnh.grid(row=0, column=2, sticky='w')
        self.cnh = ttk.Entry(linha5, width=15)
        self.cnh.grid(row=1, column=2)

        lb_alcoolemia = ttk.Label(linha5, text='Dados Etilômetro', font=('', 10, 'bold'))
        lb_alcoolemia.grid(row=0, column=3, sticky='w', padx=15)
        self.alcoolemia = ttk.Entry(linha5, width=50)
        self.alcoolemia.grid(row=1, column=3, padx=15)

        ##############################################################################################################
        linha6 = ttk.Frame(self)
        linha6.pack(fill='x', padx=20, pady=25)
        lb_obs = ttk.Label(linha6, text='Observações', font=('', 10, 'bold'))
        lb_obs.grid(row=0, column=0, sticky='w')
        self.obs = ttk.Entry(linha6, width=100)
        self.obs.grid(row=1, column=0)

        ##############################################################################################################
        linha7 = ttk.Frame(self)
        linha7.pack(fill='x', padx=20)
        bt_salvar = ttk.Button(linha7, text="SALVAR", width=40, style='success', command=self.salvar)
        bt_salvar.grid(row=0, column=0)

        self.repete = ttk.Checkbutton(linha7, text="Marque para repetir o veículo!", style="success-round-toggle",
                                      variable=self.repetir)
        self.repete.grid(row=0, column=1, padx=50)

        ##############################################################################################################
        linha8 = ttk.Frame(self)
        linha8.pack(fill='x', padx=20, pady=35)
        self.lb_msg = ttk.Label(linha8, text='MSG', anchor='center', borderwidth=1, style='warning', relief='solid')
        self.lb_msg.pack(fill='x', ipady=3)

        # finaliza detalhes do carregamento da página
        self.ait.focus()

        ##############################################################################################################
        # BIND
        ##############################################################################################################
        self.ait.bind('<FocusOut>', lambda event: self.verifica_ait(self.ait.get()))
        self.local.bind('<KeyRelease>', (lambda event: self.autocomplete_logradouro(self.local.get().upper(),
                                                                                    len(self.local.get()))))
        self.data.entry.bind('<KeyRelease>', lambda event: data_mask(self.data, self.data.entry.get()))
        self.hora.bind('<KeyRelease>', lambda event: hora_mask(self.hora, self.hora.get()))
        self.codigo.bind('<KeyRelease>', lambda event: self.verifica_enquadramento(self.codigo, self.codigo.get()))

    ##############################################################################################################
    # FUNÇÕES DA PÁGINA
    ##############################################################################################################
    def salvar(self):
        dados_form = self.coleta_formulario()
        if insert_ait(dados_form):
            self.lb_msg['text'] = f"{self.ait.get()} Salvo!!!"
            self.lb_msg['foreground'] = "yellow"
            self.lb_msg['font'] = ('', 10, 'bold')
        else:
            self.lb_msg['text'] = "Houve um erro ao salvar"
            self.lb_msg['foreground'] = "red"
            self.lb_msg['font'] = ('', 10, 'bold')
        novo_logradouro(self.local.get().upper())
        if self.repetir.get():
            self.repete_veiculo()
        else:
            self.limpa_form()

    def coleta_formulario(self):
        self.dados_form = [
            self.ait.get(),
            self.placa.get().upper(),
            self.condutor.get().upper(),
            self.local.get().upper(),
            data_us(self.data.entry.get()),
            self.hora.get(),
            self.re.get(),
            self.codigo.get(),
            self.competencia['text'],
            self.artigo['text'],
            self.crr.get().upper(),
            self.recolha.get().upper(),
            self.cnh.get().upper(),
            self.alcoolemia.get().upper(),
            self.obs.get().upper(),
            self.talao_select.get(),
            self.valor
        ]
        if self.dados_form[0] == "" or self.dados_form[1] == "" or self.dados_form[3] == "" \
           or self.dados_form[4] == "" or self.dados_form[5] == "" or self.dados_form[6] == "" \
           or self.dados_form[7] == "" or self.dados_form[8] == "":
            self.lb_msg['text'] = "AIT, Placa, Local, Data, Hora, RE e Código não podem ficar vazios!!!"
            self.lb_msg['foreground'] = 'red'
            return False
        else:
            return self.dados_form

    def verifica_ait(self, numero_ait):
        if numero_ait == "":
            pass
        else:
            ait = Ait()
            ait.set_ait(numero_ait)
            if ait.numero:
                self.lb_msg['text'] = "AIT já cadastrado!!!"
                self.lb_msg['foreground'] = 'red'
                self.ait.focus()
            else:
                self.lb_msg['text'] = ""
                # preenche o re pela lista de talões
                for num_aits in self.taloes:
                    if num_aits[1]:
                        if int(numero_ait) in num_aits[1]:
                            self.re.delete(0, 'end')
                            self.re.insert(0, num_aits[0])
                            self.re['state'] = 'disabled'
                            break
                        else:
                            self.re.delete(0, 'end')
                            self.re['state'] = 'normal'

    def verifica_enquadramento(self, campo, codigo_enq):
        if len(codigo_enq) >= 6:
            campo.delete(5, "end")
        elif not is_number(codigo_enq):
            campo.delete((len(codigo_enq) - 1), 'end')
        elif len(codigo_enq) < 5:
            self.competencia['text'] = ''
            self.artigo['text'] = ''
        elif len(codigo_enq) == 5:
            cod = Infra()
            cod.set_infra(codigo_enq)
            if cod.artigo:
                self.competencia['text'] = f" {cod.competencia}"
                self.artigo['text'] = f" {cod.artigo}"
                self.competencia['font'] = ('', 10, 'bold')
                self.artigo['font'] = ('', 10, 'bold')
                self.competencia['background'] = '#696969'
                self.artigo['background'] = '#696969'
                self.valor = "{:.2f}".format(cod.valor * cod.fator)
            else:
                self.competencia['text'] = ' Cód. Inválido'
                self.artigo['text'] = ' Cód. Inválido'
                self.competencia['background'] = '#FFDAB9'
                self.artigo['background'] = '#FFDAB9'

    def autocomplete_logradouro(self, logradouro, len_f):
        logr = retorna_logradouro(logradouro)
        if len(logr) > len_f:
            self.local.delete(0, 'end')
            self.local.insert(0, logr.upper())
            self.local.select_range(len_f, len(logr))

    def repete_veiculo(self):
        self.ait.delete(0, 'end')
        self.codigo.delete(0, 'end')
        self.competencia['text'] = ""
        self.artigo['text'] = ""
        self.crr.delete(0, 'end')
        self.recolha.set("NÃO")
        self.cnh.delete(0, 'end')
        self.alcoolemia.delete(0, 'end')
        self.obs.delete(0, 'end')
        self.ait.focus()

    def limpa_form(self):
        self.ait.delete(0, 'end')
        self.placa.delete(0, 'end')
        self.condutor.delete(0, 'end')
        self.local.delete(0, 'end')
        self.hora.delete(0, 'end')
        self.re['state'] = 'normal'
        self.re.delete(0, 'end')
        self.codigo.delete(0, 'end')
        self.competencia['text'] = ""
        self.artigo['text'] = ""
        self.crr.delete(0, 'end')
        self.recolha.set("NÃO")
        self.cnh.delete(0, 'end')
        self.alcoolemia.delete(0, 'end')
        self.obs.delete(0, 'end')
        self.ait.focus()
