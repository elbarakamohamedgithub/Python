# dada una frase , vocales a mayusculas y consonantes a minusculas
def miniMayu(frase, resultado):
    vocales = "aeiou"
    resultado = " "
    if len(frase) == 0:
        return resultado
    else:
        if frase[0] in vocales:
            resultado +=  frase[0].upper()
            return miniMayu(frase[1:], resultado)
        else:
            resultado +=  frase[0].lower()
            return miniMayu(frase[1:], resultado)

frase = "fuck sapos hermanito"
resultado = ""
print(miniMayu(frase, resultado))

def deMayuAMinu(frase, resultado, i):
    vocales = "aeiou"
    if len(frase) == i:
        return resultado
    else:
        if frase[i] in vocales:
            resultado +=  frase[i].upper()
            return deMayuAMinu(frase, resultado, i+1)
        else:
            resultado +=  frase[i].lower()
            return deMayuAMinu(frase, resultado,i+1)
print(deMayuAMinu(frase,resultado,0))

# dada una frase, encontrar las veces que aparece una palabra
def encontrarPalabra(frase, palabra, resultado):
    if len(frase) == 0:
        return resultado
    else:
        if palabra == frase[0]:
            return encontrarPalabra(frase[1:], palabra, resultado+1)
        else:
            return encontrarPalabra(frase[1:], palabra, resultado)
        
frase = "la concha de tu madre"
palabra = "a"
print(encontrarPalabra(frase,palabra, 0))

# dada una frase, vocales al principio, consonantes al final
def principioFinal(frase, resultado,i):
    vocales ="aeiou"
    if len(resultado) == len(frase):
        return resultado
    else:
        if frase[i] in vocales:
            resultado = frase[i] + resultado
            return principioFinal(frase, resultado, i +1)
        else:
            resultado += frase[i]
            return principioFinal(frase, resultado, i +1)

frase = "carla"  
resultado = ""
print(principioFinal(frase, resultado, 0))  

#dado un string devolver una lista con todas las vocales
def vocalesString(frase, resultado):
    vocales = "aeiou"
    if len(frase) == 0:
        return resultado
    else:
        if frase[0] in vocales:
            resultado.append(frase[0])
            return vocalesString(frase[1:], resultado)
        else:
            return vocalesString(frase[1:], resultado)
frase = "la madre que te pario  a"
print(vocalesString(frase, []))

#dada una lista de numeros, calcular la suma de los numeros de la lista
def sumaNumeros(listanums, suma):
    if len(listanums) == 0:
        return suma
    else:
        return sumaNumeros(listanums[1:], suma + listanums[0])

listanums = [1,4,3,2,1]
suma = 0
print(sumaNumeros(listanums, suma))

#dada una lista de numeros, devolver una lista con los números pares 
def numerosPares(listanumeros, listapares):
    if len(listanumeros) == 0:
        return listapares
    else:
        if listanumeros[0]%2 == 0:
            listapares.append(listanumeros[0])
            return numerosPares(listanumeros[1:], listapares)
        else:
            return numerosPares(listanumeros[1:],listapares)

listanumeros = [4,2,5,6,4,6,7]
print(numerosPares(listanumeros, []))


#EJERCICIOS REPETIDOS
# dada una frase , vocales a mayusculas y consonantes a minusculas
def vocalesiCOnsonantes(frase, resultado):
    vocales = "aeiou"
    if len(frase) == 0:
        return resultado
    else:
        if frase[0] in vocales:
            return vocalesiCOnsonantes(frase[1:], resultado + frase[0].upper())
        else:
            return vocalesiCOnsonantes(frase[1:], resultado + frase[0].lower())

frase = "fuck sapos hermanito"
resultado = ""
print(vocalesiCOnsonantes(frase, resultado))

# dada una frase, encontrar las veces que aparece una palabra
def vecesPalabra(frase, palabra, resultado):
    if len(frase) == 0:
        return resultado
    else:
        if frase[0] == palabra:
            return vecesPalabra(frase[1:], palabra, resultado +1)
        else:
            return vecesPalabra(frase[1:], palabra, resultado)
frase = "marruecos va a pasar mamones"
print(vecesPalabra(frase, "m",0))

# dada una frase, vocales al principio, consonantes al final
def ordenVocales(frase, resultado):
    vocales = "aeiou"
    if len(frase) == 0:
        return resultado
    else:
        if frase[0] in vocales:
            resultado = frase[0] + resultado
            return ordenVocales(frase[1:], resultado)
        else:
            return ordenVocales(frase[1:], resultado + frase[0])
frase = "carle"  
resultado = ""
print(ordenVocales(frase, resultado))  

#dado un string devolver una lista con todas las vocales
def vocalesinString(frase, resultado):
    vocales = "aeiou"
    if len(frase) == 0:
        return resultado
    else:
        if frase[0] in vocales:
            resultado.append(frase[0])
            return vocalesinString(frase[1:], resultado)
        else:
            return vocalesinString(frase[1:], resultado)
frase = "la madre que te pario  a"
print(vocalesinString(frase, []))

#dada una lista de numeros, calcular la suma de los numeros de la lista
def sumaNumsLista(lista, resultat):
    if len(lista) == 0:
        return resultat
    else:
        return sumaNumsLista(lista[1:], resultat + lista[0])
lista = [1,4,3,2,1]
resultat = 0
print(sumaNumsLista(lista, resultat))

def cuentadelante(m,n):
    if m == n:
        print(m)
    else:
        print(m)
        cuentadelante(m+1, n)
print(cuentadelante(10,20))
