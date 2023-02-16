import os
cara = open("pract29/caraa.txt","r")
dura = open("pract29/dura.txt","r")
clients = open("pract29/clients.txt","w")

dicClientes = {}
for linea in cara:
    cliente = {
        "nombre":linea[7:38],
        "direccion": linea[38:68],
        "ciudad": linea[68:]
    }
    dicClientes[linea[:7]] = cliente

for linea in dura:
    cliente = {
        "nombre":linea[7:38],
        "direccion": linea[38:68],
        "ciudad": linea[68:]
    }
    dicClientes[linea[:7]] = cliente


listaNombres = []
for clave, valor in dicClientes.items():
    listaNombres.append(valor["nombre"])

for i in range(len(listaNombres) -1):
    for j in range(len(listaNombres) -1 -i):
        if listaNombres[j] > listaNombres[j+1]:
            listaNombres[j], listaNombres[j+1] = listaNombres[j+1],listaNombres[j]
print(listaNombres)

for item in listaNombres:
    for key, value in dicClientes.items():
        if item == value["nombre"]:
            clients.writelines(key + value["nombre"] + value["direccion"] + value["ciudad"])