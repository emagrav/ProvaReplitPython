print("**********classe_cane_esempio.py*******")
print()

class Cane_ver1: 
  # questa variabile dell'oggetto self è condivisa con tutte le istanze se non inizializzata in __init__
  attributi=[]

  def __init__(self, nome):
    self.nome = nome
    
    # Quì la variabile di self è inizializzata; pertanto 
    # il contenuto non sarà condiviso tra le diverse istanze della classe
    self.attributi = [] 
  
  def add_attributo(self, attributo):
    self.attributi.append(attributo)
  
  def __str__(self):
    return f"{self.nome} {self.attributi}"

class Cane_ver2:
  attributi=[]  
  
  def __init__(self, nome):
    self.nome = nome
  
    # In questo caso la variabile non la stiamo inizializzando, 
    # pertanto il suo contenuto sarà lo stesso per tutte le istanze.
    # Lo stesso dicasi anche nel caso la utilizzassimo (sempre qui nell'init), ad es.:
    # self.attributi.append(nome)
  
  def add_attributo(self, attributo):
    self.attributi.append(attributo)
  
  def __str__(self):
    return f"{self.nome} {self.attributi}"

# Nella versione 1 ogni cane ha i suoi attributi e li mantiene 
# anche qualora vengano definiti altri cani con altri attributi
d1=Cane_ver1('Woody')
d1.add_attributo('Meticcio')
d1.add_attributo('Nero e bianco')
print("<Cane ver. 1>", d1)

d2=Cane_ver1('Toby')
d2.add_attributo('Bassotto')
d2.add_attributo('Nero')
print("<Cane ver. 1>", d2)

# di nuovo Woody (che non è cambiato nel frattempo)
print("<Cane ver. 1>", d1)
print()

# Nella versione 2, invece, i cani condividono la stessa lista di attributi
d3=Cane_ver2('Rex')
d3.add_attributo('Pastore tedesco')
d3.add_attributo('Beige')
print("<Cane ver. 2>", d3)

d4=Cane_ver2('Gigi')
d4.add_attributo('Maltese')
d4.add_attributo('Bianco')
print("<Cane ver. 2>", d4)

# di nuovo Rex (che nel frattempo è cambiato)
print("<Cane ver. 2>", d3)
print()
'''
Pertanto, sintetizzando, se una variabile in una classe viene inizializzata nell'__init__
allora questa diventa una variabile d'istanza, altrimenti una variabile di classe condivisa
tra le varie istanze della classe stessa
'''