from library.PPlay.sprite import Sprite

from environment import variables as gvar
from environment.instances import keyboard, window

from controller import player, enemy, bullet
from screen import hud

background = Sprite("./src/assets/tileset/background.png")


def run():
    if keyboard.key_pressed("esc"):
        gvar.STATE = 0
        window.delay(150)

    background.draw()
    player.run()
    enemy.run()
    bullet.run()
    hud.run()