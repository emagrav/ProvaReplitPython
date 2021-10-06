print ("***ITERATORI***")
class Reverse:
  def __init__(self, data):
    self.data = data
    self.index = len(data)
  def __iter__(self):
    return self

#yield a che serve?
#E' possibile definire delle classi che restituiscono un proprio iteratore

s = "ciao"
it = iter(s)
'''
print(it.next())
print(it.next())
print(it.next())
print(it.next())
'''
parola = 'spam'

#for i in range(len(parola)-1,.1,-1)

#zip crea una lista con le tuple corrispondenti agli elementi avnti lo stess indice

mesi = "Gennaio Febbraio Marzo".split()
entrate = [300, 260, 444]
spese = [100, 320, 80]

zippone = zip(mesi, entrate, spese)
print("Zip = ", zippone)

for mese, entrata, spesa in zippone:
  guadagno = entrata - spesa
  print("Guadagno nel mese di {0} : {1}".format(mese, guadagno))