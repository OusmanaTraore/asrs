def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None
    
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
