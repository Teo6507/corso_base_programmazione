guadagno=int(input("Inserisci quanto hai guadagnato: "))
irpef=0

if guadagno<=30000:
    if guadagno<10000:
        iperf=0
    if guadagno>=10000:
        iperf=22/100*guadagno
else:
    iperf=4400+33/100*(guadagno-30000)
print(iperf)

exit=input("press any key to exit")    