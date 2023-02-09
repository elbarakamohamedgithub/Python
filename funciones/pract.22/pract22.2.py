def posicioLletra(paraula, lletra):
    for i in range(len(paraula)):
        if paraula[i] == lletra:
            return i

print(posicioLletra("mohamde","d"))