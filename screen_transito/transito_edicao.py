import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import DateEntry

from functions.tk_center import tk_center
from functions.functions import data_mask, hora_mask, is_number, data_us, data_pt

from classes_transito.tr_ait import *
from classes_transito.tr_logradouros import *
from classes_transito.tr_infra import *
from classes_transito.tr_talao import *
from functions.globals import ait_global

class TransitoEdicao(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 700, 600)
        self.geometry(geo)
        self.title("ADMIN Trânsito - EDITAR AUTO DE INFRAÇÃO")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        ##############################################################################################################
        # VARIÁVEIS DE INICIALIZAÇÃO
        ##############################################################################################################
        self.talao_select = tk.StringVar(self, "Municipio")
        self.dados_form = []
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

        self.municipal = ttk.Radiobutton(linha1, text="Municipal   | ", value="Municipio",
                                         variable=self.talao_select)
        self.municipal.grid(row=0, column=1, pady=5, padx=5)
        self.estadual = ttk.Radiobutton(linha1, text="Estadual", value="Estado",
                                        variable=self.talao_select)
        self.estadual.grid(row=0, column=2, pady=5, padx=5)

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
        self.competencia = ttk.Label(linha3, text='', background='#FFDAB9', width=30)
        self.competencia.grid(row=1, column=4, ipady=3)

        ##############################################################################################################
        linha4 = ttk.Frame(self)
        linha4.pack(fill='x', padx=20, pady=25)
        self.artigo = ttk.Label(linha4, text='', background='#FFDAB9', width=100)
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

        ##############################################################################################################
        linha8 = ttk.Frame(self)
        linha8.pack(fill='x', padx=20, pady=35)
        self.lb_msg = ttk.Label(linha8, text='MSG', anchor='center', borderwidth=1, style='warning', relief='solid')
        self.lb_msg.pack(fill='x', ipady=3)

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
        # PREENCHE O FORMULÁRIO
        ##############################################################################################################
        self.preenche_form()

    ##############################################################################################################
    # FUNÇÕES DA PÁGINA
    ##############################################################################################################
    def salvar(self):
        if self.coleta_formulario():
            if ait_global.update_ait():
                self.lb_msg['text'] = f"{self.ait.get()} Salvo!!!"
                self.lb_msg['foreground'] = "black"
                self.lb_msg['font'] = ('', 10, 'bold')
            else:
                self.lb_msg['text'] = "Houve um erro ao salvar"
                self.lb_msg['foreground'] = "red"
                self.lb_msg['font'] = ('', 10, 'bold')
            novo_logradouro(self.local.get().upper())


    def coleta_formulario(self):
        ait_global.numero = self.ait.get()
        ait_global.placa = self.placa.get().upper()
        ait_global.condutor = self.condutor.get().upper()
        ait_global.local = self.local.get().upper()
        ait_global.dia = data_us(self.data.entry.get())
        ait_global.hora = self.hora.get()
        ait_global.re = self.re.get()
        ait_global.codigo = self.codigo.get()
        ait_global.competencia = self.competencia['text']
        ait_global.artigo = self.artigo['text']
        ait_global.crr = self.crr.get().upper()
        ait_global.remocao = self.recolha.get().upper()
        ait_global.cnh = self.cnh.get().upper()
        ait_global.alcoolemia = self.alcoolemia.get().upper()
        ait_global.obs = self.obs.get().upper()
        ait_global.talao = self.talao_select.get()

        if ait_global.numero == "" or ait_global.placa == "" or ait_global.local == "" or\
           ait_global.dia == "" or ait_global.hora == "" or ait_global.re == "" or\
           ait_global.codigo == "" or ait_global.competencia == "":
            return False
        else:
            return True

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
                self.competencia['background'] = '#F0FFF0'
                self.artigo['background'] = '#F0FFF0'
                ait_global.valor = "{:.2f}".format(cod.valor * cod.fator)
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

    def preenche_form(self):
        self.talao_select.set(ait_global.talao)
        self.ait.insert(0, ait_global.numero)
        self.placa.insert(0, ait_global.placa)
        self.condutor.insert(0, ait_global.condutor)
        self.local.insert(0, ait_global.local)
        self.data.entry.delete(0, 'end')
        self.data.entry.insert(0, data_pt(ait_global.dia))
        self.hora.insert(0, ait_global.hora)
        self.re.insert(0, ait_global.re)
        self.codigo.insert(0, ait_global.codigo)
        self.competencia['text'] = ait_global.competencia
        self.artigo['text'] = ait_global.artigo
        self.crr.insert(0, ait_global.crr)
        self.recolha.set(ait_global.remocao)
        self.cnh.insert(0, ait_global.cnh)
        self.alcoolemia.insert(0, ait_global.alcoolemia)
        self.obs.insert(0, ait_global.obs)