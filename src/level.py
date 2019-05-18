from library.PPlay.sprite import Sprite

class Level(object):
    def __init__(self, window, level_path):
        self.obstacles = []
        self.window = window
        self.boundary = ((1/4) * self.window.width, (3/4) * self.window.width)
        self.__setup(level_path)

    def update(self):
        pass

    def render(self):
        for obstacles in self.obstacles:
            obstacles.draw()

    def move(self, x_velocity):
        for obstacle in self.obstacles:
            obstacle.x += x_velocity

    def __setup(self, level_path):
        level_constructor = open(level_path, "r")

        line = level_constructor.readline()
        lin = 0
        while lin <= 29:
            for col in range(len(line)):
                if line[col] == "1":
                    tile = Sprite("./src/assets/floor.png")
                    tile.set_position(col * (tile.width - 2), lin * (tile.height - 2))
                    self.obstacles.append(tile)
            line = level_constructor.readline()
            lin += 1

        level_constructor.close()
