lun = int(input("Da quante cifre è composto il numero binario? "))
espo = 0
ncifre = 0 #numero cifre passate dal while
nbinario = ""
ndecimale = 0

while ncifre != lun :
    ncifre = ncifre + 1
    cifra = input("Inserisci il valore della cifra a destra ")
    c = int(cifra)
    nbinario = nbinario + cifra
    ndecimale = ndecimale + (c*(2**espo))
    espo = espo + 1

print("Il numero binario fornito, con il sistema decimale, corrisponde a ",ndecimale )
print("Secondo le funzioni di Python il numero binario è uguale a", int(nbinario[::-1], base = 2))
