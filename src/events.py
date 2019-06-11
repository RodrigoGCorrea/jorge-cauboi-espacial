from player import Player
from enemy import Enemy
from library.PPlay.keyboard import Keyboard

import globals

keyboard = Keyboard()


class Events(object):
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def update(self, level, camera):
        self.control_events()
        self.player_events(camera)
        self.player.update(level)

    def player_events(self, camera):
        # movement
        if (
            keyboard.key_pressed("left")
            and keyboard.key_pressed("right") == False
            and self.player.colliding["left"] == False
            and camera.cam_velocity == 0
        ):
            self.player.velocity["x"] = -globals.X_VELOCITY_PLAYER
        elif (
            keyboard.key_pressed("right")
            and keyboard.key_pressed("left") == False
            and self.player.colliding["right"] == False
            and camera.cam_velocity == 0
        ):
            self.player.velocity["x"] = globals.X_VELOCITY_PLAYER
        else:
            self.player.velocity["x"] = 0

        # jump
        if self.player.colliding["bottom"] == True and self.player.jumping == False:
            if keyboard.key_pressed("up"):
                self.player.jumping = True
                self.player.colliding["bottom"] = False

        # direction
        if keyboard.key_pressed("left"):
            self.player.direction["left"] = True
            self.player.direction["right"] = False
        elif keyboard.key_pressed("right"):
            self.player.direction["right"] = True
            self.player.direction["left"] = False

    def control_events(self):
        if keyboard.key_pressed("esc"):
            globals.GAME_STARTED = False

    def enemy_events(self):
        # direction
        if self.player.x + self.player.width/2 < self.enemy.x:
            self.player.direction["left"] = True
            self.player.direction["right"] = False
        else:
            self.player.direction["left"] = False
            self.player.direction["right"] = True
        # movement
        # jump
