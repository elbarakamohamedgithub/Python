dict_articulos = { 4: {"nombre": "ASUS TUF GeForce RTX", "stock": 6, "precio": 1400},
 2: {"nombre": "ASUS DUAL Radeon RX6600", "stock": 12, "precio": 294},
 3: {"nombre": "Intel Core i7-13700K", "stock": 9, "precio": 530},
 1: {"nombre": "Kingston Fury Beast 32GB", "stock": 10, "precio": 180},
 10: {"nombre": "Corsair DC Cable Pro Kit", "stock": 20, "precio": 110},
 11: {"nombre": "Gigabyte GC-TITAN RIDGE 2.0", "stock": 15, "precio": 81},
 }
#revisado
def new_item_id():
    id = input("Introduce tu id: ")
    try:
        if not id.isdigit():
            raise AssertionError
        else:
            try:
                if int(id) < 0:
                    raise AssertionError
                else:
                    try:
                        if int(id) in dict_articulos.keys():
                            raise AssertionError
                        else:
                            print(id)
                    except AssertionError:
                        print("El ID ja existeix" )   
            except AssertionError:
                print("El id ha de ser positiu")
    except AssertionError:
        print("El id ha de ser numèric")
    
    
new_item_id()

    