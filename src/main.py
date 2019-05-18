from library.PPlay.window import Window
from library.PPlay.sprite import Sprite
from level import Level
from entity import Entity
import globals

class Game(object):
    def __init__(self):
        self.window = Window(globals.WIDTH, globals.HEIGHT)
        self.window.set_title("JSC")

        self.level = Level(self.window, "./src/levels/level.txt")
        self.jorge = Entity("./src/assets/jorge_idle.png", 8)
        self.background = Sprite("./src/assets/space.png")

    def events(self):
        pass

    def update(self):
        self.jorge.update(self.window.delta_time(), self.level)
        self.level.update()

    def render(self):
        self.background.draw()
        self.jorge.render()
        self.level.render()

if __name__ == "__main__":
    game = Game()
    while globals.GAME_STARTED:
        game.events()
        game.update()
        game.render()
        game.window.update()
