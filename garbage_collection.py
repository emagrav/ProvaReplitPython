
print("*********GARBAGE COLLECTION**********")

import gc
print(gc.get_threshold()) #(700,10,10)
#print(gc.get_objects(0)) #sbrodolata non so bene di cosa 

gc.set_threshold(700,5,5)
print(gc.get_threshold()) #(700,5,5)

gc.set_threshold(700,10,10)
print(gc.get_threshold()) #(700,10,10)


######################################


i=0
def ciclo():
  x={}
  x[i+1]=x #la chiave corrente punta al dizionario
  print(x)

collected=gc.collect()
print("Garbage collector: %d oggetti collezionati" %(collected))

# stampiamo il ciclo
for i in range(10):
    ciclo()

collected=gc.collect()
print("Garbage collector: %d oggetti collezionati" %(collected))


print('\u272A') #Unicode
print('\u2665')