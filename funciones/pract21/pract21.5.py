#a
def personesAprovades(alumnes, notes):
    llistaAprovats = {}
    for nota in notes:
        for alumne in alumnes:
            if nota >= 5 and notes.index(nota) == alumnes.index(alumne):
                llistaAprovats[alumne] = nota
    print("NOM DE LES PERSONES QUE HAN APROVAT:")
    for nombre, nota in llistaAprovats.items():
        print("-",nombre)
    
personesAprovades(["moha","baak","alex","noia","moooha","misssi"],[2,5,4,7,10,2])   
input("")

#b
def numAprovats(notes):
    aprovats = 0
    for nota in notes:
        if nota >= 5:
            aprovats += 1
    print("NUMERO DE PERSONES APROVADES:")
    return   aprovats

print(numAprovats([2,5,4,7,10,2]))
input("")

#c
def maximaNota(alumnes, notes):
    
    llistaAprovats = {}
    for nota in notes:
        for alumne in alumnes:
            if nota == 10 and notes.index(nota) == alumnes.index(alumne):
                llistaAprovats[alumne] = nota
                notes.remove(nota)
                alumnes.remove(alumne)
    print("ALUMNES AMB MAXIMA NOTA")
    for nom, nota in llistaAprovats.items():
        print("-",nom.ljust(23),nota)            

maximaNota(["olga","moha","carles","ilyes","sam"],[10,5,10,4,10])
input("")

#d
def superiorMitjana(alumnes,notes):
    sumaNotes = 0
    notesSuperiors = {}
    for nota in notes:
        sumaNotes += nota
    sumaNotes /= len(notes)
   
    for nota in notes:
        for alumne in alumnes:
            if nota >= sumaNotes and notes.index(nota) == alumnes.index(alumne):
                notesSuperiors[alumne] = nota
                notes.remove(nota)
                alumnes.remove(alumne)
    print("ALUMNES AMB NOTA SUPERIOR A MITJANA")
    for nom, nota in notesSuperiors.items():
        print("~",nom.ljust(23),nota)
superiorMitjana(["olga","moha","carles","ilyes","sam"],[10,5,8,4,10])
input("")


#e
def estudian(alumnes, notes, alumne):
    if alumne in alumnes:
        for nota in notes:
            if notes.index(nota) == alumnes.index(alumne):
                return nota
    else:
        return None
print(estudian(["olga","moha","carles","ilyes","sam"],[10,5,8,4,10],alumne=input("Nom del alumne  buscar: ")))
        

    


