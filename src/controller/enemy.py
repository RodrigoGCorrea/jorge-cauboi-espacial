from random import randint
from pygame import math

from environment import variables as gvar
from environment.instances import window
from classes.entity import Entity

from .player import player

enemy_mtx = []
enemy_type = 0

wave = 0


def reset():
    global enemy_mtx
    global wave
    global enemy_type

    enemy_mtx = []
    wave = 0
    enemy_type = 0


def run():
    global enemy_mtx
    global wave
    global enemy_type

    # SPAWN
    if len(enemy_mtx) == 0:
        level = randint(1, 3)
        enemy_type = randint(1, 5)
        level_constructor = open("./src/assets/levels/level" + str(level) + ".txt", "r")
        line = level_constructor.readline()
        lin = 0
        while lin < 17:
            for col in range(len(line)):
                if line[col] == "1":
                    enemy = Entity(
                        window,
                        "./src/assets/actors/enemies/minion{}/running_right.png".format(
                            enemy_type
                        ),
                        8,
                    )
                    enemy.set_position(
                        col * (gvar.WIDTH / 22)
                        + (gvar.WIDTH / 22) / 2
                        - enemy.animation.width / 2,
                        lin * (gvar.HEIGHT / 17)
                        + (gvar.HEIGHT / 17) / 2
                        - enemy.animation.height,
                    )
                    enemy.strenght = gvar.ENEMY_DAMAGE + wave
                    enemy_mtx.append(enemy)
            line = level_constructor.readline()
            lin += 1
        wave += 1

    # MOVEMENT
    for enemy in enemy_mtx:
        print(enemy.strenght)
        enemy_direction = math.Vector2(
            player.animation.x - enemy.animation.x,
            player.animation.y - enemy.animation.y,
        )
        enemy_direction.normalize_ip()
        enemy_direction *= gvar.ENEMY_VELOCITY + wave
        enemy.move(enemy_direction)

    # COLISSION
    for enemy1 in range(len(enemy_mtx)):
        for enemy2 in range(enemy1 + 1, len(enemy_mtx)):
            if enemy_mtx[enemy1].animation.collided(enemy_mtx[enemy2].animation):
                if enemy_mtx[enemy1].distance_to(player) < enemy_mtx[
                    enemy2
                ].distance_to(player):
                    new_vel_length = enemy_mtx[enemy2].velocity.length() - 30
                    enemy_mtx[enemy2].velocity.normalize_ip()
                    enemy_mtx[enemy2].velocity *= new_vel_length
                    enemy_mtx[enemy2].move(enemy_mtx[enemy2].velocity)
                else:
                    new_vel_length = enemy_mtx[enemy1].velocity.length() - 30
                    enemy_mtx[enemy1].velocity.normalize_ip()
                    enemy_mtx[enemy1].velocity *= new_vel_length
                    enemy_mtx[enemy1].move(enemy_mtx[enemy1].velocity)

    # DRAW
    for enemy in enemy_mtx:
        enemy.update()
        enemy.render()
