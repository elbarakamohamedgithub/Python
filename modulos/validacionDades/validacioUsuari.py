def validacioNom():
    nom = input("INTRODUEIX EL TEU NOM D'USUARI: ")
    try:
        if len(nom) > 6 and len(nom)  < 12:
            try: 
                if nom.isalnum():
                    return True
            
                raise ValueError
            except ValueError:
                return("EL NOM HA DE SER ALFANUMERIC")
        raise NameError

    except NameError:
        return("EL NOM HA DE TENIR ENTR 6 Y 12 CARACTERS")

def validacioContra():
    contra = input("INTRODUEIX LA CONTRASSENYA: ")
    try:
        if len(contra) > 8 and not " "in contra:
            try:
                if contra.lower() != contra and contra.isalnum() :
                    return True
                raise ValueError
            except ValueError:
                return("LA CONTRASSENYA TRIADA NO ES SEGURA")
        raise NameError
    except NameError:
        return("LA CONTRASSENYA TRIADA NO ES SEGURA")
print(validacioContra())