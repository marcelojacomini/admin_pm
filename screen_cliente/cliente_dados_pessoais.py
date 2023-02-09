import tkinter as tk
import ttkbootstrap as ttk
from functions.tk_center import tk_center
from ttkbootstrap import DateEntry

from classes.cl_dados_pessoais import *

from functions.globals import *
from functions.functions import format_cpf, cpf_mask, data_pt, data_us, data_mask


class ClienteDadosPessoais(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 750, 560)
        self.geometry(geo)
        self.title("ADMIN - ENDEREÇO PM")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        # Inicia configurações da GUI
        self.dados = DadosPessoais().set_dados_pessoais(cliente_global.re)

        # INFO DO CLIENTE
        self.cliente = ttk.Frame(self)
        self.cliente.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.10)
        self.lcliente = ttk.Label(self.cliente, font=('', 14),
                                  text=f"Dados Pessoais de\n"
                                       f"{cliente_global.graduacao_txt} "
                                       f"{cliente_global.re}-{cliente_global.dc} "
                                       f"{cliente_global.nome}")
        self.lcliente.pack()

        # FORMULÁRIO
        self.form = ttk.Frame(self)
        self.form.place(relx=0.05, rely=0.18, relwidth=0.93, relheight=0.80)
        self.re = ttk.Entry(self)
        self.re.insert(0, cliente_global.re)

        self.linha1 = ttk.Frame(self.form)
        self.linha1.pack(fill='x', anchor='w', pady=10)
        self.lb_cpf = ttk.Label(self.linha1, text='CPF')
        self.lb_cpf.grid(row=0, column=0, sticky='w')
        self.cpf = ttk.Entry(self.linha1)
        self.cpf.grid(row=1, column=0)
        self.lb_rg = ttk.Label(self.linha1, text='RG')
        self.lb_rg.grid(row=0, column=1, padx=10, sticky='w')
        self.rg = ttk.Entry(self.linha1)
        self.rg.grid(row=1, column=1, padx=10)
        self.lb_nascimento = ttk.Label(self.linha1, text='Data Nascimento')
        self.lb_nascimento.grid(row=0, column=2, sticky='w')
        self.nascimento = DateEntry(self.linha1, bootstyle='success')
        self.nascimento.grid(row=1, column=2)

        self.linha2 = ttk.Frame(self.form)
        self.linha2.pack(fill='x', anchor='w', pady=10)
        self.lb_cnh = ttk.Label(self.linha2, text='Número CNH')
        self.lb_cnh.grid(row=0, column=0, sticky='w')
        self.cnh = ttk.Entry(self.linha2)
        self.cnh.grid(row=1, column=0)
        self.lb_validade_cnh = ttk.Label(self.linha2, text='Validade')
        self.lb_validade_cnh.grid(row=0, column=1, sticky='w', padx=10)
        self.validade_cnh = DateEntry(self.linha2, bootstyle='primary')
        self.validade_cnh.grid(row=1, column=1, padx=10)
        self.lb_categoria = ttk.Label(self.linha2, text='Cat. CNH')
        self.lb_categoria.grid(row=0, column=2, sticky='w')
        self.categoria = ttk.Combobox(self.linha2, values=list_categoria, state='readonly',
                                      font=('', 12), width=5)
        self.categoria.grid(row=1, column=2)
        self.lb_sat = ttk.Label(self.linha2, text='Cat. SAT')
        self.lb_sat.grid(row=0, column=3, sticky='w', padx=10)
        self.sat = ttk.Combobox(self.linha2, values=list_categoria, state='readonly',
                                font=('', 12), width=5)
        self.sat.grid(row=1, column=3, padx=10)

        self.linha3 = ttk.Frame(self.form)
        self.linha3.pack(fill='x', anchor='w', pady=10)
        self.lb_nat = ttk.Label(self.linha3, text='Local de Nascimento')
        self.lb_nat.grid(row=0, column=0, sticky='w')
        self.nat = ttk.Entry(self.linha3, width=50)
        self.nat.grid(row=1, column=0)
        self.lb_uf = ttk.Label(self.linha3, text='UF')
        self.lb_uf.grid(row=0, column=1, padx=10)
        self.uf = ttk.Combobox(self.linha3, values=list_uf, state='readonly',
                               font=('', 10), width=5)
        self.uf.grid(row=1, column=1, padx=10)
        self.uf.set('SP')

        self.linha4 = ttk.Frame(self.form)
        self.linha4.pack(fill='x', anchor='w')
        self.lb_rua = ttk.Label(self.linha4, text='Logradouro')
        self.lb_rua.grid(row=0, column=0, pady=10, sticky='w')
        self.rua = ttk.Entry(self.linha4, width=50)
        self.rua.grid(row=1, column=0)
        self.lb_numero = ttk.Label(self.linha4, text='Número')
        self.lb_numero.grid(row=0, column=1, sticky='w', padx=10)
        self.numero = ttk.Entry(self.linha4)
        self.numero.grid(row=1, column=1, padx=10)
        self.lb_complemento = ttk.Label(self.linha4, text='Complemento')
        self.lb_complemento.grid(row=0, column=2, sticky='w')
        self.complemento = ttk.Entry(self.linha4, width=30)
        self.complemento.grid(row=1, column=2)

        self.linha5 = ttk.Frame(self.form)
        self.linha5.pack(fill='x', anchor='w', pady=10)
        self.lb_bairro = ttk.Label(self.linha5, text='Bairro')
        self.lb_bairro.grid(row=0, column=0, sticky='w')
        self.bairro = ttk.Entry(self.linha5, width=40)
        self.bairro.grid(row=1, column=0)
        self.lb_cidade = ttk.Label(self.linha5, text='Cidade')
        self.lb_cidade.grid(row=0, column=1, padx='10', sticky='w')
        self.cidade = ttk.Entry(self.linha5, width=40)
        self.cidade.grid(row=1, column=1, padx='10')

        self.linha6 = ttk.Frame(self.form)
        self.linha6.pack(fill='x', pady=15)
        self.bt_salvar = ttk.Button(self.linha6, text='SALVAR', style='success', width=35, command=self.salvar)
        self.bt_salvar.grid(row=0, column=0)
        self.lb_msg = ttk.Label(self.linha6, text='', font=('', 12, 'bold'), style='warning')
        self.lb_msg.grid(row=0, column=1, padx=40)

        ##############################################################################################################
        # BIND
        ##############################################################################################################
        self.cpf.bind('<KeyRelease>', lambda event: cpf_mask(self.cpf, self.cpf.get()))
        self.cpf.bind('<FocusOut>', lambda event: format_cpf(self.cpf, self.cpf.get()))
        self.nascimento.entry.bind('<KeyRelease>', lambda event: data_mask(self.nascimento,
                                                                           self.nascimento.entry.get()))
        self.validade_cnh.entry.bind('<KeyRelease>', lambda event: data_mask(self.validade_cnh,
                                                                             self.validade_cnh.entry.get()))

        self.preenche_form()

    def preenche_form(self):
        dados_pessoais = DadosPessoais().set_dados_pessoais(cliente_global.re)
        if dados_pessoais:
            self.cpf.insert(0, dados_pessoais.cpf)
            self.rg.insert(0, dados_pessoais.rg)
            self.nascimento.entry.delete(0, 'end')
            self.nascimento.entry.insert(0, data_pt(dados_pessoais.nascimento))
            self.cnh.insert(0, dados_pessoais.cnh)
            self.validade_cnh.entry.delete(0, 'end')
            self.validade_cnh.entry.insert(0, data_pt(dados_pessoais.validade))
            self.categoria.set(dados_pessoais.categoria)
            self.sat.set(dados_pessoais.sat)
            self.nat.insert(0, dados_pessoais.nat)
            self.uf.set(dados_pessoais.uf)
            self.rua.insert(0, dados_pessoais.rua)
            self.numero.insert(0, dados_pessoais.numero)
            self.complemento.insert(0, dados_pessoais.complemento)
            self.bairro.insert(0, dados_pessoais.bairro)
            self.cidade.insert(0, dados_pessoais.cidade)
        else:
            print('dados não encontrados')

    def salvar(self):
        if not self.dados:
            novo = self.coleta_form()
            try:
                novo.insert_dados_pessoais()
                self.lb_msg['text'] = "DADOS SALVOS!!!!"
                self.dados = DadosPessoais().set_dados_pessoais(cliente_global.re)
            except SystemError:
                self.lb_msg['text'] = "Erro ao gravar NOVO!"
        elif self.dados:
            atualiza = self.coleta_form()
            try:
                atualiza.update_dados_pessoais()
                self.lb_msg['text'] = "DADOS ATUALIZADOS!"
            except SystemError:
                self.lb_msg['text'] = "Erro ao atualizar!!!"

    def coleta_form(self):
        dados_form = DadosPessoais()
        dados_form.re = cliente_global.re
        dados_form.cpf = self.cpf.get()
        dados_form.rg = self.rg.get().upper()
        dados_form.nascimento = data_us(self.nascimento.entry.get())
        dados_form.cnh = self.cnh.get()
        dados_form.validade = data_us(self.validade_cnh.entry.get())
        dados_form.categoria = self.categoria.get()
        dados_form.sat = self.sat.get()
        dados_form.nat = self.nat.get().upper()
        dados_form.uf = self.uf.get()
        dados_form.rua = self.rua.get().upper()
        dados_form.numero = self.numero.get().upper()
        dados_form.complemento = self.complemento.get().upper()
        dados_form.bairro = self.bairro.get().upper()
        dados_form.cidade = self.cidade.get().upper()
        return dados_form
