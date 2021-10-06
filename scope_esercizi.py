print("*******scope_esercizi********")
print()

spam = "" #questo è spam globale

def scope_test():

  spam = "test spam" #questo spam è nonlocal

  def do_local():
    spam = "local spam"
    print(">>Interno local:", spam)
  
  def do_nonlocal():
    nonlocal spam #definisco nonlocal la vaiabile spam quindi punto allo spam nonlocal
    spam = "nonlocal spam" #modifico spam non locale
    print(">>Interno nonlocal:", spam)

  def do_global():
    global spam  #definisco global la vaiabile spam
    spam = "global spam"
    print(">>Interno gobal:", spam)

  def try_nonlocal():
    #nonlocal spam
    print("Provo se nonlocal:", spam)
  
  do_local()
  print("Dopo assegn. local:", spam)
  print()
  
  try_nonlocal()
  print("Dopo tentativo nonlocal:", spam)
  print()

  do_nonlocal()
  print("Dopo assegn. nonlocal:", spam)
  print()

  do_global()
  print("Dopo assegn. global:", spam)
  print()

  try_nonlocal()
  print("Dopo tentativo nonlocal:", spam)
  print()
  

scope_test()
print("Nello scope globale:", spam)