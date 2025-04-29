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
    dPontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range (len(lista_dados)):
        if lista_dados[i] == 1:
            dPontos[1] += 1
        if lista_dados[i] == 2:
            dPontos[2] += 2
        if lista_dados[i] == 3:
            dPontos[3] += 3
        if lista_dados[i] == 4:
            dPontos[4] += 4
        if lista_dados[i] == 5:
            dPontos[5] += 5
        if lista_dados[i] == 6:
            dPontos[6] += 6
    
    return dPontos

def calcula_pontos_soma (lista_dados):
    soma = 0 
    for i in range(len(lista_dados)):
        soma += lista_dados[i]
    return soma

def calcula_pontos_sequencia_baixa (lista_dados):
    lista_em_ordem = sorted(lista_dados) #coloca a lista em ordem crescente
    i = 0 #indice
    c = 0 #contador
    if len(lista_em_ordem) < 4:
        return 0
    while i < len(lista_em_ordem)-1: #loop que verifica ate o penultimo termo da sequencia em relacao ao ultimo
        if lista_em_ordem[i] == lista_em_ordem[i+1]-1: #se o termo eh um menor que o proximo
            c += 1 
            i += 1
        elif lista_em_ordem[i] == lista_em_ordem[i+1]: #se o termo eh igual ao proximo
            i += 1
        elif lista_em_ordem[i] < lista_em_ordem[i+1]-1: #se o termo seguinte for dois ou mais maior 
            i += 1
        if c == 3: #se c chegar a 3 (sequencia de 4 numeros presente na lista) loop para
            break
    if c == 3: #se c for 3 a sequencia existe e retorna 15 pontos
        return 15
    else: #se nao existir retorna 0 (so pode ser 3 ou menor que 3 por causa do break no loop)
        return 0
