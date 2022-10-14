A=int(input("inserisci il primo numero: "))
B=int(input("inserisci il secondo numero: "))
C=int(input("inserisci il terzo numero: "))
#Maggiore=0

if (A>B):
   if(C > A):
       Maggiore=C
   else:
       Maggiore=A
else:
   if(C > B):
       Maggiore=C
   else:
       MAggiore=B


if(A+B+C > 10):
   print(Maggiore)
else:
    print(A+B+C)