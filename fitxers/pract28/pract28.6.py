import os
a = open("pract28/clauValor.txt")

def carregar_dades(archiu):
    diccionariCamps = {}
    for frase in a.readlines():
        for palabra in frase:
            if palabra != ":":
                print(palabra, end="")
            else:
                print(palabra, end="")

carregar_dades(a)