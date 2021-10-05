print("********* CLASSI ESEMPI ******")
import csv
class Persona:
  '''
    def __init__(self,nome,cognome,corso,green_pass):
    pass
  '''  
  def __init__(self, lista):
    #nome,cognome,eta,corso,green=lista.split(';') #interessante al posto di una lista, posso mettere tante variabili a sinistra quanti sono gli elementi
    nome=lista[0]
    cognome=lista[1]
    eta=lista[2]
    corso=lista[3]
    green=lista[4]

    self.nome=nome
    self.cognome=cognome
    self.eta=eta
    self.corso=corso
    self.green=green
  
  def stampa(self):
    return f"Scheda Studente\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso:{self.corso}\n Greenpass:{self.green}"
  
  def dizionario(self):
    d={}
    chiave = self.nome + " " + self.cognome
    valore = self.eta + " " + self.corso + " " + self.green
    d[chiave]=valore
    return d
  
#stud1 = Studente("Giacomo;Leopardi;99;Letteratura;True")
dati=[]
with open("Files/elenco_studenti.csv") as filecsv:
  lettore=csv.reader(filecsv,delimiter=";")
  for parola in lettore:
    dati.append(parola)
print(dati)


for i in range(1,len(dati)):
  p = Persona(dati[i])
  print(p.stampa())
  print(p.dizionario())
  print()