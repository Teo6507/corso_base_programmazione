controllo=0
while controllo<=0:
    nome=input("Inserisci solo cifre: ")
    lenght=len(nome)
    i=0
    output=0
    while i<lenght:
        if nome[i]=="1" or nome[i]=="2" or nome[i]=="3" or nome[i]=="4" or nome[i]=="5" or nome[i]=="6" or nome[i]=="7" or nome[i]=="8" or nome[i]=="9" or nome[i]=="0":
            output=output+int(nome[i])
            i=i+1
            controllo=1
        else:
            controllo=0
            break
print(output)