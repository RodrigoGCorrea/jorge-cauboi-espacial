from library.PPlay.window import Window
from library.PPlay.sprite import Sprite
from library.PPlay.keyboard import Keyboard
from level import Level
from player import Player
from menu import Menu
from camera import Camera
from events import Events
import globals

class Game(object):
    def __init__(self):
        self.window = Window(globals.WIDTH, globals.HEIGHT)
        self.window.set_title("JSC")

        self.level = Level(self.window, "./src/levels/level.txt")
        self.jorge = Player(self.window, "./src/assets/jorge_idle.png", 8)
        self.background = Sprite("./src/assets/space.png")
        self.menu = Menu(self.window)
        self.camera = Camera(self.window)
        self.events = Events(self.jorge)

    def update(self):
        self.events.update(self.level, self.camera)
        self.level.update()
        self.camera.update(self.jorge, self.level)

    def render(self):
        self.background.draw()
        self.level.render()
        self.jorge.render()

if __name__ == "__main__":
    game = Game()
    while globals.GAME_STARTED:
        if globals.STATE == 0:
            game.menu.run()
        if globals.STATE == 1:
            game.update()
            game.render()
        game.window.update()
        game.window.clock.tick(120)
