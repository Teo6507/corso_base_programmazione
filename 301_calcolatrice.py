#Crea una semplice calcolatrice.
#Chiedi all'utente che operazione vuole eseguire e i due numeri.
#Le operazioni sono la somma, la differenza, la moltiplicazione e la divisione.
#Una volta eseguito il calcolo chiedi se vuole proseguire (Y/N) e so vuole eseguire un altro calcolo.
#Usa le funzioni. Presta attenzione che l'utente non divida per 0.
def somma(x,y):
    return x+y
def differenza(x,y):
    return x-y
def moltiplicazione(x,y):
    return x*y
def divisione(x,y):
    if y!=0:
        divisione=x/y
    else:
        divisione="Impossibile"
    return divisione
while True:
    n_1:int=int(input("Inserisci il primo numero: "))
    segno:str=input("Inserisci il segno (+,-,*,/): ")
    n_2:int=int(input("inserisci il secondo numero: "))
    if segno=="+":
        print(somma(n_1,n_2))
    if segno=="-":
        print(differenza(n_1,n_2))
    if segno=="*":
        print(moltiplicazione(n_1,n_2))
    if segno=="/":
        print(divisione(n_1,n_2))
    while True:
        check:str=input("Vuoi continuare? (y/n): ")
        if check == "y" or check == "n":
            break
    if check == "n":
        break