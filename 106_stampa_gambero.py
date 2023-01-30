#Inserisci una parola/frase. Stampa il risultato partendo da destra. Es. Giorgio diventa "oigroiG"
string=input("Inserisci una stringa: ")
i=len(string)-1
output=""
while i>=0:
    output=output+string[i]
    i=i-1
print(output)