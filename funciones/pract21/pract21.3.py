def esalfabetica(paraula):
    ordenada = True
    for i in range(0, len(paraula)-1):
        if paraula[i] > paraula[i+1]:
            ordenada = False

    return ordenada
print(esalfabetica("amor"))

