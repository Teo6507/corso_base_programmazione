operazioni=int(input("inserisci il numero di operazioni: "))
output=int(input("inserisci il primo numero"))
i=1

while i<operazioni:
    segno=int(input('inserisci 1 per la somma, 2 per la sottrazione, 3 per la divisione o 4 per la moltiplicazione: '))
    numero_a=int(input("Inserisci un numero: "))
    if(segno==1):
        output=output+numero_a
    else:
        if(segno==2):
            output=output-numero_a
        else:
            if(segno==3):
                if(numero_a==0):
                    output="Non puoi dividere per zero!"
                else:
                    output=output/numero_a
            else:
                if(segno==4):
                    output=output*numero_a
                else:
                    output=output+numero_a
    i=i+1
print(output)

exit=input("press any key to exit")