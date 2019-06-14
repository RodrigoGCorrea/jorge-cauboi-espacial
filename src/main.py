from library.PPlay.sprite import Sprite

from window import window
from menu import Menu

import player
import globals

background = Sprite("./src/assets/tileset/background.png")
menu = Menu(window)

if __name__ == "__main__":
    while globals.GAME_STARTED:
        if globals.STATE == 0:
            menu.run()
        if globals.STATE == 1:
            background.draw()
            player.run()

        window.update()
        window.clock.tick(60)
