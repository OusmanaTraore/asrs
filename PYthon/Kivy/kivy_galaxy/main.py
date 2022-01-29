from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.utils import platform
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import  NumericProperty, Clock
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color


class MainWidget(Widget):
    from transforms import transform, transform_2D,transform_persective
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 10
    V_LINES_SPACING = .25 # percentage in screen width
    vertical_lines = []
 
    H_NB_LINES = 15
    H_LINES_SPACING = .1 # percentage in screen width
    horizontal_lines = []

    SPEED = 2
    current_offset_y = 0
    
    SPEED_X = 12
    current_speed_x = 0
    current_offset_x = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__( **kwargs)
        #print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update, 1.0/60.0)

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard = None

    # Detection de la platform
    def is_desktop(self):
        if platform   in ('win', 'linux', 'macosx'):
            # print("platform: ",platform)
            return True
        else:
            return False
        #     print ("platform inconnue")

    

    def on_parent(self, widget, parent):
        print("ON PARENT W:" + str(self.width) + " H:" + str(self.height))

    def on_size(self, *args):
        pass
        # self.update_vertical_lines()
        # self.update_horizontal_lines()
        # print("ON SIZE W:" + str(self.width) + " H:" + str(self.height))
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * 0.75
    
    def on_perspective_point_x(self, widget, value):
        pass
        # print("PX: " + str(value))

    def on_perspective_point_y(self, widget, value):
        pass
        # print("PY: " + str(value))

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            #self.line = Line(points=[100, 0, 100, 100 ])
            # V_NB_LINES = 7
            # V_LINES_SPACING
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())
    
    def update_vertical_lines(self):
        # self.line.points = [ self.perspective_point_x, 0, self.perspective_point_y, 100]
        central_line_x = self.width / 2
        spacing = self.V_LINES_SPACING * self.width  # espacement entre deux lignes
        offset = -int(self.V_NB_LINES/2) + 0.5
        for i in range(0, self.V_NB_LINES):
            line_x = int(central_line_x + offset*spacing + self.current_offset_x)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x,  self.height)
            self.vertical_lines[i].points=[x1, y1, x2, y2]
            offset += 1
    
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())
    
    def update_horizontal_lines(self):
        central_line_x = self.width / 2
        spacing = self.V_LINES_SPACING * self.width 
        offset = -int(self.V_NB_LINES/2) + 0.5

        xmin = central_line_x + offset* spacing +self.current_offset_x
        xmax = central_line_x - offset* spacing +self.current_offset_x
        spacing_y = self.H_LINES_SPACING * self.height # espaces vertical entre deux lignes horizontale
        for i in range(0, self.H_NB_LINES):
            line_y =  i * spacing_y - self.current_offset_y # ajout du current offset_y
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax,  line_y)
            self.horizontal_lines[i].points=[x1, y1, x2, y2]
    
 
    
    # Rafraichissement des lignes horizontales et verticales
    def update(self, dt):
        time_factor = dt*60 #prise en compte du Delta Time
        
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.current_offset_y +=  self.SPEED *time_factor

        spacing_y = self.H_LINES_SPACING * self.height

        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y

        self.current_offset_x +=  self.current_speed_x *time_factor

    # appui des touches sur ecran
    def on_touch_down(self, touch):
        if touch.x < self.width/2:
            #print("<-")
            self.current_speed_x = self.SPEED_X
        else: 
            #print("->")
            self.current_speed_x = - self.SPEED_X

    # relachement des touches 
    def on_touch_up(self, touch):
        #print("UP")
        self.current_speed_x = 0


    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            print("<-")
            self.is_desktop()
            self.current_speed_x = self.SPEED_X
        elif keycode[1] == 'right':
            print("->")
            self.current_speed_x = - self.SPEED_X
        return True
    
    def on_keyboard_up(self, keyboard, keycode):
        self.current_speed_x = 0

class GalaxyApp(App):
    pass


GalaxyApp().run()
