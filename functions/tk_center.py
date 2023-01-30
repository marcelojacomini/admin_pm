
def tk_center(master, largura, altura):

    w = master.winfo_screenwidth()
    h = master.winfo_screenheight()

    px = int(w/2 - largura/2)
    py = int(h/2 - altura/2)
    return f'{largura}x{altura}+{px}+{py}'
