print("*****CLASSI ESEMPI 2*********")

import classi_esempi as es


studente_due = es.Studente("Paolo", "Gnomo", "44", True,"Informatica")
print(studente_due.scheda_personale())

print(id(es.studente_uno))
print(id(studente_due))

print(studente_due == es.studente_uno) # i due oggetti benché contenenti stessi dati sono diversi

#####
saluto1="ciao"
saluto2="ciao"

print(saluto1==saluto2) #qui invece le due stringhe sono uguali
print(id(saluto1))
print(id(saluto2))

######
class Universita:
  def __init__(self, corso, sede, aula, docente):
    self.corso=corso
    self.sede=sede
    self.aula=aula
    self.docente=docente
  def __str__(self):
    return f"Info su università {self.corso} {self.sede} {self.aula} {self.docente}"
class SuperStudente(es.Persona, Universita):
  def __init__(self,nome,cognome,eta,green,esami,corso,sede,aula,docente):
    self.esami=esami
    es.Persona.__init__(self,nome, cognome,eta,green)
    Universita.__init__(self,corso, sede, aula, docente)
  
  def __str__(self):
    return es.Persona.__str__(self) +  Universita.__str__(self)

giovanni = SuperStudente("Giovanni", "Ginger", "33", False,"tanti", "Religione", "Roma sede", "aula magna", "the best teacher")
print(giovanni)