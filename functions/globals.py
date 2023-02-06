from classes.cl_cliente import Cliente
from classes_transito.tr_ait import Ait

# VARIÁVEL GLOBAL CRIADA PARA RECEBER INFORMAÇÕES TRANSITÓRIAS DE CLIENTE
cliente_global = Cliente()
# VARIÁVEL GLOBAL CRIADA PARA RECEBER INFORMAÇÕES TRANSITÓRIAS DE AIT
ait_global = Ait()

################################################################################################################
# TRATAMENTO DE GRADUAÇÕES PARA LISTA POR ANTIGUIDADE
################################################################################################################
# DICIONÁRIO CRIADO PARA CONVERSÃO DE INDICE DE GRADUAÇÃO
graduacoes = {
    "CEL PM": 1,
    "TEN-CEL PM": 2,
    "MAJ PM": 3,
    "CAP PM": 4,
    "1º TEN PM": 5,
    "2º TEN PM": 6,
    "ASP-OF PM": 7,
    "SUBTEN PM": 8,
    "1º SGT PM": 9,
    "2º SGT PM": 10,
    "3º SGT PM": 11,
    "CB PM": 12,
    "SD PM": 13
}
# LISTA DE GRADUAÇÕES UTILIZADA PARA COMBOBOX
list_grad = ["CEL PM", "TEN-CEL PM", "MAJ PM", "CAP PM", "1º TEN PM", "2º TEN PM", "ASP-OF PM",
             "SUBTEN PM", "1º SGT PM", "2º SGT PM", "3º SGT PM", "CB PM", "SD PM"]


# FUNÇÃO PARA CONVERSÃO DO TEXTO DA GRADUAÇÃO EM ÍNDICE NUMÉRICO
def indice_grad(grad):
    if grad in graduacoes:
        return graduacoes[grad]


# FIM GRADUAÇÕES

# LISTA TIPOS DE CONTATO
tipos_contato = ["1-Telefone", '2-e-mail funcional', '3-e-mail pessoal', '4-Outros']

# LISTA CRIADA PARA CATEGORIA CNH
list_categoria = ["A", "B", "C", "D", "E", "A-B", "A-C", "A-D", "A-E"]

# LISTA UNIDADE FEDERATIVA
list_uf = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MS', 'MT', 'MG', 'PA', 'PB', 'PR', 'PE',
           'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']


# PERIODO EAD
list_periodo_ead = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO',
                    'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']