print("****LIST COMPREHENSIIONS*****")
print()

lista_uno = [1, 2, 3]
lista_due = [3, 1, 4]

mix = [(x,y) for x in lista_uno for y in lista_due if x != y]

print (mix)