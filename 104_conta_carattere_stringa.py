#Chiedere all'utente una stringa ed un carattere.
#Contare quante volte quel carattere è presente nella stringa.
i=0
string=input("Inserisci una stringa: ")
letter=input("Inserisci una lettera: ")
lenght=len(string)
count=0
while i<lenght:
    if string[i]==letter:
        count=count+1
    i=i+1
print(count)