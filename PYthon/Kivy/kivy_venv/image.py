from kivy.app import App
from kivy.properties import StringProperty,BooleanProperty
# from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.stacklayout import StackLayout
# from kivy.metrics import dp

class ImagesExemple(GridLayout):
    pass
    # mon_texte = StringProperty("0")
    # compteur = 0
    # compteur_actif = BooleanProperty(False)
    # # slider_value_txt = StringProperty("Valeur")
    # text_input_str = StringProperty("toto")


    # def on_button_click(self):
    #     print("Button click")

    #     if self.compteur_actif:
    #         self.compteur += 1
    #         self.mon_texte = str(self.compteur)

    # def on_toggle_button_state(self, widget):
    #     #print("toogle state: " + widget.state)
    #     if widget.state == "normal":
    #         # print("OFF")
    #         widget.text= "OFF"
    #         self.compteur_actif = False
    #     else:
    #         # print("ON")
    #         widget.text= "ON"
    #         self.compteur_actif = True
    
    # def on_switch_active(self, widget):
    #     print("Switch: " + str(widget.active))

    # def on_text_validate(self,widget):
    #     self.text_input_str = widget.text
    # #     print("Slider: " + str(int(widget.value)))
    #     # self.slider_value_txt = str(int(widget.value))



class imageApp(App):
    pass

imageApp().run()
