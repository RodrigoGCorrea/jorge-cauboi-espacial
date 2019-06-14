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
    # DEFAULT
    player.set_state("idle")
    vel_vector = [0, 0]

    # CHECKING COLLISION
    if player.animation.x <= 1:
        player.set_colliding(True, "left")
        player.set_position(player.animation.x + 1, player.animation.y)
    elif player.animation.x + player.animation.width >= window.width:
        player.set_colliding(True, "right")
        player.set_position(player.animation.x - 1, player.animation.y)

    if player.animation.y + (player.animation.height / 2) <= 96:
        player.set_colliding(True, "up")
        player.set_position(player.animation.x, player.animation.y + 1)
    elif player.animation.y + player.animation.height >= window.height:
        player.set_colliding(True, "down")
        player.set_position(player.animation.x, player.animation.y - 1)

    # RESET COLLISION
    if (
        player.colliding["left"] == True
        and keyboard.key_pressed("right")
    ):
        player.colliding["left"] = False
    if (
        player.colliding["right"] == True
        and keyboard.key_pressed("left")
    ):
        player.colliding["right"] = False
    if (
        player.colliding["up"] == True
        and keyboard.key_pressed("down")
    ):
        player.colliding["up"] = False
    if (
        player.colliding["down"] == True
        and keyboard.key_pressed("up")
    ):
        player.colliding["down"] = False
    # MOVING
    if (
        keyboard.key_pressed("right") == True
        and keyboard.key_pressed("left") == False
        and player.colliding["right"] == False
    ):
        vel_vector[0] = gvar.VELOCITY_PLAYER
        player.set_direction("right")
        player.set_state("running")
    elif (
        keyboard.key_pressed("left") == True
        and keyboard.key_pressed("right") == False
        and player.colliding["left"] == False
    ):
        vel_vector[0] = -gvar.VELOCITY_PLAYER
        player.set_direction("left")
        player.set_state("running")

    if (
        keyboard.key_pressed("up") == True
        and keyboard.key_pressed("down") == False
        and player.colliding["up"] == False
    ):
        vel_vector[1] = -gvar.VELOCITY_PLAYER
        player.set_state("running")
    elif (
        keyboard.key_pressed("down") == True
        and keyboard.key_pressed("up") == False
        and player.colliding["down"] == False
    ):
        vel_vector[1] = gvar.VELOCITY_PLAYER
        player.set_state("running")

    # ANIMATION

    if player.state["idle"]:
        if player.direction["right"]:
            player.set_animation("./src/assets/actors/jorge/idle_right.png", 8)
        elif player.direction["left"]:
            player.set_animation("./src/assets/actors/jorge/idle_left.png", 8)
    elif player.state["running"]:
        if player.direction["right"]:
            player.set_animation(
                "./src/assets/actors/jorge/running_right.png", 8)
        elif player.direction["left"]:
            player.set_animation(
                "./src/assets/actors/jorge/running_left.png", 8)

    else:
        if player.direction["right"]:
            player.set_animation("./src/assets/actors/jorge/idle_right.png", 8)
        elif player.direction["left"]:
            player.set_animation("./src/assets/actors/jorge/idle_left.png", 8)

    print(
        window.delta_time(),
        player.state,
        player.direction,
        player.velocity,
        player.colliding,
    )
    vel_vector = math.Vector2(vel_vector[0], vel_vector[1])
    player.move(vel_vector)
    player.update()
    player.render()
