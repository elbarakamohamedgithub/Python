def dades():
    llistaNumeros = []
    while True:
        numero = input("INTRODUCE UN NUMERO: ")
        if int(numero) < 0:
            break
        llistaNumeros.append(int(numero))
    return llistaNumeros

def suma(llistaNumeros):
    sumaNumeros = 0
    for i in llistaNumeros:
        
        sumaNumeros += int(i)
    return sumaNumeros


def maxim(llistaNumeros):
    for i in range(len(llistaNumeros)-1):
        for j in range(len(llistaNumeros)-1-i):
            if llistaNumeros[j] > llistaNumeros[j+1]:
                llistaNumeros[j],llistaNumeros[j+1] = llistaNumeros[j+1],llistaNumeros[j]
    return llistaNumeros[0]


def minim(llistaNumeros):
    for i in range(len(llistaNumeros)-1):
        for j in range(len(llistaNumeros)-1-i):
            if llistaNumeros[j] < llistaNumeros[j+1]:
                llistaNumeros[j],llistaNumeros[j+1] = llistaNumeros[j+1],llistaNumeros[j]
    return llistaNumeros[0]


def recorregut(llistaNumeros):
    for i in range(len(llistaNumeros)-1):
        for j in range(len(llistaNumeros)-1-i):
            if llistaNumeros[j] < llistaNumeros[j+1]:
                llistaNumeros[j],llistaNumeros[j+1] = llistaNumeros[j+1],llistaNumeros[j]
    return llistaNumeros[0] - llistaNumeros[-1]

def mitjana(llistaNumeros):
    sumaNumeros = 0
    for i in llistaNumeros:
        sumaNumeros += i

    return sumaNumeros/len(llistaNumeros)


def variancia(llistaNumeros):
    total = 0
    medias = mitjana(llistaNumeros)
    for i in llistaNumeros:
        total += (i - medias)**2
    return total / (len(llistaNumeros) -1)

def checkLength(llistaNumeros):
    if len(llistaNumeros) == 0:
        return True
    
    return False

llista = []

menutxt = "Llegir dades\nCalcular el recorregut\nCalcular la mitjana\nCalcular la variància\nSalir"
menu = True


menullegir = False
menumitjana = False
menurecorregut = False
menuvariancia = False

while menu:
    print(menutxt)
    opc = ""
    while True:
        opc = input("Introduce una opcion: ")
        if opc.isnumeric() and int(opc) in range(0,6):
            opc = int(opc)
            break
        else:
            print("INTRODUCE UNA OPCION VALIDA")
            
    if opc == 1:
        menullegir = True
        menu = False

    elif opc == 2 and checkLength(llista) == False:
        menurecorregut = True
        menu = False

    elif opc == 3 and checkLength(llista) == False:
        menumitjana = True
        menu = False
        
    elif opc == 4 and checkLength(llista) == False:
        menuvariancia = True
        menu = False

    elif opc == 5:
        menu = False
 
    
    while menullegir:
        llista = dades()
        print(llista)
        menu = True
        menullegir = False

    while menurecorregut:
        print(recorregut(llista))
        menu = True
        menurecorregut = False

    while menumitjana:
        print(mitjana(llista))
        menu = True
        menumitjana = False

    while menuvariancia:
        print(variancia(llista))
        menu = True
        menuvariancia = False