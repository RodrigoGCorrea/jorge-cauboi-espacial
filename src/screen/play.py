from library.PPlay.sprite import Sprite

from environment import variables as gvar
from environment.instances import keyboard, window

from controller import player, enemy, bullet
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
    if player.player.life <= 0:
        gvar.STATE = 3
        window.delay(150)

    background.draw()
    player.run()
    enemy.run()
    bullet.run()
    hud.run()


def reset():
    player.reset()
    enemy.reset()
    bullet.reset()
