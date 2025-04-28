from random import randint
def rolar_dados (dados):
    lista_valores =[]
    i = 0
    while i < dados:
        lista_valores.append(randint(1,6))
        i += 1
    return lista_valores


def guardar_dado (dados_rolados, dados_guardados, indice):
    dados_rodados= []
    for i in range (dados_rolados):
        if i == indice:
            dados_guardados.append(dados_rolados[i])
        else:
            dados_rodados.append(dados_rolados[i])
    lista_final = (dados_rolados, dados_guardados)
    return lista_final