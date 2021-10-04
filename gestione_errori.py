import sys
def divisore(a,b):
    ris = a / b
    return ris
    
try:
    print("Primo tenttivo;",divisore(4,2))
    #print("Secondo tenttivo;",divisore(5,0))
    print("Terzo tenttivo;",divisore("s",2))
except ZeroDivisionError as err:
    print('Hai una divisione per zero. {0}'.format(err))
except TypeError as err:
    print('Hai inserito caratteri non numerici. {0}'.format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
finally:
    print('comunque sia riesco a salutari. Fico!')

def moltiplicatore():
    try:
        a=int(input('inserisci il primo fattore: ')) #ValueError lo becchi anche passando 2.5 in quanto int(2.5) restiruisce 2 mentre int("2.5") da errore. Andrebbe risolto così in caso di necessità int(float("2.5"))
        b=int(input('inserisci il secondo fattore: '))
        ris = a * b
        print("Risultato:", ris)
    except ValueError:
        print('Inserisci solo numeri interi')
#moltiplicatore()
