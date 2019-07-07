from pygame import math

from classes.entity import Entity

from environment import config 
from environment.instances import window, keyboard, store

player = Entity(window, "./src/assets/actors/jorge/idle_right.png", 8)
player.set_position(10, window.height / 2)

vel_vector = math.Vector2(0, 0)

store.dispatch("player", value=player)


def reset():
    global vel_vector

    player.__init__(window, "./src/assets/actors/jorge/idle_right.png", 8)
    player.set_position(10, window.height / 2)
    vel_vector = math.Vector2(0, 0)

    store.dispatch("player", value=player)


def run():
    global vel_vector

    # DEFAULT
    player.set_state("idle")
    vel_vector.update(0, 0)

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
    if player.colliding["left"] == True and keyboard.key_pressed("d"):
        player.colliding["left"] = False
    if player.colliding["right"] == True and keyboard.key_pressed("a"):
        player.colliding["right"] = False
    if player.colliding["up"] == True and keyboard.key_pressed("s"):
        player.colliding["up"] = False
    if player.colliding["down"] == True and keyboard.key_pressed("w"):
        player.colliding["down"] = False

    # MOVING
    if (
        keyboard.key_pressed("d") == True
        and keyboard.key_pressed("a") == False
        and player.colliding["right"] == False
    ):
        vel_vector.x = 1
        player.set_direction("right")
        player.set_state("running")
    elif (
        keyboard.key_pressed("a") == True
        and keyboard.key_pressed("d") == False
        and player.colliding["left"] == False
    ):
        vel_vector.x = -1
        player.set_direction("left")
        player.set_state("running")

    if (
        keyboard.key_pressed("w") == True
        and keyboard.key_pressed("s") == False
        and player.colliding["up"] == False
    ):
        vel_vector.y = -1
        player.set_state("running")
    elif (
        keyboard.key_pressed("s") == True
        and keyboard.key_pressed("w") == False
        and player.colliding["down"] == False
    ):
        vel_vector.y = 1
        player.set_state("running")

    # COLLISION WITH ENEMY
    for enemy in store.get("enemy_mtx"):
        if player.collide(enemy) and player.staggered == False:
            player.damage(enemy.strenght)
            player.staggered = True

    # RESET COLLISION WITH ENEMY
    if player.staggered:
        player.damage_cooldown -= window.delta_time() * 1000
        if player.damage_cooldown <= 0:
            player.damage_cooldown = config.DAMAGE_COOLDOWN
            player.staggered = False

    # ANIMATION
    if player.staggered:
        if player.state["idle"]:
            if player.direction["right"]:
                player.set_animation(
                    "./src/assets/actors/jorge/idle_right_staggered.png", 8
                )
            elif player.direction["left"]:
                player.set_animation(
                    "./src/assets/actors/jorge/idle_left_staggered.png", 8
                )
        elif player.state["running"]:
            if player.direction["right"]:
                player.set_animation(
                    "./src/assets/actors/jorge/running_right_staggered.png", 8
                )
            elif player.direction["left"]:
                player.set_animation(
                    "./src/assets/actors/jorge/running_left_staggered.png", 8
                )
        else:
            if player.direction["right"]:
                player.set_animation(
                    "./src/assets/actors/jorge/idle_right_staggered.png", 8
                )
            elif player.direction["left"]:
                player.set_animation(
                    "./src/assets/actors/jorge/idle_left_staggered.png", 8
                )

    else:
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
        else:
            if player.direction["right"]:
                player.set_animation("./src/assets/actors/jorge/idle_right.png", 8)
            elif player.direction["left"]:
                player.set_animation("./src/assets/actors/jorge/idle_left.png", 8)

    if vel_vector != math.Vector2(0):
        vel_vector.normalize_ip()
    vel_vector *= config.VELOCITY_PLAYER

    player.move(vel_vector)
    player.update()
    player.render()

    store.dispatch("player", value=player)
