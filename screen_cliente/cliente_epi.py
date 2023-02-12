from imports import *
from functions.functions import data_mask, data_pt, data_us
from classes.cl_epi import *


class ClienteEpi(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 650, 350)
        self.geometry(geo)
        self.title("ADMIN - EPI")
        # self.iconbitmap("ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        # Inicia configurações da GUI
        self.dados = Epi().set_epi(CLIENTE.re)

        # INFO DO CLIENTE
        self.cliente = ttk.Frame(self)
        self.cliente.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.20)
        self.lcliente = ttk.Label(self.cliente, font=('', 14),
                                  text=f"EPI\n"
                                       f"{CLIENTE.graduacao_txt} "
                                       f"{CLIENTE.re}-{CLIENTE.dc} "
                                       f"{CLIENTE.nome}")
        self.lcliente.pack()

        # FORMULÁRIO
        self.form = ttk.Frame(self)
        self.form.place(relx=0.05, rely=0.28, relwidth=0.93, relheight=0.80)

        self.linha1 = ttk.Frame(self.form)
        self.linha1.pack(fill='x', anchor='w', pady=10)
        self.lb_arma = ttk.Label(self.linha1, text='Nº Arma')
        self.lb_arma.grid(row=0, column=0, sticky='w')
        self.arma = ttk.Entry(self.linha1)
        self.arma.grid(row=1, column=0)
        self.lb_colete = ttk.Label(self.linha1, text='Nº Colete')
        self.lb_colete.grid(row=0, column=1, padx=10, sticky='w')
        self.colete = ttk.Entry(self.linha1)
        self.colete.grid(row=1, column=1, padx=10)
        self.lb_validade_colete = ttk.Label(self.linha1, text='Validade Colete')
        self.lb_validade_colete.grid(row=0, column=2, sticky='w')
        self.validade_colete = DateEntry(self.linha1, bootstyle='success')
        self.validade_colete.grid(row=1, column=2)

        self.linha2 = ttk.Frame(self.form)
        self.linha2.pack(fill='x', anchor='w', pady=10)
        self.lb_algemas = ttk.Label(self.linha2, text='Nº Algemas')
        self.lb_algemas.grid(row=0, column=0, sticky='w')
        self.algemas = ttk.Entry(self.linha2)
        self.algemas.grid(row=1, column=0)
        self.lb_tonfa = ttk.Label(self.linha2, text='Carga Tonfa?')
        self.lb_tonfa.grid(row=0, column=2, sticky='w', padx=10)
        self.tonfa = ttk.Combobox(self.linha2, values=['SIM', 'NÃO'], state='readonly',
                                  font=('', 12), width=5)
        self.tonfa.grid(row=1, column=2, padx=10)
        self.tonfa.set('NÃO')
        self.lb_espargidor = ttk.Label(self.linha2, text='Nº Espargidor')
        self.lb_espargidor.grid(row=0, column=3, sticky='w', padx=10)
        self.espargidor = ttk.Entry(self.linha2)
        self.espargidor.grid(row=1, column=3, padx=10)
        self.lb_validade_espargidor = ttk.Label(self.linha2, text='Validade Espargidor')
        self.lb_validade_espargidor.grid(row=0, column=4, sticky='w')
        self.validade_espargidor = DateEntry(self.linha2, bootstyle='info')
        self.validade_espargidor.grid(row=1, column=4)

        self.linha3 = ttk.Frame(self.form)
        self.linha3.pack(fill='x', pady=15)
        self.bt_salvar = ttk.Button(self.linha3, text='SALVAR', style='success', width=35, command=self.salvar)
        self.bt_salvar.grid(row=0, column=0)
        self.lb_msg = ttk.Label(self.linha3, text='', font=('', 12, 'bold'), style='warning')
        self.lb_msg.grid(row=0, column=1, padx=40)

        ##############################################################################################################
        # BIND
        ##############################################################################################################
        self.validade_colete.entry.bind('<KeyRelease>', lambda event: data_mask(self.validade_colete,
                                                                                self.validade_colete.entry.get()))
        self.validade_espargidor.entry.bind('<KeyRelease>',
                                            lambda event: data_mask(self.validade_espargidor,
                                                                    self.validade_espargidor.entry.get()))

        self.preenche_form()

    def preenche_form(self):
        dados_epi = Epi().set_epi(CLIENTE.re)
        if dados_epi:
            self.arma.insert(0, dados_epi.arma)
            self.colete.insert(0, dados_epi.colete)
            self.validade_colete.entry.delete(0, 'end')
            self.validade_colete.entry.insert(0, data_pt(dados_epi.validade_colete))
            self.algemas.insert(0, dados_epi.algemas)
            self.tonfa.set(dados_epi.tonfa)
            self.espargidor.insert(0, dados_epi.espargidor)
            self.validade_espargidor.entry.delete(0, 'end')
            self.validade_espargidor.entry.insert(0, data_pt(dados_epi.validade_espargidor))
        else:
            print('dados não encontrados')

    def salvar(self):
        if not self.dados:
            novo = self.coleta_form()
            try:
                novo.insert_epi()
                self.lb_msg['text'] = "DADOS SALVOS!!!!"
                self.dados = Epi().set_epi(CLIENTE.re)
            except SystemError:
                self.lb_msg['text'] = "Erro ao gravar NOVO!"
        elif self.dados:
            atualiza = self.coleta_form()
            try:
                atualiza.update_epi()
                self.lb_msg['text'] = "DADOS ATUALIZADOS!"
            except SystemError:
                self.lb_msg['text'] = "Erro ao atualizar!!!"

    def coleta_form(self):
        dados_form = Epi()
        dados_form.re = CLIENTE.re
        dados_form.arma = self.arma.get().upper()
        dados_form.colete = self.colete.get().upper()
        dados_form.validade_colete = data_us(self.validade_colete.entry.get())
        dados_form.algemas = self.algemas.get().upper()
        dados_form.tonfa = self.tonfa.get()
        dados_form.espargidor = self.espargidor.get().upper()
        dados_form.validade_espargidor = data_us(self.validade_espargidor.entry.get())
        return dados_form
