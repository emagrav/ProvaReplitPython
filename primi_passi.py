print('Hello, world!')
for x in range(10):
  print(x)
print ("anvedi!!")
###
nome="Ele"
citta="RoMa"
frase = "Mi chIAMo {}, sono nato a {} e vivO a {}".format(nome,citta,citta)
print(frase.upper())
print(frase.capitalize())
print(frase.lower())
print(frase)
print(frase.find("ELE"))
print(frase.find("Ele"))
print("ELE" in frase)
print("ELE".capitalize() in frase)
frase2 = frase.replace(frase[-4:],"TarANTo",1)
print(frase2)
frase2 = frase.replace(frase[-4:],"TarANTo")
print(frase2)