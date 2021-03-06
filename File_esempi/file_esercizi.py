print("******FILE ESERCIZI*******")

import csv, os
from pathlib import Path

comune = []
monumento = []

# ricavo l'oggetto Path associato a questo stesso file di script 
cur_path = Path(os.path.realpath(__file__))
print("__file__:", __file__)
print("realpath(__file__):", os.path.realpath(__file__))

# ricavo quindi il path assoluto della sua directory
parent_dir = cur_path.parent.absolute()
# ora il path della directory superiore
path = str(parent_dir.parent.absolute())
# da quì posso partire per raggiungere il file di input
# NOTA: gli slash li prende anche Windows quindi questo script
# può girare anche in questo S.O.
path += "/Files/monumenti_unix.csv" 

print("Path assoluto del file csv di input:", path)

# NOTA: se la directory corrente (del terminale da cui viene
# lanciato lo script) fosse quella in cui è contenuto lo script
# allora per ottenere il path assoluto della directory superiore
# si potrebbe ottenere semplicemente così
parent_dir_path = os.path.abspath('..')
print("parent dir path:", parent_dir_path)

with open(path) as filecsv:
  lettore=csv.reader(filecsv, delimiter=";")
  
  for parola in lettore:
    if parola[0]=="ROMA":
      comune.append(parola[0])
      monumento.append(parola[3])
  print(comune)
  print(monumento)