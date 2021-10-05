print("********* CLASSI ESEMPI ******")
import csv
class Persona:
  '''
    def __init__(self,nome,cognome,green_pass):
    pass
  '''  
  def __init__(self, nome, cognome, eta, green):
    self.nome=nome
    self.cognome=cognome
    self.eta=eta
    #self.corso=corso
    self.green=green

  @classmethod #costruttore alternativo!!!
  def inizializza(cls, lista):
    #nome,cognome,eta,corso,green=lista.split(';') #interessante al posto di una lista, posso mettere tante variabili a sinistra quanti sono gli elementi
    nome=lista[0]
    cognome=lista[1]
    eta=lista[2]
    green=lista[3]

    return cls(nome,cognome,eta,green)
 
  @staticmethod
  def info_prog(s):
    info = """
    Nome: Persona
    Creato da: Emanuele
    Commenti; scritto usando Python 3
      """
    return info + s
  def stampa(self):
    return f"Scheda Persona\n Nome:{self.nome}\n Cognome:{self.cognome}\n Greenpass:{self.green}"
  
  def dizionario(self):
    d={}
    chiave = self.nome + " " + self.cognome
    valore = self.eta + " " + self.green
    d[chiave]=valore
    return d
  
#stud1 = Studente("Giacomo;Leopardi;99;Letteratura;True")
dati=[]
with open("Files/elenco_persone.csv") as filecsv:
  lettore=csv.reader(filecsv,delimiter=";")
  for parola in lettore:
    dati.append(parola)
print(dati)


for i in range(1,len(dati)):
  p = Persona.inizializza(dati[i])
  print(p.stampa())
  print(p.dizionario())
  print()

#######

class Studente(Persona): #Studente eredita da Persona
  def __init__(self,nome,cognome,eta,green,corso):
    super().__init__(nome,cognome,eta,green) #richiamo l'init della superclasse
    self.corso=corso #aggiunho il nuovo parametro di inizializzazione della classe
  
  def scheda_personale(self):
    scheda = f"""
    Nome: {self.nome}
    Cognome: {self.cognome}
    Età: {self.eta}
    Greenpass?: {self.green}
    Corso : {self.corso}
    +++"""
    return scheda

studente_uno = Studente("Paolo", "Gnomo", "44", True,"Informatica")
print(studente_uno.scheda_personale())

with open("Files/elenco_studenti.csv") as filecsv:
  lettore=csv.reader(filecsv,delimiter=";")
  for riga in lettore:
    print(riga)

print(Studente.info_prog("ciao")) #richiamo di un metodo statioco
