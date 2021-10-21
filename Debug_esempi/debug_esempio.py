import pdb

print("*********DEBUG ESEMPIO*****")

for i in range(10):
  print(i)
  if i==5:
    pdb.set_trace()

print("fine ")
'''
posso nella Console poi premere 'i' per vedere i valore della
variabile i del ciclo
poi next poi c per continuare, exit, cl(ear), ecc.
'''