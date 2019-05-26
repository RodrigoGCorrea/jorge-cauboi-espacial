from library.PPlay.window import Window
from library.PPlay.sprite import Sprite
from library.PPlay.keyboard import Keyboard
from level import Level
from entity import Entity
from menu import Menu
from camera import Camera
import globals

class Game(object):
    def __init__(self):
        self.window = Window(globals.WIDTH, globals.HEIGHT)
        self.window.set_title("JSC")

        self.level = Level(self.window, "./src/levels/level.txt")
        self.jorge = Entity(self.window)
        self.background = Sprite("./src/assets/space.png")
        self.menu = Menu(self.window)
        self.camera = Camera(self.window)

    def events(self):
        keyboard = Keyboard()

        if keyboard.key_pressed("esc"):
            globals.GAME_STARTED = False

    def update(self):
        self.level.update()
        self.jorge.update(self.level, self.camera)
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
            game.events()
            game.update()
            game.render()
        game.window.update()
        game.window.clock.tick(120)
