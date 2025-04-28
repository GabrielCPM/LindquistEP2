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


    
