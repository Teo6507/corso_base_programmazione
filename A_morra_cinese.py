computer=1
utente=""
perso=0
vinto=0
pareggio=0

while True:
    if computer==4:
        computer=1
    
    utente=int(input("inserisci 1 per CARTA, 2 per SASSO o 3 per FORBICI: "))
    
    if computer==1:
        print("CARTA")
    if computer==2:
        print("SASSO")
    if computer==3:
        print("FORBICI")
    
    if computer==utente:
        pareggio=pareggio+1
        print("Hai pareggiato!")
    else:
        if utente==1:
            if computer==2:
                vinto=vinto+1
                print("Hai vinto!")
            if computer==3:
                perso=perso+1
                print("Hai perso!")
        if utente==2:
            if computer==3:
                vinto=vinto+1
                print("Hai vinto!")
            if computer==1:
                perso=perso+1
                print("Hai perso!")
        if utente==3:
            if computer==1:
                vinto=vinto+1
                print("Hai vinto!")
            if computer==2:
                perso=perso+1
                print("Hai perso!")
    print("VITTORIE: "+str(vinto))
    print("SCONFITTE: "+str(perso))
    print("PAREGGI: "+str(pareggio))

    if vinto==2:
        break
    if perso==2:
        break
    computer=computer+1
print("FINE")