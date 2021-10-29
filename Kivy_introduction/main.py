from kivymd.app import MDApp
from kivy.lang import Builder

# In questa stringa multiriga vado a specificare i componenti utilizzati dall'app e le loro proprietà
# 
# che sarà al centro dello schermo (x=0.5, y=0.5)
KV = """
Screen: # Screen è il widget di primo livello (root)
    # pensavo di poter mettere qui anche le impostazioni di screen e invece le prende solo nel metodo build
    # title: "Hello Kitty! :)" 
    MDRectangleFlatButton: #esso contiene un pulsante piatto rettangolare
        #text: "Bello lu pulsante!" # con un testo 
        text: "Hello Kivy World!" # con un testo 
        #pos_hint: {"center_x": 0.5, "center_y": 0.5} # e la posizione del suo centro all'interno dello Screen
        # la posizione del punto (0,0) dello Screen corrisponde all'angolo in basso a sinistra
        pos_hint: {"center_x": 0, "center_y": 0} # e la posizione del suo centro all'interno dello Screen
        pos_hint: {"center_x": 0.25, "center_y": 0.25} # e la posizione del suo centro all'interno dello Screen
        pos_hint: {"x": 0, "y": 0} # e la posizione dell'angolo in basso a sinistra del widget all'interno dello Screen
"""


class MainApp(MDApp): # sto estendendo MDApp
    def build(self):
        self.title = "Hello Kivy" # se non impostato = Main
        self.theme_cls.theme_style = "Dark" # Light
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

MainApp().run()