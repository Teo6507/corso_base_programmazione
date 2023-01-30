i=0
string=input("Inserisci una stringa: ")
A=0
E=0
I=0
O=0
U=0
lenght=len(string)
while i<lenght:
    if string[i]=="A" or string[i]=="a":
        A=A+1
    if string[i]=="E" or string[i]=="e":
        E=E+1
    if string[i]=="I" or string[i]=="i":
        I=I+1
    if string[i]=="O" or string[i]=="o":
        O=O+1
    if string[i]=="U" or string[i]=="u":
        U=U+1
    i=i+1
print("A: " + str(A)+ ", E:" + str(E)+ ", I:" + str(I)+ ", O:" + str(O)+ ", U:" + str(U))