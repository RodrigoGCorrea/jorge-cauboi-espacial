from library.PPlay.sprite import Sprite

class LevelControl(object):
    def __init__(self, window, level_mtx):
        self.level_mtx = level_mtx
        self.window = window
        self.__draw()

    def update(self):
        self.__draw()
    
    def __draw(self):
        for col in range(len(self.level_mtx)):
            for lin in range(len(self.level_mtx[0])):
                if self.level_mtx[col][lin] == 1:
                    tile = Sprite("./src/assets/floor.png")
                    tile.set_position(lin * tile.width, col * tile.height)
                    tile.draw()
       