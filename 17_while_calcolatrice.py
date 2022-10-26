numero_a=int(input('inserisci un numero: '))
numero_b=int(input('inserisci un numero: '))
segno=int(input('inserisci 1 per la somma, 2 per la sottrazione, 3 per la divisione o 4 per la moltiplicazione: '))
output=0
if(segno==1):
    output=numero_a+numero_b
else:
    if(segno==2):
        output=numero_a-numero_b
    else:
        if(segno==3):
            output=numero_a/numero_b
            if(numero_b==0):
                output="Non puoi dividere per zero!"
        else:
            if(segno==4):
                output=numero_a*numero_b
            else:
                output=numero_a+numero_b
print(output)