from library.PPlay.sprite import Sprite

class Level(object):
    def __init__(self, window, level_path):
        self.obstacles = []
        self.floor = []
        self.window = window
        self.__setup(level_path)

    def update(self):
        pass

    def render(self):
        for floor in self.floor:
            floor.draw()
        for obstacles in self.obstacles:
            obstacles.draw()

    def move(self, x_velocity):
        for floor in self.floor:
            floor.x += x_velocity
        for obstacle in self.obstacles:
            obstacle.x += x_velocity

    def __setup(self, level_path):
        level_constructor = open(level_path, "r")

        line = level_constructor.readline()
        lin = 0
        while lin<=28:
            for col in range(len(line)):
                if line[col] == "1":
                    tile = Sprite("./src/assets/obstacles.png")
                    tile.set_position(col * (tile.width - 2), lin * (tile.height - 2))
                    self.obstacles.append(tile)
            line = level_constructor.readline()
            lin += 1

        for col in range(len(line)):
                if line[col] == "1":
                    tile = Sprite("./src/assets/floor.png")
                    tile.set_position(col * (tile.width - 2), lin * (tile.height - 2))
                    self.obstacles.append(tile)

        level_constructor.close()
