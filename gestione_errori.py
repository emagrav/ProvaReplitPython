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
        a=int(input('inserisci il primo fattore: '))
        b=int(input('inserisci il secondo fattore: '))
        ris = a * b
        print("Risultato:", ris)
    except ValueError:
        print('Inserisci solo numeri interi')
moltiplicatore()
