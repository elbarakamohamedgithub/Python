import os
tablets = open("pract30/tablets.txt","r")
barats = open("pract30/barats.txt", "w")
tabarats = {}

def tabletsBarats(tablets,barats,p):
    for linea in tablets.readlines():
        producta = linea.split("; ")
        nombre = producta[0]
        modelo = producta[1]
        
        valocidad = int(producta[3])
        if valocidad < 500:
            salida = nombre[:3] + "-" + modelo +  " Baixa"
        elif valocidad >= 500 or valocidad <= 900:
            salida = nombre[:3] + "-" + modelo + " Mitjana"
        else:
            salida = nombre[:3] + "-" + modelo + " Alta"
        
        if float(producta[4][:-2]) < p:
            barats.write(salida+"\n")
    
tabletsBarats(tablets, barats, 500)



tablets.close()
barats.close()