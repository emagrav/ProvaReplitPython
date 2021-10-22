import csv

print("********* CLASSI ESEMPI ******")

class Persona:
  def __init__(self, nome, cognome, eta, green):
    self.nome=nome
    self.cognome=cognome
    self.eta=eta
    self.green=green

  # repr è pensato più per fornire informazioni di stato dell'oggetto più approfondite ad uso tecnico
  def __repr__(self): #richiamabile tramite repr(oggetto)
    return f"Persona {self.nome} {self.cognome}"
  
  # str invece deve fornire lo stato in maniera meno complicata e sotto forma di stringa
  def __str__(self): #richiamabile tramite str(oggetto) o anche print oggetto in quanto è il metodo di default
    return f"Mi chiamo {self.nome} {self.cognome}"

  
  @classmethod 
  def inizializza(cls, lista):
    '''
    costruttore alternativo dove, anziché passare i singoli paramentri 
    uno alla volta, è possibile passare una lista che li comprende tutti
    '''
    nome=lista[0]
    cognome=lista[1]
    eta=lista[2]
    green=lista[3]

    # se invece di farmi passare una lista avessi deciso di farmi passare una stringa 
    # con i valori delle colonne/campi separati da un separatore, ad es. ";", avrei
    # potuto ottenere le quattro variabili precedenti in un sol colpo, con un'unica istruzione
    #nome, cognome, eta, corso, green = lista.split(';') 
    
    # richiamo quindi il costruttore  passando i singoli parametri
    return cls(nome, cognome, eta, green)
 
  @staticmethod
  def info_prog(s):
    info = """
    Nome: Persona
    Creato da: emagrav
    Commenti: scritto usando Python 3
    """
    return info + s

  def stampa(self):
    return f"Scheda Persona\n Nome:{self.nome}\n Cognome:{self.cognome}\n Greenpass:{self.green}"
  
  def scheda_personale(self):
    scheda = f"""
    Nome: {self.nome}
    Cognome: {self.cognome}
    Età: {self.eta}
    Greenpass?: {self.green}
    """
    return scheda
  
  def getDizionario(self) -> dict:
    '''
    compone un dizionario di un solo elemento (coppia chiave-valore)
    formato da Nome + Cognome come chiave e come valore invece da 
    età + True/False (a seconda se il soggetto è dotato o meno di green pass)
    '''
    d={}
    
    chiave = self.nome + " " + self.cognome
    valore = self.eta + " " + self.green
    d[chiave]=valore
    
    return d

# uso questa if per capire se questo file "persona.py" viene importato come modulo
# da altri file python per usare le classi qui definite o se sto lanciando proprio 
# direttamente questo modulo
# Ricorda: solo il modulo che viene lanciato assume il valore __main__
# con questa if riesco ad evitare che il file python che importa questo modulo non esegua
# anche tutto il codice (con le print che c'è qui sotto)
if __name__ == "__main__":  
  # carico una lista con le righe (a loro volta liste) presenti nel file 
  lista_righe_del_file=[]

  with open("Files/elenco_persone.csv") as filecsv:
    # csv.reader() restituisce un oggetto iterabile (il file) di liste (le righe)
    lettore = csv.reader(filecsv, delimiter=";") 
    for lista_riga in lettore: 
      lista_righe_del_file.append(lista_riga)

  # stampo la lista delle righe (che, a loro volta, sono liste di elementi delle colonne/campi)
  print(lista_righe_del_file)

  # ciclo negli elementi della listone associato al file
  for i in range(len(lista_righe_del_file)):
    p = Persona.inizializza(lista_righe_del_file[i]) # qui utilizzo il costruttore alternativo a cui passo la riga (che ricordo è una lista)
    print(p.stampa())
    print(p.getDizionario())
    print()
