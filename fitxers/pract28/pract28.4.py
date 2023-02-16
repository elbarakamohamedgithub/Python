import os

a = open("pract28/pract28.txt","r")
lineas = 0
paraulas = 0

for linea in a.readlines():
    lineas += 1
print(lineas)
a.seek(0)
for paraula in a:
    paraulas += 1
print(paraulas)

print( a.tell())

a.close()