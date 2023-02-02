import logging
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import DateEntry

from functions.tk_center import tk_center
from functions.functions import data_mask, hora_mask, codigo_mask
from data_base.data_base import Con

from classes_transito.tr_logradouros import *
from classes_transito.tr_infra import *


class TransitoCadastro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 700, 700)
        self.geometry(geo)
        self.title("ADMIN Trânsito - NOVO AUTO DE INFRAÇÃO")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        ##############################################################################################################
        # VARIÁVEIS DE INICIALIZAÇÃO
        ##############################################################################################################
        talao_select = tk.StringVar(self, "Municipio")

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
                                    variable=talao_select)
        municipal.grid(row=0, column=1, pady=5, padx=5)
        estadual = ttk.Radiobutton(linha1, text="Estadual", value="Estado",
                                   variable=talao_select)
        estadual.grid(row=0, column=2, pady=5, padx=5)

        ##############################################################################################################
        linha2 = ttk.Frame(self)
        linha2.pack(fill='x', padx=20, pady=15)
        lb_ait = ttk.Label(linha2, text="Nº AIT", font=('', 10, 'bold'))
        lb_ait.grid(row=0, column=0, sticky='w')
        ait = ttk.Entry(linha2, width=12, style="success")
        ait.grid(row=1, column=0)

        lb_condutor = ttk.Label(linha2, text="CONDUTOR", font=('', 10, 'bold'))
        lb_condutor.grid(row=0, column=1, sticky='w', padx=15)
        condutor = ttk.Entry(linha2, width=35)
        condutor.grid(row=1, column=1, padx=15)

        lb_local = ttk.Label(linha2, text="LOCAL", font=('', 10, 'bold'))
        lb_local.grid(row=0, column=2, sticky='w')
        local = ttk.Entry(linha2, width=45)
        local.grid(row=1, column=2)

        ##############################################################################################################
        linha3 = ttk.Frame(self)
        linha3.pack(fill='x', padx=20)
        lb_data = ttk.Label(linha3, text='DATA', font=('', 10, 'bold'))
        lb_data.grid(row=0, column=0, sticky='w')
        data = DateEntry(linha3, style='warning', width=12)
        data.grid(row=1, column=0)

        lb_hora = ttk.Label(linha3, text="HORA", font=('', 10, 'bold'))
        lb_hora.grid(row=0, column=1, sticky='w', padx=15)
        hora = ttk.Entry(linha3, width=6)
        hora.grid(row=1, column=1)

        lb_re = ttk.Label(linha3, text="RE PM", font=('', 10, 'bold'))
        lb_re.grid(row=0, column=2, sticky='w')
        re = ttk.Entry(linha3, width=9)
        re.grid(row=1, column=2)

        lb_codigo = ttk.Label(linha3, text="COD. ENQ.", font=('', 10, 'bold'))
        lb_codigo.grid(row=0, column=3, sticky='w', padx=25)
        codigo = ttk.Entry(linha3, width=9, style='secondary')
        codigo.grid(row=1, column=3, padx=25)

        lb_competencia = ttk.Label(linha3, text='COMPETENCIA', font=('', 10, 'bold'))
        lb_competencia.grid(row=0, column=4, sticky='w')
        competencia = ttk.Label(linha3, text='  Compentencia', background='#17a2b8', width=30)
        competencia.grid(row=1, column=4, ipady=3)

        ##############################################################################################################
        linha4 = ttk.Frame(self)
        linha4.pack(fill='x', padx=20, pady=15)
        artigo = ttk.Label(linha4, text='  Artigo do auto de infração de transito', background='#17a2b8', width=100)
        artigo.grid(row=0, column=0, ipady=3, sticky='w')

        linha5 = ttk.Frame(self)
        linha5.pack(fill='x', padx=20)
        lb_crr = ttk.Label(linha5, text="CRR", font=('', 10, 'bold'))
        lb_crr.grid(row=0, column=0, sticky='w')
        crr = ttk.Entry(linha5, width=10)
        crr.grid(row=1, column=0)

        lb_recolha = ttk.Label(linha5, text="VEÍC. REC.", font=('', 10, 'bold'))
        lb_recolha.grid(row=0, column=1, padx=15, sticky='w')
        recolha = ttk.Combobox(linha5, width=10, values=['NÃO', 'SIM'], state='readonly')
        recolha.grid(row=1, column=1, padx=15)
        recolha.set('NÃO')


        ##############################################################################################################
        # BIND
        ##############################################################################################################
        local.bind('<KeyRelease>', (lambda event: autocomplete_logradouro(local, local.get())))
        data.entry.bind('<KeyRelease>', lambda event: data_mask(data, data.entry.get()))
        hora.bind('<KeyRelease>', lambda event: hora_mask(hora, hora.get()))
        codigo.bind('<KeyRelease>', lambda event: codigo_mask(codigo, codigo.get()))
        # self.codigo.bind('<FocusOut>', lambda event: verifica_enquadramento(self.codigo, self.codigo.get()))
