from xmlrpc.client import Boolean
from storage_manager import StorageManager
from models import Pizza
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from kivy.properties import *
from kivy.lang import Builder
from http_client import HttpClient


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()

class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str =  StringProperty("")

    def __init__(self, **kwargs) :
        super().__init__(**kwargs)
        """self.pizzas = [
            Pizza("4 fromages","chèvre, emmental, brie, comté", 9.5, True),
            Pizza("Thon","tomates, parmessan, salade, thon", 11.2, False),
            Pizza("Orientales"," fromage, champignons, olives", 10, False)
        ]"""

        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data("pizzas", pizzas_dict)

    def on_server_error(self, error):
        print("ERREUR: " + error)
        self.error_str = "ERREUR: " + error

    def on_parent(self, widget, parent):
        # l = [pizza.get_dictionnary() for pizza in self.pizzas]
        pizzas_dict = StorageManager().load_data("pizzas")
        if pizzas_dict:
            self.recycleView.data= pizzas_dict
        
with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())

class PizzaApp(App):
    def build(self):
        return MainWidget()

PizzaApp().run()