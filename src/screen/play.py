from library.PPlay.sprite import Sprite

from environment import variables as gvar
from environment.instances import keyboard, window, store

from controller import player, enemy, bullet, atributes
from screen import hud

background = Sprite("./src/assets/tileset/background.png")


def run():
    # MENU
    if keyboard.key_pressed("esc"):
        gvar.STATE = 0
        window.delay(150)

    # POWER UP
    if keyboard.key_pressed("p"):
        gvar.STATE = 2
        window.delay(150)

    # GAME OVER
    if store.get("player").life <= 0:
        gvar.STATE = 3
        window.delay(150)

    # CHANGE LEVEL
    if keyboard.key_pressed("y"):
        store.dispatch("enemy_mtx", value=[])

    # DIE
    if keyboard.key_pressed("u"):
        store.get("player").life = -1

    # SCORE
    if keyboard.key_pressed("t"):
        store.dispatch("score", lambda score: score + 200)

    background.draw()
    player.run()
    enemy.run()
    bullet.run()
    hud.run()


def reset():
    player.reset()
    enemy.reset()
    bullet.reset()
    atributes.reset()
