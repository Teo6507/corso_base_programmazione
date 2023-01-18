nome=input("Inserisci una stringa: ")
l=len(nome)
i=0
output=0
while i<l:
    if nome[i]=="a" or nome[i]=="e" or nome[i]=="i" or nome[i]=="o" or nome[i]=="u" or nome[i]=="A" or nome[i]=="E" or nome[i]=="I" or nome[i]=="O" or nome[i]=="U":
        output=output+1
    i=i+1
print(output)