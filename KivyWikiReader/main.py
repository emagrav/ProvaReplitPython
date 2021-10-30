# importiamo classe MDApp
from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
Screen:

     # https://kivy.org/doc/stable/guide/widgets.html#organize-with-layouts
    GridLayout:
        rows: 2

        # https://kivymd.readthedocs.io/en/latest/components/label/
        MDLabel:
            id: mdlab
            text: "Benvenuti su Wikipedia Reader"
            font_style: "H1"
            #padding_x: 30
        # https://kivymd.readthedocs.io/en/latest/components/button/#mdraisedbutton
        MDRaisedButton:
            id: mdbu
            text: "PREMI QUESTO TASTO!"
            # https://kivy.org/doc/stable/api-kivy.uix.widget.html?highlight=size_hint_x#kivy.uix.widget.Widget.size_hint_x
            # 1 equivale al 100% della larghezza del genitore e quindi, in questo caso, della schermata
            # 0.5 equivale al 50%
            size_hint_x: 1 
"""

class WikiReaderApp(MDApp):
    def build(self):
        self.title = "WikipediaReader"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "200" # la saturazione (rispetto ad es. a 400 abbiamo un indigo più chiaro)
        return Builder.load_string(KV)

WikiReaderApp().run()

