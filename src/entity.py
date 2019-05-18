from pygame.transform import flip
import math
from library.PPlay.animation import Animation 
from library.PPlay.gameimage import load_image
from library.PPlay.keyboard import Keyboard
import globals

class Entity(object):
    def __init__(self, sprite_path, frames):
        self.animation = Animation(sprite_path, frames)
        self.animation.set_position(globals.WIDTH/2 - self.animation.width/2, globals.HEIGHT - self.animation.height - 20)
        self.animation.set_total_duration(frames * globals.FRAME_SPEED)
        self.animation.play()

        self.set_position = self.animation.set_position

        self.direction = {
            "right": True,
            "left": False
        }
        self.state = {
            "idle": True,
            "walking": False,
            "jumping": False,
            "colliding": False
        }

        self.dx = 0
        self.dy = 0
        self.y0 = self.animation.y
        self.y_time = 0

        self.strg = 1 
        self.dex = 1
        self.life = 20
        self.lvl = 1

    def update(self, dt, level):
        self.set_behavior(level)

        if self.state["idle"] or self.state["colliding"]:
            self.dx = 0
            self.dy = 0
            self.y_time = 0
            self.y0 = self.animation.y
            self.set_position(math.floor(self.animation.x), math.floor(self.animation.y))
        elif self.state["walking"]:
            if self.direction["left"]:
                self.dx = -globals.X_VELOCITY_PLAYER
            elif self.direction["right"]:
                self.dx = globals.X_VELOCITY_PLAYER
        elif self.state["jumping"]:
            self.dy = globals.Y_VELOCITY_PLAYER
            self.jump(self.dy, dt)

        self.walk(self.dx * dt)
        print(self.animation.x, self.animation.y, self.y_time, self.get_state(), self.get_direction())
    
    def render(self):
        if self.state["idle"]:
            self.set_animation("./src/assets/jorge_idle.png", 8)
        elif self.state["walking"]:
            self.set_animation("./src/assets/jorge_running.png", 8)
        elif self.state["jumping"]:
            self.set_animation("./src/assets/jorge_idle.png", 8)
        elif self.state["colliding"]:
            self.set_animation("./src/assets/jorge_idle.png", 8)

        if self.direction["left"]:
            self.animation.image = flip(self.animation.image, True, False)

        self.animation.update()
        self.animation.draw()

    def walk(self, dx):
        self.animation.x += dx

    def jump(self, dy, dt):
        self.y_time += globals.FALL_TIME * dt
        self.animation.y = self.y0 - dy * self.y_time - (globals.GRAVITY * (self.y_time)**2)/2
    
    def attack(self):
        pass
    
    def set_behavior(self, level):
        keyboard = Keyboard()

        # IDLE
        if self.state["idle"]:
            # MOVING LEFT
            if keyboard.key_pressed("left") and keyboard.key_pressed("right") == False:
                self.set_direction("left")
                self.set_state("walking")
            # MOVING RIGHT
            elif keyboard.key_pressed("right") and keyboard.key_pressed("left") == False:
                self.set_direction("right")
                self.set_state("walking")
            # JUMPING
            elif keyboard.key_pressed("up"):
                self.set_state("jumping")

        # MOVING
        elif self.state["walking"]:
            # KEPT MOVING
            if (keyboard.key_pressed("left") and keyboard.key_pressed("right") == False or 
                keyboard.key_pressed("right") and keyboard.key_pressed("left") == False):

                # JUMPING
                if keyboard.key_pressed("up"):
                    self.set_state("jumping")

                # CHECK COLLISION
                for obstacle in level.obstacles:
                    if self.animation.collided(obstacle):
                        if self.direction["left"]:
                            self.set_position(obstacle.x + obstacle.width + 1, self.animation.y)
                        elif self.direction["right"]:
                            self.set_position(obstacle.x - self.animation.width - 1, self.animation.y)
                        self.set_state("colliding")
                        break

            # STOPPED MOVING
            else:
                self.set_state("idle")

        # JUMPING
        elif self.state["jumping"]:
            for obstacle in level.obstacles:
                if self.animation.collided(obstacle):
                    self.set_position(self.animation.x, obstacle.y - self.animation.height - 1)
                    self.set_state("idle")
                    break

        # COLLIDING
        elif self.state["colliding"]:
            if self.direction["left"] and keyboard.key_pressed("right"):
                self.set_state("walking")
                self.set_direction("right")
            elif self.direction["right"] and keyboard.key_pressed("left"):
                self.set_state("walking")
                self.set_direction("left")

    def set_state(self, state):
        for key, _ in self.state.items():
            if key == state:
                self.state[key] = True
            else:
                self.state[key] = False

    def set_direction(self, direction):
        for key, _ in self.direction.items():
            if key == direction:
                self.direction[key] = True
            else:
                self.direction[key] = False

    def set_animation(self, sprite_path, frames):
        self.animation.image, self.animation.rect = load_image(sprite_path, alpha=True)
        self.animation.total_frames = frames
        self.animation.set_total_duration(frames * globals.FRAME_SPEED)

    def get_state(self):
        for key, value in self.state.items():
            if value:
                return key

    def get_direction(self):
        for key, value in self.direction.items():
            if value:
                return key