# Programma per calcolare:
# Perimetro del Quadrato
# Perimetro del Rettangolo
# Circonferenza del Cerchio

print ("Buongiorno utente\nQuesto programma permette di calcolare il perimetro di diverse figure geometriche")
figura_scelta = int(input("Scelga una figura geometrica tra:\n1) Quadrato\n2) Rettangolo\n3) Cerchio\n>>>"))
if figura_scelta == 1:
    lato_quadrato = int(input("Inserisci la lunghezza di un lato del quadrato:\n>>>"))
    print ("Il perimetro del quadrato è", lato_quadrato*4)
elif figura_scelta == 2:
    base_rettangolo = int(input("Inserisci la lunghezza della base del rettangolo:\n>>>"))
    altezza_rettangolo = int(input("Inserisci l'altezza del rettangolo\n>>>"))
    print ("Il perimetro del rettangolo è",(base_rettangolo*2 + altezza_rettangolo*2))
elif figura_scelta == 3:
    Pi_greco = 3.14
    raggio_cerchio = float(input("Inserisci la lunghezza del raggio del cerchio:\n>>>"))
    print ("La circonferenza del cerchio è", Pi_greco*raggio_cerchio*2)
else:
    print ("La scelta selezionata non è valida")



