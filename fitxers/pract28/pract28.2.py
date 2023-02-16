import os

archiu = open("pract28/pract28.txt", "r")
archiu1 = open("pract28/pract281.txt","w")
a = 0   
for i in archiu:
    dada = i
    archiu1.write(i)



archiu1.close()
archiu.close()