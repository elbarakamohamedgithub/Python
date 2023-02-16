import os
a = open("pract28/pract28.txt","r")
b = open("pract28/pract281.txt","w")

letras = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
          "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s",
          "t", "u", "v", "w", "x", "y", "z")

for parula in a.readlines():
    for letra in parula:
        letra = (letra + "13")
        b.write(letra)       

