print("*****CLASSI ESEMPI 2*********")

# importo il modulo persona.py e lo referenzio con stud
import studente as stud

# nel moduo referenziato da stud c'è una classe Studente
studente_due = stud.Studente("Paolo", "Gnomo", "44", True, "Informatica")
print(studente_due.scheda_personale())

# referenzio la variabile studente_uno contenuta nel modulo stud
print(id(stud.studente_uno)) 
print(id(studente_due))

# I due oggetti benché contenenti gli stessi dati, sono diversi (cfr. i loro id)
# Ma per Python la condizione di uguaglianza tra oggetti si ottiene
# qualora semplicemente contengano gli stessi dati
print(studente_due == stud.studente_uno) 

#####
# qui invece le due stringhe sono uguali in tutto e per tutto,
# persino a livelo di id
saluto1="ciao"
saluto2="ciao"

print(saluto1 == saluto2) 
print(id(saluto1))
print(id(saluto2))