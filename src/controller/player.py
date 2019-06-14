from pygame import math

from environment import variables as gvar
from environment.instances import window, keyboard
from classes.entity import Entity

player = Entity(window, "./src/assets/actors/jorge/idle_right.png", 8)
player.set_position(10, window.height / 2)

vel_stop = math.Vector2(0)
vel_right = math.Vector2(gvar.VELOCITY_PLAYER, 0)
vel_left = math.Vector2(-gvar.VELOCITY_PLAYER, 0)
vel_down = math.Vector2(0, gvar.VELOCITY_PLAYER)
vel_up = math.Vector2(0, -gvar.VELOCITY_PLAYER)


def run():
    player.move(vel_stop)
    player.set_state("idle")

    if keyboard.key_pressed("right") == True and keyboard.key_pressed("left") == False:
        player.move(vel_right)
        player.set_direction("right")
        player.set_state("running")
    elif (
        keyboard.key_pressed("left") == True and keyboard.key_pressed("right") == False
    ):
        player.move(vel_left)
        player.set_direction("left")
        player.set_state("running")

    if keyboard.key_pressed("up") == True and keyboard.key_pressed("down") == False:
        player.move(vel_up)
        player.set_state("running")
    elif keyboard.key_pressed("down") == True and keyboard.key_pressed("up") == False:
        player.move(vel_down)
        player.set_state("running")

    if player.state["idle"]:
        if player.direction["right"]:
            player.set_animation("./src/assets/actors/jorge/idle_right.png", 8)
        elif player.direction["left"]:
            player.set_animation("./src/assets/actors/jorge/idle_left.png", 8)
    elif player.state["running"]:
        if player.direction["right"]:
            player.set_animation("./src/assets/actors/jorge/running_right.png", 8)
        elif player.direction["left"]:
            player.set_animation("./src/assets/actors/jorge/running_left.png", 8)
    
    print(player.state, player.direction, player.velocity)

    player.update()
    player.render()
