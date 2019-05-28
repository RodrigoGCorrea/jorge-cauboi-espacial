from entity import Entity
from library.PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()

class Player(Entity):
    def __init__(self, window, animation_path, animation_frame):
        super().__init__(window, animation_path, animation_frame)
        self.animation.set_position(globals.WIDTH/2, 500)

    def update(self, level):
        self.clear_variables()
        self.fall()
        self.walk()
        self.jump()
        self.collision_y(level)
        self.collision_x(level)
