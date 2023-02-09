def sum(llisa):
    numero = 0
    for i in llisa:
        numero += int(i)
    return numero
#Sprint(sum([1,5,4]))


def multipl(llista):
    result = 1
    for i in llista:
        result *= i
    return result

print(multipl([3,20,3]))