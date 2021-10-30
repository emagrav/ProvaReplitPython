class Mente_e_Corpo:

    def __init__(self):
        pass
 
    def penso(self, pensiero):
        if pensiero == "Ora giocherò bene":
            self.gioca("Meglio")
    
    def gioca(self, come):
        if come == "Concentrato":
            self.attenzione = "Elevata"
            self.distrazione = "Assente"
            self.errori_gratuiti = "Rari e comunque giusti"
            self.corri("Su tutte le palle")
            self.servi_prima("Alla grande")
            self.servi_seconda("Alla grande")
            self.colpisci_diritto("Alla grande")

        if come == "Meglio":
            self.attenzione = "Adeguata"
            self.distrazione = "Molto ridotta"
            self.errori_gratuiti = "Descisamente diminuiti"
            self.corri("Su tutte le palle")
            self.rispondi("in campo")
            self.servi_prima("Percentuale")
            self.servi_seconda("Percentuale")
            self.colpisci_diritto("Bene")
            self.colpisci_rovescio("Bene")
            self.gioca("Concentrato")
            
    def corri(self, come):
        if come == "Su tutte le palle":
            self.fiato = "Tanto"
            self.velocita = "Elevata"
            self.coordinazione = "Elevata"
            self.fiducia = "Elevata"
            self.atleticita = "Elevata"
            self.dolori = "Nessuno"

    def pensa(self, nuovo_pensiero):
        self.penso(nuovo_pensiero)
    
    def servi_prima(self, come):
        if come == "Alla grande":
            self.tecnica = "Perfetta"
            self.precisione = "Elevata"
            self.forza = "Eccezionale"
            self.rotazione = "Lieve kick"
        if come == "Percentuale":
            self.tecnica = "Buona"
            self.precisione = "Buona"
            self.forza = "Adeguata"
            self.rotazione = "Kick medio"

    def servi_seconda(self, come):
        if come == "Alla grande":
            self.tecnica = "Perfetta"
            self.precisione = "Elevata"
            self.forza = "Adeguata"
            self.rotazione = "Tanto kick"
        
        if come == "Percentuale":
            self.tecnica = "Buona"
            self.precisione = "Buona"
            self.forza = "Adeguata"
            self.rotazione = "Kick elevato"


    def colpisci_diritto(self, come):
        if come == "Alla grande":
            self.tecnica = "Perfetta"
            self.precisione = "Elevata"
            self.forza = "Eccezionale"

    def colpisci_rovescio(self, come):
        if come == "Alla grande":
            self.tecnica = "Perfetta"
            self.precisione = "Elevata"
            self.forza = "Eccezionale"

m = Mente_e_Corpo()

if m.penso("Come sto giocando male"):
     m.pensa("Ora giocherò bene")

if m.penso("Devo vincere"):
    m.gioca("Concentrato")