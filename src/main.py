from library.PPlay.window import Window
from library.PPlay.sprite import Sprite
from library.PPlay.animation import Animation
from library.PPlay.gameimage import load_image
from library.PPlay.keyboard import Keyboard
from level_control import LevelControl
import globals

def main():
	window = Window(globals.WIDTH, globals.HEIGHT)
	window.set_title("JSC")
	jorge = Animation("./src/assets/jorge_idle.png", 8)
	background = Sprite("./src/assets/background.png")
	lifebar = Sprite("./src/assets/lifebar.png")
	
	jorge.set_position(window.width/2 - jorge.width/2, window.height - 50 - jorge.height)
	background.set_position(0, -50)

	keyboard = Keyboard()

	lifebar.draw()
	background.draw()
	jorge.set_total_duration(800)
	jorge.play()
	jorge.draw()
	
	map = LevelControl(window, globals.LEVEL1)

	while globals.GAME_STARTED:
		if keyboard.key_pressed("right"):
			jorge.image, jorge.rect = load_image("./src/assets/jorge_running.png", alpha=True)
		else:
			jorge.image, jorge.rect = load_image("./src/assets/jorge_idle.png", alpha=True)

		background.draw()
		lifebar.draw()
		map.update()
		jorge.update()
		jorge.draw()

		window.update()

if __name__ == "__main__":
	main()
