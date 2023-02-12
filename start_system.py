from imports import *


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        # INICIA A CLASSE PARA JANELA PRINCIPAL
        geo = tk_center(self, 280, 300)
        self.geometry(geo)
        self.title("ADMIN - LOGIN")
        self.iconbitmap("img/pm_ico.ico")
        self.resizable(False, False)
        self.st = ttk.Style()
        self.st.theme_use("darkly")

        frame_lg = ttk.Frame(self)
        frame_lg.pack(fill='x', pady=20)
        lb_login = ttk.Label(frame_lg, text='LOGIN', font=('', 16, 'bold'))
        lb_login.pack()

        frame_user = ttk.Frame(self)
        frame_user.pack(pady=10)
        lg_user = ttk.Label(frame_user, text='Usuário: ')
        lg_user.grid(row=0, column=0, padx=5, pady=10)
        self.user = ttk.Entry(frame_user)
        self.user.grid(row=0, column=1)
        lg_pass = ttk.Label(frame_user, text='Senha: ')
        lg_pass.grid(row=1, column=0, padx=5, pady=10)
        self.password = ttk.Entry(frame_user, show='*')
        self.password.grid(row=1, column=1)
        self.bt_acesso = ttk.Button(frame_user, text='ACESSAR', command=self.acessar)
        self.bt_acesso.grid(row=2, column=0, pady=15, columnspan=2, sticky='we')

        frame_msg = ttk.Frame(self)
        frame_msg.pack(fill='x', pady=10)
        self.lb_msg = ttk.Label(frame_msg, text='')
        self.lb_msg.pack()

    def acessar(self):
        user_session.user = self.user.get()
        user_session.password = self.password.get()
        login = user_session.set_user()
        if user_session.user:
            self.withdraw()
            App()
        else:
            self.lb_msg['text'] = "Usuário ou senha inválido"

log = Login()
log.mainloop()
