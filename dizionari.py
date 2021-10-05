print("*************DIZIONARI**********")

mio_diz = {"key1":"val1","eta":24, 3.14:"pi_greco", "primi":[1,3,5,7]}

print(mio_diz["key1"])
print(mio_diz[3.14])

#aggiungo nuovo elemento
mio_diz["new_key"]="new_val"
print(mio_diz)

print("primi" in mio_diz) #verifico se una chiave è censita

del mio_diz["key1"]
print(mio_diz)

print(mio_diz.keys())
print(mio_diz.values())
print(mio_diz.items())

chiavi=list(mio_diz.keys())
valori=list(mio_diz.values())
voci=list(mio_diz.items())

print("Riepilogo chiavi:",chiavi)
print("Riepilogo valori:",valori)
print("Riepilogo voci:",voci)

#for k in chiavi:
for k in mio_diz.keys():
    print(k)

#get per gestire l'assenza di una chiave cercata per ottenere il corrispondente valore
print(mio_diz.get(3.14,"Voce non trovata nel dizionario"))
print(mio_diz.get("birra","Voce non trovata nel dizionario"))

#setdefault serve come get per gestire l'assenza ma anziché restituire un messaggio di default, assegna un nuovo elemento con la coppia chiave-valore indicata.
#qualora la chiave esistesse già, restituirebbe il valore già associato e non quello passato in questa istruzione
mio_diz.setdefault(3.14,"pi greco!!!")
mio_diz.setdefault("birra","Corona Extra")

print(mio_diz)

########
diction = {}
diction["a"] = "abello"
diction["b"] = "brutto"
diction["k"] = "ketteridi"

b=diction.copy() #creo una copia del dizionario

print("D1=",diction)
print("Copy1=",b)

del b["k"] # cancello un elemento del dzionario copia

print("D2=",diction)
print("Copy2=",b)
