from PPlay.window import Window
from PPlay.sprite import Sprite
from level_control import LevelControl
import globals

def main():
    window = Window(globals.WIDTH, globals.HEIGHT)
    window.set_title("JSC")
    player = Sprite("src\\assets\\sprite_player clone-1.png.png")
    background = Sprite("src\\assets\\maxresdefault.jpg")
    lifebar = Sprite("src\\assets\\lifebar.png")
    
    player.set_position(window.width/2 - player.width/2, window.height - 50 - player.height)
    background.set_position(0, -50)

    lifebar.draw()
    background.draw()
    player.draw()
    
    map = LevelControl(window, globals.LEVEL1)

    while globals.GAME_STARTED:
        background.draw()
        lifebar.draw()
        map.run()
        player.draw()

        window.update()

if __name__ == "__main__":
    main()