print ("*****FUNZIONI.PY*******")
def somma(a,b):
    ris=a+b
    return (ris)

print(somma(1,5))
##################
x=14
def funzione_che_usa_var_globale_1():
    global x
    x += 2 # essendo questa istruzione equivalente ad x = x + 2
           # se prima non fosse dichiarata la variabile x come global che farebbe intendere all'interprete 
           # che x è la stessa definita a livello globale... oppure se prima non fosse presente un'assegnazione
           # di x tale da far capire all'interprete che questa x è locale e, pertanto, diversa dall'omonima 
           # globale, questa istruzione andrebbe in errore in quanto prima cercherebbe di leggere il valore 
           # della globale (l'x dopo l'uguale dell'assegnazione) ma poi si ritroverebbe a dover eseguire 
           # un'assegnazione non consentita della variabile globale all'interno di uno scope locale quale 
           # quello, appunto, di una funzione. Per questo motivo l'interprete tratterebbe x come una variabile
           # locale che però non è stata definita in precedenza
    return(x)

print (funzione_che_usa_var_globale_1())
##################
def funzione_che_usa_var_globale_2():
    y = x   # in questo caso non c'è nessun errore in quanto leggo il valore della variabile globale ma non
            # cerco mai di modificarne il contenuto
    y += 2
    return (y)

print (funzione_che_usa_var_globale_2())

# PERTANTO LE VARIABILI GLOBALI POSSONO ESSERE tranquillamente LETTE MA NON MODIFICATE 
# all'interno di una funzione.
# SE LE SI VUOLE MODIFICARE, DEVONO ESSERE DICHIARATE come GLOBAL 