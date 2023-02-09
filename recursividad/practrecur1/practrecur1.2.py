#1Programar un algoritme recursiu que permeti fer la divisió per restes successives
def restaSuccesiva(numero, resta):
    resultat = 0
    if numero >= resta:
        resultat = + 1 + restaSuccesiva((numero-resta),resta)
    return resultat
print(restaSuccesiva(13,2))

#Programar un algoritme recursiu que permeti sumar els dígits d’un número
def sumarDigits(numero):
    resultat = 0
    if numero != "":
        numero = str(numero)
        resultat = + int(numero[0]) + sumarDigits(numero[1:])
    return resultat
print(sumarDigits(432))

#Programar un algoritme recursiu que permeti sumar els elements d’una llista
def sumarElments(llista):
    suma = 0
    if len(llista) != 0:
        suma = + llista[0] + sumarElments(llista[1:])
    return suma
print(sumarElments([12,32,3]))

#Escriure la funció Potencia(x, y) = x^y de manera recursiva.
def potencia(x, y):
    resultado = 1
    if y != 0:
        resultado = x * potencia(x, y-1)
    return resultado
print(potencia(5,3))

#Escriure el producte de dos números de manera recursiva.
def producte(x, y):
    resultat = 0
    if y != 0:
        resultat =  x + producte(x, y-1)
    return resultat
print(producte(5,3))

#Programar una funció recursiva que permeti multiplicar els elements d’un Array
def elementsArray(array):
    resultado = 1
    if len(array) != 0:
        resultado = array[0] * elementsArray(array[1:])
    return resultado
print(elementsArray([3,30,20]))

#Escriure un programa que trobi la suma dels enters positius parells des de N fins a 2
def sumaParells(n):
    resultat = 0
    if n >= 2:
        if n % 2 ==0:
            resultat = n + sumaParells(n-1)
        else:
            resultat = sumaParells(n-1)
    return resultat
print(sumaParells(11))

#Escriure f.recursiva que imprimeixi els valors des de 1 fins a un número introduït per l’usuari.
def printarNumeros(numero):
    n = 1
    if n != numero:
        print(numero)
        numero = printarNumeros(numero -1)
    return n
#numero = int(input("introduce un numero : "))
print(printarNumeros(5))

# donats dos vectors de número sencers, retorni un booleà indicant si són iguals.
def vectorsIguals(vector1, vector2):
    if len(vector1) != 0:
        if vector1[0] == vector2[0]:
            return vectorsIguals(vector1[1:], vector2[1:])
        else:
            return False
    return True
print(vectorsIguals([23,45,3,2],[23,45,3,2]))

# comprovi si el valor d’algun dels elements del vector coincideix amb el seu índex.
def comprovacioVector(vector):
    posicio = 0
    if len(vector) != 0:
        if vector[0] == posicio:
            return True
        posicio = + 1 + comprovacioVector(vector[1:])
    return False
print(comprovacioVector([6,5,4,3,2,1]))

#Programa recursiu que demani a l’usuari una frase i la repeteixi un número de vegades.
def repetirFrase(frase, veces):
    if veces != 0:
        print(frase)
        return repetirFrase(frase, veces -1)
#frase = input("introdueix una frase: ")
#veces = int(input("quantes vegades la vols repeitr: "))
#repetirFrase(frase, veces)

#Escriure un programa recursiu que insereixi valors aleatoris en una llista
import random
def numerosAleatoris(llistaValors):
    if len(llistaValors) < 5:
        llistaValors.append(random.randint(0,10000))
        return numerosAleatoris(llistaValors)
    return llistaValors
print(numerosAleatoris([]))

#Escriure un programa recursiu que insereixi valors aleatoris sense repetició en una llista.
def numerosAleatorisRepetits(llistaValors):
    numero = 0
    if len(llistaValors) < 5:
        numero = random.randint(0,100000)
        if numero not in llistaValors:
            llistaValors.append(numero)
            return numerosAleatorisRepetits(llistaValors)
        return numerosAleatorisRepetits(llistaValors)
    return llistaValors
print(numerosAleatorisRepetits([]))



