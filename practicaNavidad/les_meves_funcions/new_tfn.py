#revisado
def new_tfn():
    numeroTfn = input("Introdueix el numero de telefon: ")
    try:
        if len(numeroTfn) != 9:
            raise ValueError
        elif not numeroTfn.isdigit() :   
            raise TypeError
        else:
            print(numeroTfn)
    except ValueError:
        print("El telefon no te un format adequat(9 números)")
    except TypeError:
        print("EL telfon no te un format adequat(no pot contenir lletres)")
new_tfn()

