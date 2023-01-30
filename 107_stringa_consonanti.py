#Chiedi una stringa all'utente. Stampa la stringa inserita senza le vocali.
i=0
string=input("Inserisci una stringa: ")
output=""
lenght=len(string)
while i<lenght:
    if string[i]!="a" and string[i]!="e" and string[i]!="i" and string[i]!="o" and string[i]!="u" and string[i]!="A" and string[i]!="E" and string[i]!="I" and string[i]!="O" and string[i]!="U":
        output=output+string[i]
    i=i+1
print(output)