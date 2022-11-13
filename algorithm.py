def algoritmo_a_star(grafo):
    x = 0
    suma = 0
    suma2 = 0
    suma_l = []
    lista = []
    lista_n = []
    lista.append(grafo[0][0])
    while(len(grafo) >= 1):
        if (grafo[x][0] == lista[-1]):
            suma += grafo[x][2]
            suma_l.append(grafo[x][2])
            l_suma = grafo[x][2]
            lista.append(grafo[x][1])
            grafo.pop(x)
            if (lista[-1] == 'G'):
                if (suma2):
                    if (suma > suma2):
                        suma = suma2
                        lista = lista_n.copy()
                else:
                    lista_n = lista.copy()
                    suma2 = suma
                    x = 0
        elif (x == len(grafo) - 1):
            lista.pop(-1)
            suma -= suma_l[-1]
            suma_l.pop(-1)
            x = 0
        else:
            x+=1
    if (suma > suma2):
        suma = suma2
        lista = lista_n
    return (suma, lista)
