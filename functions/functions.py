import hashlib
from datetime import datetime


def tk_center(master, largura, altura):
    w = master.winfo_screenwidth()
    h = master.winfo_screenheight()
    px = int(w/2 - largura/2)
    py = int(h/2 - altura/2)
    return f'{largura}x{altura}+{px}+{py}'


def pass_converter(password):
    # encode the password string to bytes
    password_bytes = password.encode('utf-8')
    # create the hash object
    m = hashlib.md5(password_bytes)
    # return the converted password
    return m.hexdigest()


###########################################################################################
# FORMATAÇÃO DE DATAS STRING
###########################################################################################
def data_atual_pt():
    return datetime.now().strftime("%d/%m/%Y")


def inicio_mes_pt():
    return datetime.now().strftime("01/%m/%Y")


def ano_atual():
    return datetime.now().strftime("%Y")


def mes_atual():
    return datetime.now().strftime("%m")


def data_us(data):
    data = str(data)
    return f"{data[6]}{data[7]}{data[8]}{data[9]}-{data[3]}{data[4]}-{data[0]}{data[1]}"


def data_pt(data):
    data = str(data)
    return f"{data[8]}{data[9]}/{data[5]}{data[6]}/{data[0]}{data[1]}{data[2]}{data[3]}"


###########################################################################################
# MASCARAS DE ENTRADA
###########################################################################################
# VERIFICA SE UM VALOR DIGITÁDO É NÚMERO
def is_number(numero):
    try:
        int(numero)
        return True
    except Exception as e:
        print(e)
        return False


def re_mask(campo, texto):
    if len(texto) >= 6:
        campo.delete(6, "end")
    elif not is_number(texto):
        campo.delete((len(texto) - 1), 'end')


def cpf_mask(campo, texto):
    if len(texto) >= 11:
        campo.delete(11, "end")
    elif not is_number(texto):
        campo.delete((len(texto) - 1), 'end')


def dc_mask(campo, texto):
    if len(texto) >= 1:
        campo.delete(1, "end")


def data_mask(campo, texto):
    if len(texto) == 2 or len(texto) == 5:
        campo.entry.insert("end", "/")
    if len(texto) >= 10:
        campo.entry.delete(10, "end")


def hora_mask(campo, texto):
    if len(texto) == 2:
        campo.insert("end", ":")


def format_cpf(campo, texto):
    if len(texto) == 11:
        campo['foreground'] = 'white'
        campo.insert(3, '.')
        campo.insert(7, '.')
        campo.insert(11, '-')


def formatar_moeda(valor):
    valor = f"{valor:_.2f}".replace('.', ',').replace('_', '.')
    return valor


###########################################################################################
# FUNÇÕES PARA ENTRADA DE CONTATOS
###########################################################################################
def contato_mask(tipo, campo, texto):
    if tipo == '1-Telefone':
        if len(texto) >= 11:
            campo.delete(11, "end")
        elif not is_number(texto):
            campo.delete((len(texto) - 1), 'end')


def format_telefone(tipo, campo, texto):
    if tipo == '1-Telefone':
        if len(texto) == 9:
            campo['foreground'] = 'white'
            campo.insert(0, '15-')
            campo.insert(8, '-')
        if len(texto) == 8:
            campo['foreground'] = 'white'
            campo.insert(0, '15-')
            campo.insert(7, '-')
        if len(texto) == 11:
            campo['foreground'] = 'white'
            campo.insert(2, '-')
            campo.insert(8, '-')
        if len(texto) == 10:
            campo['foreground'] = 'white'
            campo.insert(2, '-')
            campo.insert(7, '-')
        if len(texto) < 8:
            campo['foreground'] = 'red'


###########################################################################################################
# COMPARA VALIDADE
###########################################################################################################
def verifica_validade(dt):
    validade = dt.strftime('%d/%m/%Y')
    validade = datetime.strptime(validade, '%d/%m/%Y')
    hoje = datetime.now().strftime('%d/%m/%Y')
    hoje = datetime.strptime(hoje, '%d/%m/%Y')
    if validade > hoje:
        return "OK"
    else:
        return "Vencida"
