ndecimale = int(input("Inserisci il numero decimale da trasformare in binario"))
nbinario = []
ND = ndecimale

while ND != 0:
    cifra = ND % 2 #il resto è sempre 0 o 1
    ND //= 2
    nbinario.append(cifra)

nbinario.reverse()
print("Il numero inserito, ",ndecimale, ",trasformato in binario è ",nbinario)
print("Il numero ", bin(ndecimale))

