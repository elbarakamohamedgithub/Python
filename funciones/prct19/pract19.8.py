def funcioTraspas(any):
    any2 = 0
    while True:
        any2 = input("un any posterior al primer " )
        any2 = int(any2)
        if any2 < any:
            print(any2, "no es major que ",any)
        else:
            break
        
    anysbetween = any2 - (any - 1)
    return round(anysbetween/4)

print(funcioTraspas(2000))

