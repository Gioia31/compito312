città = int(input("Inserisci il numero di città per cui eseguire il calcolo "))
vescu = float(input("Inserisci il valore di escurione termica da utilizzare "))
cittàcont = 0 #città che passano x il while contatore
cittàoltre = 0 #città che passano per if 

while cittàcont != città :
    nomecittà = input ("Inserisci il nome della città da considerare ")
    tmax = float(input("Inserisci la temperatura massima registrata in questa città "))
    tmin = float(input("Inserisci la temperatura minima registrata in questa città "))
    escu = tmax - tmin
    cittàcont = cittàcont + 1

    if escu > vescu :
        listacittàoltre = []
        listacittàoltre.append(nomecittà)
        cittàoltre = cittàoltre + 1

print("Le città che superano il valore di escursione termica fornito sono ", cittàoltre, " : ", listacittàoltre)
        