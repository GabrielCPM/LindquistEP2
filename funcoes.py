from random import randint
def rolar_dados (dados):
    lista_valores =[]
    i = 0
    while i < dados:
        lista_valores.append(randint(1,6))
        i += 1
    return lista_valores

def guardar_dado (lista_rodados, lista_guardados, indice):
    lista_ex2 = []
    lista_guardados.append(lista_rodados[indice])
    del lista_rodados[indice]
    lista_ex2.append(lista_rodados)
    lista_ex2.append(lista_guardados)

    return lista_ex2

def remover_dado (dados_rolados, dados_guardados,dado_remover):
    lista_guardados = []
    lista_final = []
    for i in range(dados_guardados):
        if i == dado_remover:
            dados_rolados.append(dados_guardados[dado_remover])
        else:
            lista_guardados.append(dados_guardados[i])
    lista_final.append(dados_rolados)
    lista_final.append(lista_guardados)


    return lista_final
