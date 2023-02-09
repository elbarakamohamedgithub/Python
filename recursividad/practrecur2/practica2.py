#1
def wallis(n):
  if n == 0:
    return 1
  else:
    return ((2 * n) / (2 * n - 1)) * ((2 * n) / (2 * n + 1)) * wallis(n - 1)

#2
def invertirNumero(numero):
    resultado = ""
    if numero != "":
        resultado = numero[-1] + invertirNumero(numero[:-1])
    return resultado

#3
def metodeRus(a, b):
    resultat = 0
    if a >= 1:
        if a % 2 != 0:
            resultat += b + metodeRus(a//2, b *2)
        else:
            resultat += metodeRus(a//2,b *2)
    return resultat

#4
def printarNumeros(n):
    resultat = ""
    if n <= 7:
        resultat += str(n) + printarNumeros(n+1)
    resultat += str(n)
    return resultat


#5
import random
def endevinarNumero(numero):
    intentos = 1
    print("El programa ha generat un numero  entre 0 i 1000")
    numeroTriat = int(input("Quin creus que es ? "))
    print(numero)

    if numero == numeroTriat:
        print("CORRECET:Has endevinat el numero en el {} intent".format(intentos))
    else:
        if numeroTriat < numero:
            print("El numero es troba entre {} i 1000".format(numeroTriat))
            intentos += 1 + endevinarNumero(numero)
        else:
            print("El numero es troba entre 0 i {}".format(numeroTriat))
            intentos += 1 + endevinarNumero(numero)

    return intentos
numero = random.randint(1,1000)

#6
frase = "quiero ser millonario antes de los 20"
def separarFrase(frase):
    resltado = ""
    if len(frase) > 0:
        if frase[0] != " ":
            resltado = resltado + frase[0]
            print(resltado, end="")
            separarFrase(frase[1:])
        
        else:
            print("")
            separarFrase(frase[1:])
#7
def eliminarVocals(frase):
    vocals = "aeiou"
    resultado = ""
    if len(frase) != 0:
        if frase[0] not in vocals:
            resultado += frase[0] + eliminarVocals(frase[1:])
        else:
            resultado += eliminarVocals(frase[1:])
    return resultado
frase = "i need to become millionare i swear to gods"

#8
def imprimirparaula(paraula):
    resultat = ""
    if len(paraula) != 0:
        resultat += paraula[-1] + imprimirparaula(paraula[:-1])
        print(paraula)
    return paraula
paraula = "*****"


#9  
llistaLlistes = [[32,534,232,4,3,3,2],[23,45,2],[103,4,4,3,12],[4,3]]
def ordenarLlista(llistaLlistes, i, j):
    if i >= len(llistaLlistes):  
        return llistaLlistes
    else:
        if j >= len(llistaLlistes[i]):
            return ordenarLlista(llistaLlistes, i, j+1)
        else:
            if llistaLlistes[i][j] > llistaLlistes[i][j+1]:
                llistaLlistes[i][j],llistaLlistes[i][j+1] = llistaLlistes[i][j+1],llistaLlistes[i][j]
                return ordenarLlista(llistaLlistes,i, j+1)
            else:
                return ordenarLlista(llistaLlistes,i, j+1)
print(ordenarLlista(llistaLlistes,0,0))