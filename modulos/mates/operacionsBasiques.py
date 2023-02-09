def suma(a,b):
    return a+b

def resta(a,b):
    return a - b

def multiplicar(a, b):
    return a *b 

def dividir(a, b):
    try:
        b > 0
        return a / b              
    except ZeroDivisionError:    
        print("DIVIDEND NO VALID")
        return 0
