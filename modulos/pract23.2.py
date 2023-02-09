import mates.operacionsBasiques

a,b = 13, 3
print("OPCIO A")
print("suma: ",mates.operacionsBasiques.suma(a,b))
print("resta", mates.operacionsBasiques.resta(a,b))
print("multiplicacio", mates.operacionsBasiques.multiplicar(a,b))
print("divisio: ", mates.operacionsBasiques.dividir(a,b),"\n")

import mates.operacionsBasiques as op

print("OPCIO B")
print("suma: ",op.suma(a,b))
print("resta",op.resta(a,b))
print("multiplicacio", op.multiplicar(a,b))
print("divisio: ", op.dividir(a,b),"\n")

from mates.operacionsBasiques   import *

print("OPCIO C")
print("suma: ",suma(a,b))
print("resta",resta(a,b))
print("multiplicacio", multiplicar(a,b))
print("divisio: ",dividir(a,b))
