from environment import variables as gvar
from environment.instances import window, keyboard

from screen import menu, play

if __name__ == "__main__":
    while gvar.GAME_STARTED:
        # MENU SCREEN
        if gvar.STATE == 0:
            menu.run()

        # PLAY SCREEN
        if gvar.STATE == 1:
            play.run()

        window.update()
        window.clock.tick(60)
