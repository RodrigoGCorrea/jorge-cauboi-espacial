from library.PPlay.sprite import Sprite
from library.PPlay.keyboard import Keyboard

from instances import window, keyboard
from menu import Menu

import player
import globals

background = Sprite("./src/assets/tileset/background.png")
menu = Menu(window)

if __name__ == "__main__":
    while globals.GAME_STARTED:
        if globals.STATE == 0:
            if keyboard.key_pressed("esc"):
                globals.GAME_STARTED = False

            menu.run()

        if globals.STATE == 1:
            if keyboard.key_pressed("esc"):
                globals.STATE = 0
                window.delay(150)

            background.draw()
            player.run()

        window.update()
        window.clock.tick(60)
