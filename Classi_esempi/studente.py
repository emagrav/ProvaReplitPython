from persona import Persona 
import csv

# Ecco come si specifica in python che Studente 
# eredita (giustamente) da Persona
class Studente(Persona): 
  def __init__(self, nome, cognome, eta, green, corso):
    #richiamo l'init della superclasse
    #super().__init__(nome,cognome,eta,green) 
    
    #alternativa a richiamare super(). L'unica differenza 
    # è che in questo caso devo passare anche self
    Persona.__init__(self, nome, cognome, eta, green)
    
    # gestisco il nuovo parametro (rispetto a Persona) di inizializzazione dell'oggetto
    self.corso = corso 
  

  def scheda_personale(self):
    '''
    ridefinizione di scheda personale della superclasse Persona
    '''
    scheda = super().scheda_personale()
    scheda += f"Corso : {self.corso}"

    return scheda
  
  def __str__(self):
    return f"Studente {self.nome} {self.cognome}"

# uso questa if per capire se questo file "studente.py" viene importato come modulo
# da altri file python per usare le classi qui definite o se sto lanciando proprio 
# direttamente questo modulo
# Ricorda: solo il modulo che viene lanciato assume il valore __main__
# con questa if riesco ad evitare che il file python che importa questo modulo non esegua
# anche tutto il codice (con le print che c'è qui sotto)
if __name__ == "__main__":  
  studente_uno = Studente("Paolo"
                          , "Gnomo"
                          , "44"
                          , True
                          , "Informatica")
  print(studente_uno.scheda_personale())

  with open("Files/elenco_studenti.csv") as filecsv:
    lettore = csv.reader(filecsv, delimiter=";")
    
    for lista_riga in lettore:
      print(lista_riga)
      # TO DO
  # richiamo di un metodo statico definito in Persona
  # e richiamato dalla sottoclasse Studente
  print(Studente.info_prog(">>>>>>>> ciao <<<<<<<<<"))

  # uso della funzione isistance per gli oggetti e issubclass per le classi
  print("studente_uno è un'istanza di Persona?", isinstance(studente_uno, Persona))
  print("studente_uno è un'istanza di Studente?", isinstance(studente_uno, Studente))
  print("Studente eredita da Persona?", issubclass(Studente, Persona))