from library.PPlay.mouse import Mouse
from library.PPlay.sprite import Sprite

import globals

mouse = Mouse()

class Menu(object):
    def __init__(self, window):
        self.window = window
        self.play_button = Sprite("./src/assets/play.png")
        self.__set_pos()

    def run(self):
        self.window.set_background_color((0, 0, 0))
        self.__draw()
        self.start_game()
    
    def __draw(self):
        self.window.draw_text(
            "Jorge The Space Cowboy",
            globals.WIDTH/2, globals.HEIGHT/2 - 220,
            "./src/assets/pixel.ttf",
            40,
            (255, 255, 255)
        )
        self.play_button.draw()

    def start_game(self):
        if mouse.is_over_object(self.play_button) and mouse.is_button_pressed(1):
            globals.STATE = 1
    
    def __set_pos(self):
        self.play_button.set_position(
            globals.WIDTH/2 - self.play_button.width/2, 
            globals.HEIGHT/2 - self.play_button.height/2
            )
