import os

archivo = open("pract28/pract28.txt","r")
#print(archivo.read())
delimitador = "-"
lista = ["lias","dsd","Dsdsfsd","233"]
for i in lista:
    print(delimitador + i, end="")


archivo.close()