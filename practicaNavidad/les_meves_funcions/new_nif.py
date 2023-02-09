dict_clientes = {"34343434H": {"nombre": "Jason Statham", "telefono": "666994455"},
 "78787878K": {"nombre": "Dwayne Johnson", "telefono": "666765432"},
 "39292939S": {"nombre": "Federico Luppi", "telefono": "666232211"},
 "53423454C": {"nombre": "Lorenzo Lamas", "telefono": "666987578"},
 "87654334T": {"nombre": "Charlize Theron", "telefono": "555443322"},
 "92837467Z": {"nombre": "Linda Hamilton", "telefono": "555443322"},
 "26548734H": {"nombre": "Scarlett Johansson", "telefono": "555443322"},
 "99837653N": {"nombre": "Uma Thurman", "telefono": "555443322"}
 }
letrasDni = ["T","R","W","A","G","M","Y","F","P","D","X","B","N",
             "J","Z","S","Q","V","H","L","L","C","K","E"]

#revisado
def new_nif(new ="yes"):
    nif = input("Introdueix el nif: ")
    try:
        if len(nif) == 9:
            try:
                if letrasDni[int(nif[0:8])%23] == nif[8].upper():
                    try:
                        if nif.upper() not in dict_clientes.keys() and new == "yes":
                            print(nif.upper())
                        elif new != "yes":
                            try:
                                if nif.upper() in dict_clientes.keys():
                                    print(nif.upper())
                                else:
                                    raise NameError
                            except NameError:
                                print("El dni no existeix")
                        else:
                            raise NameError
                    except NameError:
                        print("El dni ja existeix")
                else:
                    raise TypeError
            except TypeError:
                print("La lletra del nif no es correcte")
        else:
            raise ValueError
    except ValueError:
        print("El nif ha de contenir 9 caràcters")             

new_nif("no")
