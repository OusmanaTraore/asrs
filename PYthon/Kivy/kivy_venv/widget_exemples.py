from kivy.properties import StringProperty,BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file('widget_exemples.kv')

class WidgetsExemple(GridLayout):
    mon_texte = StringProperty("0")
    compteur = 0
    compteur_actif = BooleanProperty(False)
    # slider_value_txt = StringProperty("Valeur")
    text_input_str = StringProperty("toto")


    def on_button_click(self):
        print("Button click")

        if self.compteur_actif:
            self.compteur += 1
            self.mon_texte = str(self.compteur)

    def on_toggle_button_state(self, widget):
        #print("toogle state: " + widget.state)
        if widget.state == "normal":
            # print("OFF")
            widget.text= "OFF"
            self.compteur_actif = False
        else:
            # print("ON")
            widget.text= "ON"
            self.compteur_actif = True
    
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    def on_text_validate(self,widget):
        self.text_input_str = widget.text
    #     print("Slider: " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))

class ImagesExemple(GridLayout):
    pass