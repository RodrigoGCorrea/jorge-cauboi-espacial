from environment import config
from environment.instances import window, keyboard, store

from screen import menu, play, powerup, gameover, rank

if __name__ == "__main__":
    while store.get("game_started"):
        # MENU SCREEN
        if store.get("state") == 0:
            menu.run()

        # PLAY SCREEN
        elif store.get("state") == 1:
            play.run()

        # POWER UP SCREEN
        elif store.get("state") == 2:
            powerup.run()

        # GAME OVER SCREEN
        elif store.get("state") == 3:
            if gameover.run():
                play.reset()
                store.dispatch("state", value=0)
                window.delay(150)

        # RANK SCREEN
        elif store.get("state") == 4:
            rank.run()

        window.update()
        window.clock.tick(60)
        # print(store.store)
        # print(window.clock.get_fps())
