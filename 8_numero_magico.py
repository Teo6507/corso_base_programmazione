# ----- CONSEGNA ------
# Chiedi all'utente di indovinare un numero magico.
# Il numero magico è il numero 7.
# L'utente ha 10 tentativi.
# Se indovina stampa "Complimenti, hai indovinato!"
# Se non indovina stampa "Game over!"
# ---------------------
tentativi=0

while tentativi<10:
    N=int(input("Indovina il numero magico: "))
    if (N==7):
        print("Complimenti, hai indovinato!")
        break
    else:
        print("Game over!")
        tentativi=tentativi+1

    if (tentativi == 10):
        break