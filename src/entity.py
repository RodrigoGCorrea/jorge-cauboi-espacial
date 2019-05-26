from library.PPlay.animation import Animation
from library.PPlay.keyboard import Keyboard
from pygame.transform import flip
import globals

keyboard = Keyboard()

class Entity(object):
    def __init__(self, window):
        self.window = window
        self.animation = Animation("./src/assets/jorge_idle.png", 8)
        self.animation.set_position(globals.WIDTH/2, 400)

        self.colliding = {
            "left": False,
            "right": False,
            "top": False,
            "bottom": False,
        }
        
        self.velocity = {
            "x": 0,
            "y": 0
        }
        self.time = 0
        self.jumping = False
        
        
    def update(self, level, ):
        self.clear_variables()
        self.fall()
        self.walk()
        self.collision_y(level)
        self.jump()

    def render(self):
        self.animation.draw()
    
    def walk(self):
        #set velocity
        if keyboard.key_pressed("left") and keyboard.key_pressed("right") == False:
            self.velocity["x"] = -globals.X_VELOCITY_PLAYER
        elif keyboard.key_pressed("right") and keyboard.key_pressed("left") == False:
            self.velocity["x"] = globals.X_VELOCITY_PLAYER
        else:
            self.velocity["x"] = 0
        
        if self.colliding["left"] == False and self.colliding["right"] == False:
            self.animation.x += self.velocity["x"] * self.window.delta_time()

    def clock(self):
        self.time += self.window.delta_time()
    
    def jump(self):
        if self.colliding["bottom"] == True:
            if keyboard.key_pressed("up"):
                self.jumping = True
                self.colliding["bottom"] = False
        if self.jumping:
            self.clock()
            self.velocity["y"] = 3 + globals.Y_VELOCITY_PLAYER * self.time
            self.animation.y += (globals.GRAVITY * self.time**2)/2 - self.velocity["y"] 

  
    def fall(self):
        if self.colliding["bottom"] == False:
            self.clock()
            self.animation.y += (globals.GRAVITY * self.time**2)/2


    def collision_x(self, level):
        if self.colliding["left"] == True and keyboard.key_pressed("right"):
            self.colliding["left"] = False
        
        elif self.colliding["right"] == True and keyboard.key_pressed("left"):
            self.colliding["right"] = False
    
    def collision_y(self, level):
        if self.colliding["bottom"] == False:
            for obstacle in level.obstacles:
                if self.animation.collided(obstacle) and (self.animation.y + self.animation.height) > obstacle.y:
                    self.colliding["bottom"] = True
                    self.jumping = False
                    self.animation.set_position(self.animation.x, obstacle.y - self.animation.height)

    def clear_variables(self):
        if self.colliding["bottom"] == True and self.jumping == False:
            self.time = 0
            self.velocity["y"] = 0
