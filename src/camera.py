from library.PPlay.keyboard import Keyboard

import globals

keyboard = Keyboard()


class Camera(object):
    def __init__(self, window):
        self.window = window
        self.boundary = ((1 / 4) * self.window.width, (3 / 4) * self.window.width)
        self.cam_velocity = 0

    def update(self, jorge, level):
        self.move(jorge, level)

    def move(self, jorge, level):
        if jorge.animation.x < self.boundary[0] and keyboard.key_pressed("left"):
            self.cam_velocity = globals.X_VELOCITY_PLAYER * self.window.delta_time()
            jorge.velocity["x"] = 0
            globals.CAMERA_MOVING = True
        elif jorge.animation.x > self.boundary[1] and keyboard.key_pressed("right"):
            self.cam_velocity = -globals.X_VELOCITY_PLAYER * self.window.delta_time()
            jorge.velocity["x"] = 0
            globals.CAMERA_MOVING = True
        else:
            self.cam_velocity = 0
            globals.CAMERA_MOVING = False

        level.move(self.cam_velocity)
