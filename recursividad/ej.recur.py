#sumaritems
def suma(llista1,i,total):
    if i == len(llista1):
        return total

    total += llista1[i]
    return  suma(llista1,i+1,total)
print(suma([1,2,3,4],0,0))

#ordenar llista
def itemsequal(llista1,i,j):
    if i == len(llista1) -1:
        return llista1
    if j == len(llista1):
        return itemsequal(llista1,i+1,i +2)
    if llista1[i] > llista1[j]:    
        llista1[j], llista1[i]  = llista1[i] , llista1[j]
    
    return itemsequal(llista1,i, j+1)

print(itemsequal([4,2,5,1],0,1))

#en una frase, retorna les vocals en majuscula, les consonants en miniscula
def miniMayu(frase, resultado):
    resultado = ""
    vocals = "aeiou"
    if len(resultado) == len(frase):
        return resultado
    else:
        if frase[0] in vocals:
            resultado += frase[0].upper()
            return miniMayu(frase[1:], resultado)
        else:
            resultado += frase[0].lower()
            return miniMayu(frase[1:], resultado)
frase = "jola sapos cabrones"
print(miniMayu(frase, resultado=""))

#afegir items en una llista
def incluirNumeros(a, b, llistaNumeros):
    if a > b:
        return llistaNumeros 
    llistaNumeros.append(a * a)
    return incluirNumeros(a+1, b, llistaNumeros)
print(incluirNumeros(3,7,[]))


