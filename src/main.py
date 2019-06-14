from library.PPlay.sprite import Sprite
from library.PPlay.keyboard import Keyboard

from environment import variables as gvar
from environment.instances import window, keyboard

from controller import player
from controller.menu import Menu

background = Sprite("./src/assets/tileset/background.png")
menu = Menu(window)

if __name__ == "__main__":
    while gvar.GAME_STARTED:
        if gvar.STATE == 0:
            if keyboard.key_pressed("esc"):
                gvar.GAME_STARTED = False

            menu.run()

        if gvar.STATE == 1:
            if keyboard.key_pressed("esc"):
                gvar.STATE = 0
                window.delay(150)

            background.draw()
            player.run()

        window.update()
        window.clock.tick(60)
