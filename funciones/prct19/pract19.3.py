def numeroDivisor(valor):
    for i in range(1, valor):
        if valor%i == 0:
            print(i)
                
numeroDivisor(20)