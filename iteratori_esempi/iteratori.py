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

print("Zip = ", list(zip(mesi, entrate, spese)))

for mese, entrata, spesa in zip(mesi, entrate, spese):
  guadagno = entrata - spesa
  print("Guadagno nel mese di {0} : {1}".format(mese, guadagno))

x="5,33,16,9".split()
y="4,14,456,213".split()

aggr=zip(x,y)

aggr = list(aggr)