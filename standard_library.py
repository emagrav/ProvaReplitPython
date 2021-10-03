#import random               # importo modulo random. Per poter utilizzare tutte le sue funzioni
                            # devo far precedere il nome di ciascuna funzione da random
from random import randint  # qui invece importo solo funzione radint del modulo random e non
                            # devo far precedere il nome della funzione da random
#from random import *        # qui invece importo tutte le funzioni del modulo random e non
                            # devo far precedere il nome di ciascuna funzione da random

for n in range(10):
    #val = random.randint(1,50) # caso import random
    val = randint(1,50)         # caso from random import radint (ovvero from random import *)
    print(val)