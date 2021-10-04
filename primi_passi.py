print ("*****PRIMI_PASSI.PY*******")

print('Hello, world!')
for x in range(10):
  print(x)
print ("anvedi!!")
###

############################
# alcune funzioni delle stringhe
############################
nome="Ele"
citta="RoMa"
frase = "Mi chIAMo {}, sono nato a {} e vivO a {}".format(nome,citta,citta)
print(frase.upper())
print(frase.capitalize()) # capitalize rende la prima maiuscola e il resto minuscolo.
print(frase.lower())
print(frase)

# il find è case sensitive e mi restituisce la pos. della sottostringa o -1
print(frase.find("ELE")) 
print(frase.find("Ele"))

# se mi interessa sapere solo se è contenuta una stringa ma non mi interessa la sua posizione posso
# usare + semplicemente l'istruzione "insiemistica" 'in'
print("ELE" in frase)
print("ELE".capitalize() in frase)

# il 3° parametro della replace dice quante occorrenze della sottostringa contenuta nella stringa deve 
# essere sostituita. Se non è presente la repace agisce su tutte.
frase2 = frase.replace(frase[-4:],"TarANTo",1)
print(frase2)
frase2 = frase.replace(frase[-4:],"TarANTo")
print(frase2)

voto = 6.1
sufficiente = (voto >= 6.0) 
             # espr1   if    espr2    else    espr3
risultato = 'promosso' if sufficiente else 'bocciato' # operatore ternario
print(risultato)

#None Indica il valore nullo in python. Equivale al null del C o di java. Il valore None si può testare con l'operatore is.
X = None
print('X è nullo?:', X is None)
type(X)


print(int('0x7b',base=16)) #trasformo un esadecimale in intero
print(int('33',base=8)) #trasformo un ottale in intero

print('\u272A') #Unicode
print('\u2665')

print(ord("K"))
print(chr(75))

s="fjsfjksl"
print(s.isalpha())

# unisco elementi in una stringa con un separatore
l=('a','b','c')
print(' '.join(l))
l2=':'.join(l)
print(l2)
#ottenere lista di elementi da stringa con separatori dentro
l3=l2.split(":")
print(l3)

# togliere spazi a destra e a sinistra
s="    sdfsdfs     "
print('>>'+s+'<<')

z='>>'+s.strip()+'<<'
print(z)
print(z.strip('>>').strip('<<'))