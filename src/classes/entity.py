from environment import variables as gvar
from library.PPlay.gameimage import load_image
from library.PPlay.animation import Animation
from pygame.sprite import Sprite
from pygame import math


class Entity(Sprite):
    def __init__(self, window, sprite_path, frames):
        self.window = window
        self.animation = Animation(sprite_path, frames)
        self.animation.set_sequence_time(0, frames, gvar.FRAME_SPEED)
        self.animation.play()

        self.velocity = math.Vector2(0, 0)

        self.direction = {"left": False, "right": True}
        self.state = {"idle": True, "running": False}
        self.colliding = {"left": False,
                          "right": False, "up": False, "down": False}

        self.life = 100
        self.strenght = 50

    def update(self):
        self.animation.x += self.velocity.x * self.window.delta_time()
        self.animation.y += self.velocity.y * self.window.delta_time()

    def render(self):
        self.animation.update()
        self.animation.draw()

    def move(self, vector):
        self.velocity = vector

    def distance_to(self, object):
        return (((self.animation.x + self.animation.width/2 - (object.animation.x + object.animation.width/2))**2 + (self.animation.y + self.animation.height/2 - (object.animation.y + object.animation.height/2))**2)**1/2)

    def set_animation(self, sprite_path, frames):
        self.animation.image, self.animation.rect = load_image(
            sprite_path, alpha=True)
        self.animation.total_frames = frames
        self.animation.set_total_duration(frames * gvar.FRAME_SPEED)

    def set_position(self, x, y):
        self.animation.set_position(x, y)

    def set_direction(self, direction):
        for key, _ in self.direction.items():
            if key == direction:
                self.direction[key] = True
            else:
                self.direction[key] = False

    def set_state(self, state):
        for key, _ in self.state.items():
            if key == state:
                self.state[key] = True
            else:
                self.state[key] = False

    def set_colliding(self, bool, direction):
        self.colliding[direction] = bool

    def shoot(self, bullet_path, bullet_frames, bullet_vel):
        bullet = Entity(
            self.window, bullet_path, bullet_frames)
        bullet.set_position(self.animation.x + self.animation.width/2,
                            self.animation.y + self.animation.height/2)
        bullet.velocity = bullet_vel
        return bullet
