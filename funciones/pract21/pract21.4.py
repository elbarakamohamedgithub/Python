def itemsiguals(lista1, lista2):
    listaiguals = []
    for i in lista1:
        for j in lista2:
            if j == i and j not in listaiguals:
                listaiguals.append(i)
    return listaiguals

print(itemsiguals([1,2,3,4],[2,5,3,4,2,4]))



