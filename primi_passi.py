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