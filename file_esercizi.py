print("******FILE ESERCIZI*******")

import csv

comune = []
MONUMENTO = []

with open("monumenti_unix.csv") as filecsv:
  lettore=csv.reader(filecsv, delimiter=";")
  
  for parola in lettore:
    if parola[0]=="ROMA":
      comune.append(parola[0])
      MONUMENTO.append(parola[3])
  print(comune)
  print(MONUMENTO)