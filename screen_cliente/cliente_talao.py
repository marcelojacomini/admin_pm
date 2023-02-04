import tkinter as tk
import ttkbootstrap as ttk
from functions.tk_center import tk_center
from functions.globals import cliente_global

from classes_transito.tr_talao import *


class ClienteTalao(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 450, 350)
        self.geometry(geo)
        self.title("ADMIN - TALONÁRIO DE INFRAÇÕES")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.focus_set()
        self.grab_set()

        # Inicia configurações da GUI
        self.tl_atual = Talao().set_talonario(cliente_global.re)

        # INFO DO CLIENTE
        self.cliente = ttk.Frame(self)
        self.cliente.pack(fill='x', padx=10, pady=10)
        self.lcliente = ttk.Label(self.cliente, font=('', 10),
                                  text=f"Talonário de Infrações\n"
                                       f"{cliente_global.graduacao_txt} "
                                       f"{cliente_global.re}-{cliente_global.dc} "
                                       f"{cliente_global.nome}")
        self.lcliente.pack(fill='x')

        form = ttk.Frame(self)
        form.pack(fill='x', pady=20, padx=10)
        lb_municipal = ttk.Label(form, text='Talão Municipal - nº inicial: ')
        lb_municipal.grid(row=0, column=0, sticky='e')
        self.municipal_inicio = ttk.Entry(form, width=10)
        self.municipal_inicio.grid(row=0, column=1)
        self.municipal_inicio.insert(0, self.tl_atual.mi)
        lb_ao = ttk.Label(form, text=" ao ")
        lb_ao.grid(row=0, column=2)
        self.municipal_fim = ttk.Entry(form, width=10)
        self.municipal_fim.grid(row=0, column=3)
        self.municipal_fim.insert(0, self.tl_atual.mf)

        lb_estadual = ttk.Label(form, text='Talão Estadual - nº inicial: ')
        lb_estadual.grid(row=1, column=0, pady=20, sticky='e')
        self.estadual_inicio = ttk.Entry(form, width=10)
        self.estadual_inicio.grid(row=1, column=1)
        self.estadual_inicio.insert(0, self.tl_atual.ei)
        lb_ao = ttk.Label(form, text=" ao ")
        lb_ao.grid(row=1, column=2)
        self.estadual_fim = ttk.Entry(form, width=10)
        self.estadual_fim.grid(row=1, column=3)
        self.estadual_fim.insert(0, self.tl_atual.ef)

        self.bt_atualizar = ttk.Button(self, text='ATUALIZAR TALÕES', style='secondary',
                                       command=self.atualiza_taloes)
        self.bt_atualizar.pack(fill='x', pady=20, padx=10)

        self.lb_msg = ttk.Label(self, text="")
        self.lb_msg.pack()

    def atualiza_taloes(self):
        self.tl_atual.mi = self.municipal_inicio.get()
        self.tl_atual.mf = self.municipal_fim.get()
        self.tl_atual.ei = self.estadual_inicio.get()
        self.tl_atual.ef = self.estadual_fim.get()
        if self.tl_atual.insert_talao():
            self.lb_msg['text'] = "Talonário atualizado!!!!"
        else:
            self.lb_msg['text'] = "Houve um erro ao atualizar o talonário!!!"
        self.bt_atualizar['state'] = "disabled"

