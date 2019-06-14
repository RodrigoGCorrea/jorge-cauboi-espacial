from random import randint

from environment import variables as gvar
from environment.instances import window
from classes.entity import Entity

enemy_mtx = []


def run():
    global enemy_mtx

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
                    enemy_mtx.append(enemy)
            line = level_constructor.readline()
            lin += 1

    # DRAW
    for enemy in enemy_mtx:
        enemy.render()
