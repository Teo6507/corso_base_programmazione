#Chiedi all'utente 2 stringhe. Controlla che tutti i caratteri presenti nella prima stringa siano presenti nella seconda striga. 
#Non importa la posizione.
#Stampa il risultato se vero o falso.
i=0
string_1=input("Inserisci la prima stringa: ")
string_2=input("Inserisci la seconda stringa: ")
output="Vero"
while i<len(string_1):
    if not string_1[i] in string_2:
        output="Falso"
        break
    i=i+1
print(output)