def entraParaules():
    paraualas = []
    paraula = ""
    while True:
        paraula = input("INTRODUEIX UNA PARAULA")
        if paraula == "fi":
            break
        else:
            paraualas.append(paraula)
    print(paraualas)
    
    for i in range(len(paraualas)-1):
        for j in range(i+1, len(paraualas)):
            if paraualas[i] == paraualas[j]:
                return paraualas[i]


print(entraParaules())