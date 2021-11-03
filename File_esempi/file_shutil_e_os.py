print("************FILE SHUTIL e OS****************")

import os
import shutil
from pathlib import Path

# ricavo l'oggetto Path associato a questo stesso file di script 
cur_path = Path(os.path.realpath(__file__))
# ricavo quindi il path assoluto della sua directory
parent_dir = cur_path.parent.absolute()
# ora il path della directory superiore
path = str(parent_dir.parent.absolute())

shutil.copy(path + "/Files/pippo.txt", path + "/Files/pluto.txt")
shutil.copy(path + "/Files/pippo.txt", path + "/Files/plutos.txt")

# altri metodi molto usati di shutils:
#shutils.move
#shutils.copytree
#shutils.rmtree

os.unlink(path + "/Files/plutos.txt") #elimina definitivamente plutos

lista=os.listdir(os.getcwd()) #ottengo lista dei file nella directory corrente (cwd=current working directory)
print(lista)


for cartelle, sottocartelle, file in os.walk(os.getcwd()): #questo metodo restituisce tre liste cartelle, sottocartelle e file
  print(f"ci troviamo nella cartella:{cartelle}")
  print(f"... dove ci sono le sottcartelle:{sottocartelle}")
  print(f"... dove ci sono i file: {file}")
  print()

def prova(): #una funzione è in grado di restituire più di un valore in questo case 3 liste
  return [1,2,3],[4,5,6],[7,8,9]

for a,b,c in prova():
  print(a)
  print(b)
  print(c)

