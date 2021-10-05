print("****WRAPPER*****")


from functools import wraps
import wrapper

def caps_lock(funzione_parametro):
  @wraps(funzione_parametro)
  def wrapper():
    return funzione_parametro().upper()
  return wrapper

@caps_lock
def mia_funzione()
  return "sono piccolo ma carino"

def funzione_decoratore(funzione_parametro)
  def wrapper():
    print("... codice da eseguire prima di funzione parametro")
    funzione_parametro()
    print("... codice da eseguire dopo di funzione parametro")
  return wrapper()

def mia_funzione():
    print("CIAO!!!")
    return "CIAO!!!!!"

mia_funz = funzione_decoratore(mia_funzione)