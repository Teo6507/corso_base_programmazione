A=0
B=0
P=str("!")
while A<=10:
    A=A+1
    B=str(A)
    if (A %2 == 0):
        print(B+P)
    else:
        print(A)
    
    if (A == 10):
        break
