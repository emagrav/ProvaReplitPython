print("**********classe_cane_esempio.py*******")
print()

class Cane:
  attributi=[] #visibile a tutte le istanze (non me l'aspettavo)
  def __init__(self, nome):
    self.nome = nome
  def add_attributo(self, attributo):
    self.attributi.append(attributo)
  def __str__(self):
    return f"{self.nome} {self.attributi}"

d=Cane('Fido')
d.add_attributo('Maltese')
d.add_attributo('Bianco')
print(d)

d2=Cane('Gigi')
d2.add_attributo('Maltesino')
d2.add_attributo('Bianchino')
print(d2)

class Cane2: 
  def __init__(self, nome):
    self.nome = nome
    self.attributi = [] #in questo caso la lista attributi vive solo nell'stanza della classe
  def add_attributo(self, attributo):
    self.attributi.append(attributo)
  def __str__(self):
    return f"{self.nome} {self.attributi}"

d=Cane2('Fido')
d.add_attributo('Maltese')
d.add_attributo('Bianco')
print(d)

d2=Cane2('Gigi')
d2.add_attributo('Maltesino')
d2.add_attributo('Bianchino')
print(d2)
