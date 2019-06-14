from environment import variables as gvar
from environment.instances import keyboard

from controller import menu


def run():
    if keyboard.key_pressed("esc"):
        gvar.GAME_STARTED = False

    menu.run()
