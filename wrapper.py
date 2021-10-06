print("****WRAPPER*****")

if __name__ == "__main__":
  print("In Replit non sono dento il file 'main.py' per questo non vengo stampato. Se mi lanci con un editor come VisualStudio Code, invece mi puoi vedere")

print()
#due modi di usare la tecncia del wrapping

from functools import wraps

def caps_lock(funzione_parametro):
  @wraps(funzione_parametro)
  def wrapper():
    return funzione_parametro().upper()
  return wrapper

@caps_lock
def mia_funz():
  return "parto piccolo ma poi cresco"

print(mia_funz())

#########

def funzione_decoratore(funzione_parametro):
  def wrapper():
    print("... codice da eseguire prima di funzione parametro")
    funzione_parametro()
    print("... codice da eseguire dopo di funzione parametro")
  return wrapper()

def mia_funzione():
    print("sono piccolo e rimango tale")
    
funzione_decoratore(mia_funzione)
