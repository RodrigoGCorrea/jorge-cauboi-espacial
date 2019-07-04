from environment import variables as gvar
from environment.instances import window, keyboard

from screen import menu, play, powerup, gameover

if __name__ == "__main__":
    while gvar.GAME_STARTED:
        # MENU SCREEN
        if gvar.STATE == 0:
            menu.run()

        # PLAY SCREEN
        elif gvar.STATE == 1:
            play.run()

        # POWER UP SCREEN
        elif gvar.STATE == 2:
            powerup.run()
        
        # GAME OVER SCREEN
        elif gvar.STATE == 3:
            gameover.run()
            play.reset()

        window.update()
        window.clock.tick(60)
