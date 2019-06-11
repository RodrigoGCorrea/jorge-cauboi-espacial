from library.PPlay.animation import Animation
from library.PPlay.keyboard import Keyboard
from library.PPlay.gameimage import load_image
import globals


class Entity(object):
    def __init__(self, window, animation_path, animation_frame):
        self.window = window
        self.animation = Animation(animation_path, animation_frame)
        self.animation.play()

        self.colliding = {"left": False, "right": False, "top": False, "bottom": False}

        self.velocity = {"x": 0, "y": 0}

        self.direction = {"left": False, "right": False}

        self.time = 0
        self.jumping = False
        self.is_over_object = False
        self.gravity = globals.GRAVITY

    def render(self):
        self.animation.update()
        self.animation.draw()

    def walk(self):
        if self.colliding["left"] == False and self.colliding["right"] == False:
            self.animation.x += self.velocity["x"] * self.window.delta_time()

    def clock(self):
        self.time += self.window.delta_time()

    def jump(self):
        if self.jumping:
            self.clock()
            self.velocity["y"] = 3 + globals.Y_VELOCITY_PLAYER * self.time
            self.animation.y += (self.gravity * self.time ** 2) / 2 - self.velocity["y"]

    def fall(self):
        if self.colliding["bottom"] == False:
            self.clock()
            if self.is_over_object == False and self.jumping == False:
                self.gravity = 5 * globals.GRAVITY
                self.animation.y += (self.gravity * self.time ** 2) / 2
            self.gravity = globals.GRAVITY

    def collision_x(self, level):
        for obstacle in level.obstacles:
            if (
                self.animation.collided(obstacle)
                and self.animation.x < obstacle.x + obstacle.width
                and self.direction["left"] == True
            ):
                self.colliding["left"] = True
                self.animation.set_position(
                    obstacle.x + obstacle.width, self.animation.y
                )
                break
            elif (
                self.animation.collided(obstacle)
                and self.animation.x + self.animation.width > obstacle.x
                and self.direction["right"] == True
            ):
                self.colliding["right"] = True
                self.animation.set_position(
                    obstacle.x - self.animation.width, self.animation.y
                )
                break

        if self.colliding["left"] == True and self.direction["right"]:
            self.colliding["left"] = False

        elif self.colliding["right"] == True and self.direction["left"]:
            self.colliding["right"] = False

    def collision_y(self, level):
        if self.colliding["bottom"] == False:
            for obstacle in level.obstacles:
                if (
                    self.animation.collided(obstacle)
                    and (self.animation.y + self.animation.height) > obstacle.y
                ):
                    self.colliding["bottom"] = True
                    self.jumping = False
                    self.animation.set_position(
                        self.animation.x, obstacle.y - self.animation.height
                    )

        if (
            self.colliding["bottom"] == True
            and (self.direction["left"] or self.direction["right"])
            and self.jumping == False
        ):
            self.is_over_object = False
            for obstacle in level.obstacles:
                if self.animation.y == obstacle.y - self.animation.height:
                    if (
                        obstacle.x < self.animation.x < obstacle.x + obstacle.width
                        or obstacle.x
                        < self.animation.x + self.animation.width
                        < obstacle.x + obstacle.width
                    ):
                        self.is_over_object = True
                        break
            if self.is_over_object == False:
                self.colliding["bottom"] = False

    def clear_variables(self):
        if self.colliding["bottom"] == True and self.jumping == False:
            self.time = 0
            self.velocity["y"] = 0
            self.gravity = globals.GRAVITY

    def set_animation(self, sprite_path, frames):
        self.animation.image, self.animation.rect = load_image(sprite_path, alpha=True)
        self.animation.total_frames = frames
        self.animation.set_total_duration(frames * globals.FRAME_SPEED)
