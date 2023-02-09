def desglossament_billets(quantitat):
    billet500 = 0
    billet200 = 0
    billet100 = 0
    billet50 = 0
    billet50 = 0
    billet20 = 0
    billet10 = 0
    billet5 = 0
    moneda2 = 0
    moneda1 = 0
    moneda50 = 0
    while quantitat > 0:
        if  quantitat >= 500:
            quantitat -= 500
            billet500 += 1
        elif quantitat >= 200:
            quantitat -= 200
            billet200 +=1
        elif quantitat >= 100:
            quantitat -= 100
            billet100 += 1
        elif quantitat >= 50:
            quantitat -= 50
            billet50 += 1
        elif  quantitat >=5:
            quantitat -= 5
            billet5 +=1
        elif quantitat >= 2:
            quantitat -=2
            moneda2 += 1 
        elif quantitat >= 1:
            quantitat -= 1
            moneda1 += 1
        elif quantitat >= 0.50:
            quantitat -= 0.50
            moneda50 +=1
        else:
            print("FUCK YOU PUUUUSSYYY HAHAHHHA")    
    print(billet500,billet200,billet100,billet50,billet20,billet10,billet5,moneda2,moneda1,moneda50)  
    return quantitat
        
            
        
print(desglossament_billets(7751.70))