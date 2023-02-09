dict_articulos = { 4: {"nombre": "ASUS TUF GeForce RTX", "stock": 6, "precio": 1400},
 2: {"nombre": "ASUS DUAL Radeon RX6600", "stock": 12, "precio": 294},
 3: {"nombre": "Intel Core i7-13700K", "stock": 9, "precio": 530},
 1: {"nombre": "Kingston Fury Beast 32GB", "stock": 10, "precio": 180},
 10: {"nombre": "Corsair DC Cable Pro Kit", "stock": 20, "precio": 110},
 11: {"nombre": "Gigabyte GC-TITAN RIDGE 2.0", "stock": 15, "precio": 81},
 }
#revisado
import copy
def print_tem(id, **values):
    articulos = copy.deepcopy(dict_articulos)
    for key, value in dict_articulos.items():
       
        if key == id:
            for i, valor in value.items():
                for clave, info in values.items():
                    if i == clave:
                        value[clave] = info
    try:
        if id not in dict_articulos.keys():
            raise ValueError
        else:
                
            for i, valor in dict_articulos.items():
                if i == id:
                    print("\n","ID".ljust(30),str(i).rjust(30),"\n","Name".ljust(30),str(valor["nombre"]).rjust(30),
                    "\n","Stock".ljust(30), str(valor["stock"]).rjust(30),"\n", "Price".ljust(30), str(valor["precio"]).rjust(30))
    except ValueError:
        print("No existeix un article amb aquest id")
    try:
        if articulos == dict_articulos:
            raise ValueError
    except ValueError:
        print("La parella clau=valor no existeix")
print_tem(1, stock = "233030000")
