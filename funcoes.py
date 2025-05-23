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
            c = 0
            i += 1
        if c == 3: #se c chegar a 3 (sequencia de 4 numeros presente na lista) loop para
            break
    if c == 3: #se c for 3 a sequencia existe e retorna 15 pontos
        return 15
    else: #se nao existir retorna 0 (so pode ser 3 ou menor que 3 por causa do break no loop)
        return 0
    
def calcula_pontos_sequencia_alta (lista_dados):
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
            c = 0
            i += 1
        if c == 4: #se c chegar a 3 (sequencia de 4 numeros presente na lista) loop para
            break
    if c == 4: #se c for 3 a sequencia existe e retorna 15 pontos
        return 30
    else: #se nao existir retorna 0 (so pode ser 3 ou menor que 3 por causa do break no loop)
        return 0
    
def calcula_pontos_full_house (lista_dados):
    lista_ordenada = sorted(lista_dados)
    if lista_ordenada[0] == lista_ordenada[1] and lista_ordenada[1] == lista_ordenada[2] and lista_ordenada[2] == lista_ordenada[3] and lista_ordenada[3] == lista_ordenada[4]:
        return 0
    if lista_ordenada[0] == lista_ordenada [1] and lista_ordenada [1] == lista_ordenada[2]:
        trinca = True
        if lista_ordenada[3] == lista_ordenada[4]:
            dupla = True
        else:
            dupla = False
    else:
        if lista_ordenada[2] == lista_ordenada [3] and lista_ordenada [3] == lista_ordenada[4]:
            trinca = True
            if lista_ordenada[0] == lista_ordenada[1]:
                dupla = True
            else:
                dupla = False
        else:
            trinca = False
    if trinca == True and dupla == True:
        resultado = lista_ordenada[0]+lista_ordenada[1]+lista_ordenada[2]+lista_ordenada[3]+lista_ordenada[4]
    else:
        resultado = 0
    return resultado

def calcula_pontos_quadra (lista_dados):
    i = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    while i < len(lista_dados):
        if lista_dados[i] == 1:
            c1 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 2:
            c2 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 3:
            c3 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 4:
            c4 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 5:
            c5 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 6:
            c6 += 1
            i += 1
        else:
            i += 1
    i = 0
    soma = 0
    if c1 >= 4 or c2 >= 4 or c3 >= 4 or c4 >= 4 or c5 >= 4 or c6 >= 4:
        while i < len(lista_dados):
            soma += lista_dados[i]
            i += 1
        return soma
    else:
        return 0

def calcula_pontos_quina (lista_dados):
    i = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    while i < len(lista_dados):
        if lista_dados[i] == 1:
            c1 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 2:
            c2 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 3:
            c3 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 4:
            c4 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 5:
            c5 += 1
            i += 1
        else:
            i += 1
    i = 0
    while i < len(lista_dados):
        if lista_dados[i] == 6:
            c6 += 1
            i += 1
        else:
            i += 1
    if c1 >= 5 or c2 >= 5 or c3 >= 5 or c4 >= 5 or c5 >= 5 or c6 >= 5:
        return 50
    else:
        return 0

def calcula_pontos_regra_avancada (lista_dados):
    dicio_pontuacoes = {'cinco_iguais': 0, 'full_house': 0, 'quadra': 0, 'sem_combinacao': 0, 'sequencia_alta': 0, 'sequencia_baixa': 0}
    dicio_pontuacoes['cinco_iguais'] = calcula_pontos_quina(lista_dados)
    dicio_pontuacoes['full_house'] = calcula_pontos_full_house(lista_dados)
    dicio_pontuacoes['quadra'] = calcula_pontos_quadra(lista_dados)
    dicio_pontuacoes['sem_combinacao'] = calcula_pontos_soma(lista_dados)
    dicio_pontuacoes['sequencia_alta'] = calcula_pontos_sequencia_alta(lista_dados)
    dicio_pontuacoes['sequencia_baixa'] = calcula_pontos_sequencia_baixa(lista_dados)
    return dicio_pontuacoes

def faz_jogada(lista_dados, categoria, cartela_de_pontos):
    if categoria in ['1', '2', '3', '4', '5', '6']:
        pontos_simples = calcula_pontos_regra_simples(lista_dados)
        cartela_de_pontos['regra_simples'][int(categoria)] = pontos_simples[int(categoria)]
    elif categoria in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']:
        pontos_avancados = calcula_pontos_regra_avancada(lista_dados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)