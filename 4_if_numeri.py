numeroa=int(input("inserisci il primo numero: "))
numerob=int(input("inserisci il secondo numero: "))
i=0
if numeroa > 10:
    print("FUORI SCALA")
    i=i+1
if numerob > 50:
    print("TROPPO GRANDE")
    i=i+1
if i==0:
    print("TUTTO OK")

exit=input("press any key to exit")