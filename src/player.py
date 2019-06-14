from pygame.transform import flip
from entity import Entity
from library.PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()


class Player(Entity):
    def __init__(self, window, animation_path, animation_frame):
        super().__init__(window, animation_path, animation_frame)
        self.animation.set_position(globals.WIDTH / 2, 500)

    def update(self, level):
        self.clear_variables()
        self.fall()
        self.walk()
        self.jump()
        self.collision_y(level)
        self.collision_x(level)

    def render(self):
        if (
            self.velocity["x"] == 0
            and self.velocity["y"] == 0
            and globals.CAMERA_MOVING == False
            or self.jumping
        ):
            self.set_animation("./src/assets/actors/jorge/idle.png", 8)
        else:
            self.set_animation("./src/assets/actors/jorge/running.png", 8)

        if self.direction["left"]:
            self.animation.image = flip(self.animation.image, True, False)

        self.animation.update()
        self.animation.draw()
