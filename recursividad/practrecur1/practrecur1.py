#1
def restasSuccesives(numero, resta):
    if resta >= numero:
        return numero
    numero = numero - resta
    return restasSuccesives(numero , resta)

#print(restasSuccesives(23,7))  
    
#2
def sumarDigits(numero, suma):
    if numero == "":
        return suma
    numero = str(numero)
    return sumarDigits(numero[1:], suma + int(numero[0]))
print(sumarDigits(45657,0))

#3
def sumarElements(llista, suma):
    if len(llista) == 0:
        return suma
    return sumarElements(llista[1:], suma + llista[0])

#print(sumarElements([2,44353,34,34,34,2,2,3,13232,23,3,34,23],0))

#4
def potencia(x, y, resultado ):
    if y == 0:
        return resultado
    return potencia(x, y-1, resultado * x)

#print(potencia(3,6,1))

#5
def productoNumeros(n, y, resultado):
    if y <= 0:
        return resultado
    return productoNumeros(n, y -1, resultado + n)


#print(productoNumeros(10,6,0))            

#6
def multiplicarElements(array, resultat):
    if len(array) == 0:
        return resultat
    return multiplicarElements(array[1:],resultat * array[0])

#print(multiplicarElements([12,2,3,54,3,2], 1))

#7
def sumaParells(n, resultat):
    if n == 2:
        return resultat

    if n % 2 == 0:
        return sumaParells(n-1, resultat +n)
    
    return sumaParells(n-1, resultat)

#print(sumaParells(12, 0))

#8
def imprimirNumero(n,resultat):
    if resultat == n:
        return n
    print(resultat)
    return imprimirNumero(n, resultat +1)

#print(imprimirNumero(8, 1))        

#9
def mismoValor(vector1, vector2):
    if len(vector1) == 0:
        return True
    elif vector1[0] != vector2[0]:
        return False

    return mismoValor(vector1[1:], vector2[1:])
#print(mismoValor([1,2,3,4],[1,2,3,4]))

#10
def posicioValor(vector, resultat):
    if vector == []:
        return("CAP VALOR COINCIDEIX")
    elif resultat == vector[0]:
        return vector[0]
    return posicioValor(vector[1:], resultat +1)

#print(posicioValor([16,15,14,13,11,10,11,9,8,7],0))

#11
def repetirFrase(frase, vegades):
    if vegades == 1:
        return frase
    print(frase)
    return repetirFrase(frase, vegades -1)

#print(repetirFrase("LA CONCHA DE TU MADRE", 3))

#13
def numeroInRango(rango, numero):
    if len(rango) == 0:
        return False
    elif numero == rango[0]:
        return True
    return numeroInRango(rango[1:],numero)
#print(numeroInRango([54,55,56,57,58,59,60,61,62],60))

def numInRang(num1, num2, numero):
    if numero < num1 or numero > num2:
        return False
    elif numero == num2:
        return True
    return numInRang(num1, num2 -1, numero)
#print(numInRang(15,30,25))

import random
#14
def valorsAleatoris(llistaValors,veces):
    if veces == 0:
        return llistaValors
    llistaValors.append(random.randint(0,100000))
    return valorsAleatoris(llistaValors,veces -1)
#print(valorsAleatoris([],9))       

#15
def valoresDiferentes(listaValores, veces):
    if veces == 0:
        return listaValores
    numero = random.randint(0,10000)
    if numero in listaValores:
        numero = 0
    else:
        listaValores.append(numero)
    return valoresDiferentes(listaValores, veces -1)

#print(valoresDiferentes([],10)) 