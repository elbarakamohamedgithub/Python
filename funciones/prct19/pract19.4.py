def superposicio(llista1, llista2):
    variable = False
    for i in llista1:
        for j in llista2:
            if int(i) == int(j):
                variable = True
            else:
                variable = False
    return variable
print(superposicio([1,2,3],[5,6]))