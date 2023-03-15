import random

griglia: list=["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸"]

def print_griglia(): 
    print(griglia[0] + "|" + griglia[1] + "|" + griglia[2])
    print("-----")
    print(griglia[3] + "|" + griglia[4] + "|" + griglia[5])
    print("-----")
    print(griglia[6] + "|" + griglia[7] + "|" + griglia[8])

def win():
    if griglia[0]==griglia[1]==griglia[2]:
        return True
    if griglia[3]==griglia[4]==griglia[5]:
        return True
    if griglia[6]==griglia[7]==griglia[8]:
        return True
    if griglia[0]==griglia[3]==griglia[6]:
        return True
    if griglia[1]==griglia[4]==griglia[7]:
        return True
    if griglia[2]==griglia[5]==griglia[8]:
        return True
    if griglia[0]==griglia[4]==griglia[8]:
        return True
    if griglia[2]==griglia[4]==griglia[6]:
        return True
def computer_move():
    mossa=0
    while mossa<=8:
        if griglia[mossa]=="X" or griglia[mossa]=="O":
            mossa=mossa+1
            continue
        if mossa==0 or mossa==3 or mossa==6:
            if griglia[mossa+1]==griglia[mossa] and griglia[mossa+2]==griglia[mossa]:
                break
        if mossa==1 or mossa==4 or mossa==7:
            if griglia[mossa+1]==griglia[mossa] and griglia[mossa-1]==griglia[mossa]:
                break
        if mossa==2 or mossa==5 or mossa==8:
            if griglia[mossa-1]==griglia[mossa] and griglia[mossa-2]==griglia[mossa]:
                break
        if mossa==8: 
            while True:
                mossa=random.randrange(0,9)
                if griglia[mossa]=="X" or griglia[mossa]=="O":
                    continue
                else:
                    break
            break
        mossa=mossa+1
    return mossa
        
            

O:str=""
X:str=""
i=0

while (X!="utente" and X!="computer"):
    scelta:str=input("Vuoi X o O?: ")
    if scelta=="X" or scelta=="x":
        X: str="utente"
        O: str="computer"
    else:
        if scelta=="O" or scelta=="o" or scelta=="0":
            O: str="utente"
            X: str="computer"

print_griglia()

turno=random.randrange(1,3)
if turno==1:
    print("Inizi tu!")
else:
    print("Inizio io!")

while i<=9:
    if turno==1:
        posizione=int(input("Inserisci la posizione: "))
        while griglia[posizione]=="X" or griglia[posizione]=="O" or posizione<0 or posizione>8:
            print ("IMPOSSIBILE")
            posizione=input("Inserisci la posizione: ")
        griglia.pop(posizione)
        if X=="utente":
            griglia.insert(posizione,"X")
        else:
            griglia.insert(posizione,"O")
        i=i+1
        turno=2
    print_griglia()
    print("_________________________________")
    if win():
        break
    
    if turno==2:
        posizione_computer=computer_move()
        griglia.pop(posizione_computer)
        if X=="computer":
            griglia.insert(posizione_computer,"X")
        else:
            griglia.insert(posizione_computer,"O")
        i=i+1
        turno=1
    print_griglia()
    print("_________________________________")
    if win():
        break
