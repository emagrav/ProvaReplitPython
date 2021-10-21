import sys
print("********* CONTEGGIO DEI RIFERIMENTI******")

val = 377767099
val1 = '3/7/67099'

print(sys.getrefcount(377767099)) #forse va usato con le variabili e non con i dati direttamente... boh!?

print(sys.getrefcount(377767091111))
#del(val)
print(377767099+1)
a=377767099+1
#print(val)
print(sys.getrefcount(val))

print('Dato intero La misura è espressa in byte', sys.getsizeof(val))
print('Dato stringa La misura è espressa in byte', sys.getsizeof('3/7/67099'))
print('Dato stringa La misura è espressa in byte', sys.getsizeof('3/7/670990'))