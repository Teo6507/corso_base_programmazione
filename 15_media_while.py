tot=0
i=0
while True:
    numero=int(input("Inserisci il numero: "))
    if (numero==0):
        break
    else:
        tot=tot+numero
    i=i+1
print(tot/i)


A=input("press any key to exit")