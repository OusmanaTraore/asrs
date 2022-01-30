from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.utils import platform
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import  NumericProperty, Clock
from kivy.graphics.vertex_instructions import Line, Quad, Triangle
from kivy.graphics.context_instructions import Color
import random

class MainWidget(Widget):
    from transforms import transform, transform_2D,transform_persective
    from user_actions import on_touch_up, on_touch_down, on_keyboard_down, on_keyboard_up , keyboard_closed
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    V_NB_LINES = 8
    V_LINES_SPACING = .4 # percentage in screen width
    vertical_lines = []
 
    H_NB_LINES = 8
    H_LINES_SPACING = .15 # percentage in screen width
    horizontal_lines = []

    SPEED = 0.2
    current_offset_y = 0
    current_y_loop = 0
    
    SPEED_X = 0.5
    current_speed_x = 0
    current_offset_x = 0

    #Variables du tile
    NB_TILES = 8 
    tiles = []
    tiles_coordinates = []


    #Triangle
    SHIP_WIDTH = 0.1
    SHIP_HEIGHT = 0.035
    SHIP_BASE_Y = 0.04
    ship = None
    ship_coordinates = [ (0, 0), (0, 0) , (0, 0)]

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__( **kwargs)
        #print("INIT W:" + str(self.width) + " H:" + str(self.height))
        self.init_vertical_lines()
        self.init_horizontal_lines()
        # tiles
        self.init_tiles()
        self.init_ship()

        self.pre_fill_tiles_coordinates()
        self.generate_tiles_coordinates()


        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)
        Clock.schedule_interval(self.update, 1.0/60.0)



    # Detection de la platform
    def is_desktop(self):
        if platform   in ('win', 'linux', 'macosx'):
            # print("platform: ",platform)
            return True
        else:
            return False
        #     print ("platform inconnue")


    def init_ship(self):
        with self.canvas:
            Color(0, 0, 0)
            self.ship = Triangle()

    def update_ship(self):
        center_x = self.width / 2
        base_y = self.SHIP_BASE_Y * self.height 
        half_width = self.SHIP_WIDTH * self.width / 2
        ship_height = self.SHIP_HEIGHT * self.height

        # ...self.transformation
        #     2
        # 1      3
        self.ship_coordinates[0] = (center_x - half_width, base_y)
        self.ship_coordinates[1] = (center_x, base_y + ship_height)
        self.ship_coordinates[2] = (center_x + half_width, base_y)

        x1, y1 = self.transform(*self.ship_coordinates[0])
        x2, y2 = self.transform(*self.ship_coordinates[1])
        x3, y3 = self.transform(*self.ship_coordinates[2])

        self.ship.points = [x1, y1, x2, y2, x3, y3]

    def check_ship_collisions(self):
        for i in range(0, len(self.tiles_coordinates)):
            ti_x, ti_y = self.tiles_coordinates [i]
            if ti_y > self.current_y_loop + 1 :
                return False
            if self.check_ship_collision_with_tile(ti_x, ti_y):
                return True
        return False


    def check_ship_collision_with_tile(self, ti_x, ti_y):
        xmin, ymin = self.get_tile_coordinates(ti_x,ti_y)
        xmax, ymax = self.get_tile_coordinates(ti_x+ 1,ti_y +1)

        for i in range(0,3):
            px, py = self.ship_coordinates[i]
            if xmin <= px <= xmax and ymin <= py <= ymax:
                return True
        return False
    

    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_TILES):
                self.tiles.append(Quad())

    def pre_fill_tiles_coordinates(self):
        for i in range(0, 10):
            self.tiles_coordinates.append((0,i))


    def generate_tiles_coordinates(self):
        last_x = 0
        last_y = 0

        for i in range(len(self.tiles_coordinates) -1, -1, -1):
            if self.tiles_coordinates[i][1] < self.current_y_loop:
                del self.tiles_coordinates[i]
        
        if len(self.tiles_coordinates) > 0:
            last_coordinate = self.tiles_coordinates[-1]
            last_x = last_coordinate[0] 
            last_y = last_coordinate[1] + 1

        for i in range(len(self.tiles_coordinates), self.NB_TILES):
            r = random.randint(0, 2)
            # 0 -> en avant
            # 1 -> à droite
            # 2 -> à gauche
            start_index = -int(self.V_NB_LINES / 2) +1 
            end_index = start_index + self.V_NB_LINES -1
            if last_x <= start_index:
                r = 1
            if last_x >= end_index:
                r = 2

            self.tiles_coordinates.append((last_x, last_y))
            if r ==1:
                last_x +=1
                self.tiles_coordinates.append((last_x, last_y))
                last_y +=1
                self.tiles_coordinates.append((last_x, last_y))
            elif r == 2:
                last_x -=1
                self.tiles_coordinates.append((last_x, last_y))
                last_y +=1
                self.tiles_coordinates.append((last_x, last_y))
            last_y +=1

    
    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())
    
    def get_line_x_from_index(self, index):
        """
        fonction permettant de recupérer les coordonées x d'un tile à l'écran
        """
        central_line_x = self.perspective_point_x
        spacing = self.V_LINES_SPACING * self.width  # espacement entre deux lignes
        offset = index - 0.5
        line_x = central_line_x + offset*spacing + self.current_offset_x
        return line_x
   
    def get_line_y_from_index(self, index):

        """
        fonction permettant de recupérer les coordonées y d'un tile à l'écran
        """

        spacing_y = self.H_LINES_SPACING * self.height  # espacement entre deux lignes
        line_y = index * spacing_y - self.current_offset_y
        return line_y
    
    def get_tile_coordinates(self, ti_x, ti_y):
        ti_y = ti_y - self.current_y_loop
        x = self.get_line_x_from_index(ti_x) 
        y = self.get_line_y_from_index(ti_y) 
        return  x,y
        """
        fonction permettant de recupérer les coordonées x et y d'un tile à l'écran
        """

    
    def update_tiles(self):
        for i in range(0, self.NB_TILES):
            tile = self.tiles[i]
            tile_coordinates = self.tiles_coordinates[i]
            xmin, ymin = self.get_tile_coordinates(tile_coordinates[0], tile_coordinates[1])
            xmax, ymax = self.get_tile_coordinates(tile_coordinates[0]+1, tile_coordinates[1]+1)

        x1, y1 = self.transform(xmin, ymin)
        x2, y2 = self.transform(xmin, ymax)
        x3, y3 = self.transform(xmax, ymax)
        x4, y4 = self.transform(xmax, ymin)

        tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]

    def update_vertical_lines(self):
        start_index = -int(self.V_NB_LINES/2) +1 
        for i in range(start_index, start_index+ self.V_NB_LINES):
            line_x = self.get_line_x_from_index(i)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x,  self.height)
            self.vertical_lines[i].points=[x1, y1, x2, y2]
    
    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())
    
    def update_horizontal_lines(self):
        start_index = -int(self.V_NB_LINES/2) +1 
        end_index = start_index + self.V_NB_LINES -1

        xmin = self.get_line_x_from_index(start_index)
        xmax = self.get_line_x_from_index(end_index)
        for i in range(0, self.H_NB_LINES):
            line_y = self.get_line_y_from_index(i) # ajout du current offset_y
            x1, y1 = self.transform(xmin, line_y)
            x2, y2 = self.transform(xmax,  line_y)
            self.horizontal_lines[i].points=[x1, y1, x2, y2]
    
 
    
    # Rafraichissement des lignes horizontales et verticales
    def update(self, dt):
        time_factor = dt*60 #prise en compte du Delta Time
        
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.update_tiles()
        self.update_ship()

        speed_y = self.SPEED * self.height / 100
        self.current_offset_y +=  speed_y *time_factor

        spacing_y = self.H_LINES_SPACING * self.height

        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y
            self.current_y_loop += 1
            self.generate_tiles_coordinates()
            
        speed_x = self.current_speed_x * self.width / 100
        self.current_offset_x +=  speed_x *time_factor

        if not self.check_ship_collisions():
            print("GAME OVER")

  
class GalaxyApp(App):
    pass


GalaxyApp().run()
