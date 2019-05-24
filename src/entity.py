from pygame.transform import flip
import math
from library.PPlay.animation import Animation
from library.PPlay.gameimage import load_image
from library.PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()

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
        self.set_behavior(level, dt)

        if self.state["idle"]:
            self.dx = 0
            self.dy = 0
            self.y0 = self.animation.y
            self.set_position(self.animation.x, math.floor(self.animation.y))

        elif self.state["walking"]:
            self.y0 = self.animation.y
            if self.direction["left"]:
                if self.animation.x < level.boundary[0]:
                    level.move(globals.X_VELOCITY_PLAYER * dt)
                    self.dx = 0
                else:
                    if self.colliding["left"] == True:
                        self.dx = 0
                    else:
                        self.dx = -globals.X_VELOCITY_PLAYER

            elif self.direction["right"]:
                if self.animation.x > level.boundary[1]:
                    level.move(-globals.X_VELOCITY_PLAYER * dt)
                    self.dx = 0
                else:
                    if self.colliding["right"] == True:
                        self.dx = 0
                    else:
                        self.dx = globals.X_VELOCITY_PLAYER

        elif self.state["jumping"]:
            self.dy = globals.Y_VELOCITY_PLAYER
            self.jump(self.dy, dt)

        if self.colliding["bottom"] == False and self.state["jumping"] == False:
            self.falling(dt)
        self.walk(self.dx * dt)
        print(self.colliding["left"], self.colliding["right"], self.animation.x, self.animation.y, self.get_direction(), self.colliding_tuple, dt)

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
                    self.y_time = 0
                    self.set_state("idle")
                    break
        
        #self.collided_side(level)
        self.set_fall(level)
        

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
        colliding_number = 0
        for obstacle in level.obstacles:
            if self.animation.collided(obstacle):
                self.colliding_initial = obstacle
                if self.colliding["left"] == False and self.colliding["right"] == False:
                    self.animation.set_position(self.animation.x, math.floor(self.animation.y) - 1)
                self.colliding["bottom"] = True
                self.y_time = 0
                colliding_number += 1
        
        error = 0
        if colliding_number == 2:
            error = level.obstacles[0].width

        left_limit = self.colliding_initial.x
        right_limit = self.colliding_initial.x + self.colliding_initial.width
        for obstacle in level.obstacles:
            if self.colliding_initial.collided(obstacle):
                if obstacle.x < left_limit:
                    left_limit = obstacle.x - error
                if obstacle.x > right_limit:
                    right_limit = obstacle.x + error + level.obstacles[0].width
        
        self.colliding_tuple = (left_limit, right_limit)

        if self.colliding["bottom"] == True:
            if self.colliding_tuple[0] >= self.animation.x or self.animation.x >= self.colliding_tuple[1]:
                self.colliding["bottom"] = False

    ''' def collided_side(self, level):
        collide_object = None
        for obstacle in level.obstacles:
            if collide_object == None:
                if obstacle.collided(self.animation):
                    collide_object = obstacle
            else:
                if obstacle.collided(self.animation) and obstacle.y > collide_object.y:
                    collide_object = obstacle
        if collide_object == None:
            self.colliding["left"] = False
            self.colliding["right"] = False
        else:
            if collide_object.y > self.animation.y + self.animation.height - 10:
                if collide_object.x < self.animation.x:
                    self.colliding["left"] = True
                if collide_object.x > self.animation.x:
                    self.colliding["right"] = True
            else:
                self.colliding["left"] = False
                self.colliding["right"] = False 
'''
