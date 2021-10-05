print("****WRAPPER*****")

#due modi di usare la tecncia del wrapping

from functools import wraps

def caps_lock(funzione_parametro):
  @wraps(funzione_parametro)
  def wrapper():
    return funzione_parametro().upper()
  return wrapper

@caps_lock
def mia_funz():
  return "sono piccolo ma carino"

print(mia_funz())

#########

def funzione_decoratore(funzione_parametro):
  def wrapper():
    print("... codice da eseguire prima di funzione parametro")
    funzione_parametro()
    print("... codice da eseguire dopo di funzione parametro")
  return wrapper()

def mia_funzione():
    print("sono piccolo ma carino")
    
funzione_decoratore(mia_funzione)
