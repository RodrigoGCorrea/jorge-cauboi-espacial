from entity import Entity
from library.PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()


class Enemy(Entity):
    def __init__(self, window, animation_path, animation_frame):
        super().__init__(window, animation_path, animation_frame)

    def update(self, level):
        self.clear_variables()
        self.fall()
        self.walk()
        self.jump()
        self.collision_y(level)
        self.collision_x(level)

    def spawn(self):
        self.animation.set_position()

    def render(self):
        self.animation.draw()
