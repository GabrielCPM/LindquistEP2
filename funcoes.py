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
    for i in range(len(dados_guardados)):
        if i == dado_remover:
            dados_rolados.append(dados_guardados[i])
        else:
            lista_guardados.append(dados_guardados[i])
    lista_final.append(dados_rolados)
    lista_final.append(lista_guardados)


    return lista_final

def calcula_pontos_regra_simples (lista_dados):
    dPontos = {}
    for i in range (len(lista_dados)):
        if lista_dados[i] == 1:
            dPontos[1] += 1
        if lista_dados[i] == 2:
            dPontos[2] += 1
        if lista_dados[i] == 3:
            dPontos[3] += 1
        if lista_dados[i] == 4:
            dPontos[4] += 1
        if lista_dados[i] == 5:
            dPontos[5] += 1
        if lista_dados[i] == 6:
            dPontos[6] += 1 
    return dPontos