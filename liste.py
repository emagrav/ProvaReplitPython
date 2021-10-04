print("**************LISTE*******")

# Differenza tra extend e append sulle liste
a = [1, 2, 3, 45, 65]
b = [1, 2, 3, 45, 65]
a.append(
    [66, 88]
)  # in questo caso aggiungo un elemento alla lista che è essa stessa una lista
print(a)

b.extend(
    [66, 88]
)  # in quest'altro caso invece estendo la lista con gli elementi della lista fornita come parametro
print(b)

print(a[-1])  #ultimo elemento che è una lista in questo caso

for n in range(5):
    print("ciclo n:", n)

primi = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
for primo in primi:
    print(primo)

lista_numerica = list(range(99, 300))  #come creare automaticamente una lista numerica grazie a range
print(lista_numerica)

# differenza tra del e remove
# del è un'istruzione e ha bisogno dell'inidice dell'elemento
# mentre remove ha bisogno del valore da rimuovere dalla lista
monty = ["spam","eggs","bacon","bob","alice","pluto"]
print("Lista iniziale", monty)
del monty[0]
monty.remove("pluto")
print("Lista finale", monty)

monty.insert(0,"spam")
monty.insert(5,"pluto") #ovvero monty,append("pluto")
print("Lista iniziale ripristinata", monty)

print("posizione di pluto",monty.index("pluto"))

alfabeto=["a","b","z","h","c","k","w","d","e"]
alfabeto.sort()
print(alfabeto)

alfabeto.sort(reverse=True)
print(alfabeto)

