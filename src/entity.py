from pygame.transform import flip
import math
from library.PPlay.animation import Animation
from library.PPlay.gameimage import load_image
from library.PPlay.keyboard import Keyboard
import globals

class Entity(object):
    def __init__(self, sprite_path, frames, level):
        self.animation = Animation(sprite_path, frames)
        self.animation.set_position(
            globals.WIDTH/2 - self.animation.width/2,
            520
        )
        self.animation.set_total_duration(frames * globals.FRAME_SPEED)
        self.animation.play()

        self.set_position = self.animation.set_position

        self.direction = {
            "right": True,
            "left": False,
        }
        self.state = {
            "idle": True,
            "walking": False,
            "jumping": False,
        }
        self.colliding = {
            "left": False,
            "right": False,
            "top": False,
            "bottom": False,
        }

        self.dx = 0
        self.dy = 0
        self.y0 = self.animation.y
        self.y_time = 0

        self.strg = 1
        self.dex = 1
        self.life = 20
        self.lvl = 1

        self.colliding_tuple = (0, globals.WIDTH)
        self.colliding_initial = level.obstacles[0]

    def update(self, dt, level):
        if self.state["idle"]:
            self.dx = 0
            self.dy = 0
            self.y_time = 0
            self.y0 = self.animation.y
            self.set_position(self.animation.x, math.floor(self.animation.y))

        elif self.state["walking"]:
            self.y0 = self.animation.y
            if self.direction["left"]:
                if self.animation.x < level.boundary[0]:
                    level.move(globals.X_VELOCITY_PLAYER * dt)
                    self.dx = 0
                else:
                    self.dx = -globals.X_VELOCITY_PLAYER

            elif self.direction["right"]:
                if self.animation.x > level.boundary[1]:
                    level.move(-globals.X_VELOCITY_PLAYER * dt)
                    self.dx = 0
                else:
                    self.dx = globals.X_VELOCITY_PLAYER

        elif self.state["jumping"]:
            self.dy = globals.Y_VELOCITY_PLAYER
            self.jump(self.dy, dt)

        if self.colliding["bottom"] == False and self.state["jumping"] == False:
            self.falling(dt)
        self.walk(self.dx * dt)
        self.set_behavior(level, dt)
        print(self.colliding["bottom"], self.animation.x, self.animation.y, self.get_direction(), self.colliding_tuple, dt)

    def render(self):
        if self.state["idle"]:
            self.set_animation("./src/assets/jorge_idle.png", 8)
        elif self.state["walking"]:
            self.set_animation("./src/assets/jorge_running.png", 8)
        elif self.state["jumping"]:
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

    def falling(self, dt):
        self.y_time += globals.FALL_TIME * dt
        self.animation.y = self.y0 - (globals.GRAVITY * (self.y_time)**2)/2

    def attack(self):
        pass

    def set_behavior(self, level, dt):
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
            #FALLING
            self.set_fall(level)

        # MOVING
        elif self.state["walking"]:
            # KEPT MOVING
            if (keyboard.key_pressed("left") and keyboard.key_pressed("right") == False or
                keyboard.key_pressed("right") and keyboard.key_pressed("left") == False):

                # JUMPING
                if keyboard.key_pressed("up"):
                    self.set_state("jumping")

            # STOPPED MOVING
            else:
                self.set_state("idle")
            
            #FALLING
            self.set_fall(level)

        # JUMPING
        elif self.state["jumping"]:
            # STRAFE LEFT
            if keyboard.key_pressed("left") and keyboard.key_pressed("right") == False:
                if self.animation.x < level.boundary[0]:
                    level.move(globals.X_VELOCITY_PLAYER * dt)
                    self.dx = 0
                else:
                    self.dx = -globals.X_VELOCITY_PLAYER
                self.set_direction("left")
            #STRAFE RIGHT
            elif keyboard.key_pressed("right") and keyboard.key_pressed("left") == False:
                if self.animation.x > level.boundary[1]:
                    level.move(-globals.X_VELOCITY_PLAYER * dt)
                    self.dx = 0
                else:
                    self.dx = globals.X_VELOCITY_PLAYER
                self.set_direction("right")

            # CHECKING COLLIDING
            for obstacle in level.obstacles:
                if self.animation.collided(obstacle):
                    self.set_position(self.animation.x, obstacle.y - self.animation.height - 0.5)
                    self.set_state("idle")
                    break

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

    def set_fall(self, level):
        for obstacle in level.obstacles:
            if self.animation.collided(obstacle):
                self.colliding_initial = obstacle
                self.animation.set_position(self.animation.x, math.floor(self.animation.y) - 1)
                self.colliding["bottom"] = True
                break

        left_limit = globals.WIDTH
        right_limit = 0
        for obstacle in level.obstacles:
            if self.colliding_initial.collided(obstacle):
                if obstacle.x <= left_limit:
                    left_limit = obstacle.x
                if obstacle.x >= right_limit:
                    right_limit = obstacle.x + level.obstacles[0].width
        
        self.colliding_tuple = (left_limit, right_limit)

        if self.colliding["bottom"] == True:
            if self.colliding_tuple[0] >= self.animation.x or self.animation.x >= self.colliding_tuple[1]:
                self.colliding["bottom"] = False
