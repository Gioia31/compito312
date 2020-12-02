npart = int(input("Inserisci il totale dei partecipanti "))

while npart != 0:
    npart = npart-1
    nome = input("Inserisci il nome del partecipante ")
    listapart = []
    listapart.append(nome)

    vallancio = float(input("Inserisci il valore del lancio "))

vallanci = []
vallanci.append(vallancio)
massimo = max(vallanci)
print("Il valore massimo ottenuto nella gara è ", massimo, " complimenti !!")