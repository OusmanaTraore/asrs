from kivy.app import App
from kivy.uix.widget import Widget


class LayoutGame(Widget):
    pass


class LayoutApp(App):
    def build(self):
        return LayoutGame()


if __name__ == '__main__':
    LayoutApp().run()