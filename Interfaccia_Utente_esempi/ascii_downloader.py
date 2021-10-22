import tkinter as tk
import requests

def download_ascii():
    # verifico se la stringa che restituisce il metodo get del widget Entry sia non nulla (True)
    if text_input.get(): 
        text_response = text_input.get()
    else:
        text_response = "Aggiungi una parola o una frase nel campo di testo!"
    
    # text area
    textwidget = tk.Text() 
    # tk.END corrisponde alla posizione del cursore dopo l'ultimo carattere del buffer
    textwidget.insert(tk.END, text_response) 
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

# finestra
window = tk.Tk()
window.geometry("900x550")
window.title("ASCII ART DOWNLOADER")
"""
imposto che i widget che metterò in questa finestra si espanderanno per tutta la larghezza a 
disposizione. indice della colonna 0 (prima colonna) weight=1 espandere i widget sulla colonna
"""
window.grid_columnconfigure(0, weight=1) 

# label
welcome_label = tk.Label(window
                        , text="Welcome! Aggiungi una parola o una frase da scaricare:"
                        , font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)       

# casella di testo
text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)

# pulsante download
download_button = tk.Button(text="DOWNLOAD ASCII ART", command=download_ascii)
download_button.grid(row=2, column=0, sticky="WE", padx=10, pady=10)


if __name__ == "__main__":
    window.mainloop() # per aprire la finestra