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
        self.is_over_object = False
        self.gravity = globals.GRAVITY
        
        
    def update(self, level, ):
        self.clear_variables()
        self.fall()
        self.walk()
        self.jump()
        self.collision_y(level)
        self.collision_x(level)

    def render(self):
        self.animation.draw()
    
    def walk(self):
        #set velocity
        if keyboard.key_pressed("left") and keyboard.key_pressed("right") == False and self.colliding["left"] == False:
            self.velocity["x"] = -globals.X_VELOCITY_PLAYER
        elif keyboard.key_pressed("right") and keyboard.key_pressed("left") == False and self.colliding["right"] == False:
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
            self.animation.y += (self.gravity * self.time**2)/2 - self.velocity["y"] 

  
    def fall(self):
        if self.colliding["bottom"] == False:
            self.clock()
            if self.is_over_object == False and self.jumping == False:
                self.gravity = 5 * globals.GRAVITY
                self.animation.y += (self.gravity * self.time**2)/2
            self.gravity = globals.GRAVITY


    def collision_x(self, level):
        for obstacle in level.obstacles:
            if self.animation.collided(obstacle) and self.animation.x < obstacle.x + obstacle.width and keyboard.key_pressed("left"):
                self.colliding["left"] = True
                self.animation.set_position(obstacle.x + obstacle.width, self.animation.y)
                break
            elif self.animation.collided(obstacle) and self.animation.x + self.animation.width > obstacle.x and keyboard.key_pressed("right"):
                self.colliding["right"] = True
                self.animation.set_position(obstacle.x - self.animation.width, self.animation.y)
                break
                
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

        if self.colliding["bottom"] == True and (keyboard.key_pressed("left") or keyboard.key_pressed("right")) and self.jumping == False:
            self.is_over_object = False
            for obstacle in level.obstacles:
                if self.animation.y == obstacle.y - self.animation.height:
                    if obstacle.x < self.animation.x < obstacle.x + obstacle.width or obstacle.x < self.animation.x + self.animation.width < obstacle.x + obstacle.width:
                        self.is_over_object = True
                        break
            if self.is_over_object == False:
                self.colliding["bottom"] = False

                    

    def clear_variables(self):
        if self.colliding["bottom"] == True and self.jumping == False:
            self.time = 0
            self.velocity["y"] = 0
            self.gravity = globals.GRAVITY
