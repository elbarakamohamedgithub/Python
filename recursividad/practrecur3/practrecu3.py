"1: base = 4, alçada = 3"
"****"
"****"
"****"
def rectangle(b,a):
    if a == 0:
        return ""
    else:
        if b == 0:
            print(end="\n")
            return rectangle(4, a-1)
        else:
            print("* ", end="")
            rectangle(b-1, a)

"2: abcdef = True"
letrasdicc = [ "a", "b", "c", "d", "e", "f", "g", "h", "i",
              "j", "k", "l", "m" ,"n", "ñ", "o", "p", "q",
              "r", "s", "t", "u", "v", "w", "x", "y", "z"]
paraula ="srtuv"
def orden_alfabetic(paraula):
    if len(paraula) == 1:
        return True
    else:
        if paraula[0] < paraula[0+1]:
            return orden_alfabetic(paraula[1:])
        else:
            return False
        
"3: ANATOLE  LUCAS:  2, 1, 3, 4, 7, 11, 18, '29', 47, 76, 123, 199, 322"
p = 12
def lu(p):
    if p == 0:
        resultado = 2
        return resultado
    if p == 1:
        resultado = 1
        return resultado    
    else:
       resultado1 = lu(p-1)
       resultado2 = lu(p-2)
       resultado = resultado1 + resultado2
       return resultado

"4: Qadrats perfectes  no parells"
def imprimirQuadrats(n, m):
    if n == 0:
        print("")
    else:
        if (m % 2) != 0:
            print(m*m, end=" ")
            return imprimirQuadrats(n-1, m+1)
        else:
            return imprimirQuadrats(n, m+1)
        
imprimirQuadrats(4,10)