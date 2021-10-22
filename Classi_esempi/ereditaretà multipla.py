from studente import Persona

class InfoCorso:
  def __init__(self, corso, sede, aula, docente):
    self.corso=corso
    self.sede=sede
    self.aula=aula
    self.docente=docente

  def __str__(self):
    return f"Info su università {self.corso} {self.sede} {self.aula} {self.docente}"

# esempio di ereditarietà multipla
class SuperStudente(Persona, InfoCorso):
  def __init__(self, nome, cognome, eta, green, esami, corso, sede, aula, docente):
    # questo è l'unico parametro nuovo, gi altri sono per metà noti da una superclasse
    # e l'altra metà dall'altra
    self.esami = esami 
    
    Persona.__init__(self, nome, cognome, eta, green)
    InfoCorso.__init__(self, corso, sede, aula, docente)
  
  def __str__(self):
    return Persona.__str__(self) + ", esami " + self.esami + "\n" + \
            InfoCorso.__str__(self)

# un oggetto di questa classe derivata da due superclassi
giovanni = SuperStudente("Giovanni"
                        , "Ginger"
                        , "33"
                        , False
                        , "tanti"
                        , "Religione"
                        , "Roma sede"
                        , "aula magna"
                        , "the best teacher")
print(giovanni)