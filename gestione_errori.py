def divisore(a,b):
    try:
        ris = a / b
        print("il risultto della divisione è:", ris)
    except ZeroDivisionError:
        print('Hai una divisione per zero.')

divisore(4,2)
divisore(5,0)

def moltiplicatore():
    try:
        a=int(input('inserisci il primo fattore: ')) #ValueError lo becchi anche passando 2.5 in quanto int(2.5) restiruisce 2 mentre int("2.5") da errore. Andrebbe risolto così in caso di necessità int(float("2.5"))
        b=int(input('inserisci il secondo fattore: '))
        ris = a * b
        print("Risultato:", ris)
    except ValueError:
        print('Inserisci solo numeri interi')
moltiplicatore()
