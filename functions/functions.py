from tkinter import messagebox
from datetime import datetime


###########################################################################################
# MESSAGE BOX
###########################################################################################
def mensagem(header, texto):
    messagebox.showinfo(title=header, message=texto)


def confirmacao(header, quest):
    msg_box = messagebox.askyesno(header, quest, icon='warning')
    return msg_box


###########################################################################################
# FORMATAÇÃO DE DATAS STRING
###########################################################################################
def data_atual_pt():
    return datetime.now().strftime("%d/%m/%Y")


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
    except:
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


def codigo_mask(campo, texto):
    if len(texto) >= 6:
        campo.delete(5, "end")
    elif not is_number(texto):
        campo.delete((len(texto) - 1), 'end')

def format_cpf(campo, texto):
    if len(texto) == 11:
        campo['foreground'] = 'white'
        campo.insert(3, '.')
        campo.insert(7, '.')
        campo.insert(11, '-')


###########################################################################################
# FUNÇÕES PARA ENTRADA DE CONTATOS
###########################################################################################
def contato_mask(tipo, campo, texto):
    if tipo == 'Telefone':
        if len(texto) >= 11:
            campo.delete(11, "end")
        elif not is_number(texto):
            campo.delete((len(texto) - 1), 'end')


def format_telefone(tipo, campo, texto):
    if tipo == 'Telefone':
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
def verifica_validade(dt):
    validade = dt.strftime('%d/%m/%Y')
    validade = datetime.strptime(validade, '%d/%m/%Y')
    hoje = datetime.now().strftime('%d/%m/%Y')
    hoje = datetime.strptime(hoje, '%d/%m/%Y')
    if validade > hoje:
        return "OK"
    else:
        return "Vencida"
