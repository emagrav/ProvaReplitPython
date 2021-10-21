import tkinter as tk
from typing import Text

window = tk.Tk() # creo nuova finestra
window.geometry("600x600") # grandezza in pixel
window.title("Ciao bella gente!") # titolo della finestra
window.resizable(False, False) # rendo la finestra immodificabile come dimensioni (false larghezza e altezza) perché altrimenti posso modificare le dimensione della finestra trascinando i bordi col mouse
window.configure(background="gray") # cambio lo sfondo

def first_function():
    text = "Hello World!"
    # creo una label con un testo, un colore (foreground) e un font (family, size)
    text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 16)) 
    text_output.grid(row=0, column=1, sticky="W") # la posiziono alla destra del pulsantee la incollo, aggancio a ovest

def second_function():
    text = "Nuovo messaggio, nuova funzione!"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16)) 
    text_output.grid(row=1, column=1, padx=50, sticky="W") # ...sotto il primo messaggio e spaziatura sull'asse x di 50 su entrambi i lati


first_button = tk.Button(text="Saluta!", command=first_function) # creo pulsante e associo al click il richiamo di una funzione
first_button.grid(row=0, column=0, sticky="W") # e con grid lo posiziono in alto a sx (perché lo associa direttamente a window?)

second_button = tk.Button(text="Secondo messaggio!", command=second_function)
second_button.grid(row=1, column=0, pady=20, sticky="W") # sotto al primo pulsante, la riga sotto, spaziatura sull'asse y (verticalmente quindi) di 20 sopra e sotto



if __name__ == "__main__":
    window.mainloop() # per aprire la finestra