from pygame.math import Vector2

from window import window
from entity import Entity
from library.PPlay.keyboard import Keyboard

import globals

keyboard = Keyboard()
player = Entity(window, "./src/assets/actors/jorge/idle_right.png", 8)
player.set_position(10, window.height / 2)

vel_stop = Vector2(0)
vel_right = Vector2(globals.VELOCITY_PLAYER, 0)
vel_left = Vector2(-globals.VELOCITY_PLAYER, 0)
vel_down = Vector2(0, globals.VELOCITY_PLAYER)
vel_up = Vector2(0, -globals.VELOCITY_PLAYER)


def run():
    if (
        keyboard.key_pressed("right") == False
        and keyboard.key_pressed("left") == False
        and keyboard.key_pressed("up") == False
        and keyboard.key_pressed("down") == False
    ):
        player.move(vel_stop)
        if player.direction["right"]:
            player.set_animation("./src/assets/actors/jorge/idle_right.png", 8)
        elif player.direction["left"]:
            player.set_animation("./src/assets/actors/jorge/idle_left.png", 8)

    if keyboard.key_pressed("right"):
        player.move(vel_right)
        player.set_animation("./src/assets/actors/jorge/running_right.png", 8)
        player.flip_direction()

    elif keyboard.key_pressed("left"):
        player.move(vel_left)
        player.set_animation("./src/assets/actors/jorge/running_left.png", 8)
        player.flip_direction()

    if keyboard.key_pressed("down"):
        player.move(vel_down)
        if player.direction["right"]:
            player.set_animation("./src/assets/actors/jorge/running_right.png", 8)
        elif player.direction["left"]:
            player.set_animation("./src/assets/actors/jorge/running_left.png", 8)
    elif keyboard.key_pressed("up"):
        player.move(vel_up)
        if player.direction["right"]:
            player.set_animation("./src/assets/actors/jorge/running_right.png", 8)
        elif player.direction["left"]:
            player.set_animation("./src/assets/actors/jorge/running_left.png", 8)

    player.update()
    player.render()
