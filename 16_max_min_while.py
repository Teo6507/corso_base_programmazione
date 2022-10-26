somma=0
max=float('-inf')
min=float('inf')
while True:
    numero=int(input("inserisci il numero: "))
    if (numero==0):
        break
    else:
        if (numero>max):
            max=numero
        if (numero<min):
            min=numero
print("Numero Massimo: "+ str(max))
print("Numero Minimo: "+ str(min))

exit=input("press any key to exit")