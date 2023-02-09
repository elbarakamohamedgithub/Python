def neteja_pantalla(veces):
    return veces * "\n"

print(neteja_pantalla(25))

def tres_linies(n):
    return "\n" * n

print(tres_linies(3))

def nou_linies(z):
    return 3 * tres_linies(3)

print(nou_linies(3))

def concatena_n_vegades(c,n):
    return c * n

print(concatena_n_vegades("FFF\n" , 10))