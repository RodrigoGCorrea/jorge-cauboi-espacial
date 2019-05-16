from library.PPlay.window import Window
from library.PPlay.sprite import Sprite
from library.PPlay.animation import Animation
from library.PPlay.gameimage import load_image
from library.PPlay.keyboard import Keyboard
from library.PPlay.gameobject import GameObject
from level_control import LevelControl
from entity import Entity
import globals

def main():
	window = Window(globals.WIDTH, globals.HEIGHT)
	window.set_title("JSC")
	level = LevelControl(window, "./src/levels/level.txt")
	jorge = Entity("./src/assets/jorge_idle.png", 8)
	background = Sprite("./src/assets/space.png")

	keyboard = Keyboard()

	background.draw()

	while globals.GAME_STARTED:
		if keyboard.key_pressed("esc"):
			jorge.animation.set_position(globals.WIDTH/2 - jorge.animation.width/2, globals.HEIGHT - jorge.animation.height - 20)
			jorge.y_vel = 0
			jorge.time = 0
			jorge.jumping = False
		#moving
		if keyboard.key_pressed("right"):
			jorge.walk(globals.X_VELOCITY_PLAYER * window.delta_time())
			jorge.change_animation("./src/assets/jorge_running.png", 8)
			level.move(-globals.X_VELOCITY_LEVEL * window.delta_time() * jorge.moving)

			if jorge.collided_left:
				jorge.animation.set_position(jorge.animation.x + 1, jorge.animation.y)
				jorge.collided_left = False
				jorge.moving = 1
	
		elif keyboard.key_pressed("left"):
			jorge.walk(-globals.X_VELOCITY_PLAYER * window.delta_time())
			jorge.change_animation("./src/assets/jorge_running.png", 8)
			level.move(globals.X_VELOCITY_LEVEL * window.delta_time() * jorge.moving)

			if jorge.collided_right:
				jorge.animation.set_position(jorge.animation.x - 1, jorge.animation.y)
				jorge.collided_right = False
				jorge.moving = 1
		else: 
			jorge.change_animation("./src/assets/jorge_idle.png", 8)

		if keyboard.key_pressed("space") or jorge.jumping:
			jorge.jump(window.delta_time())
			jorge.jumping = True
		#collision
		if not (jorge.collided_left and jorge.collided_right):	
			for obstacle in level.obstacles:
				if jorge.animation.collided(obstacle) and jorge.animation.x > obstacle.x:
					jorge.collided_left = True
					jorge.moving = 0
					break
				if jorge.animation.collided(obstacle) and jorge.animation.x < obstacle.x:
					jorge.collided_right = True
					jorge.moving = 0
					break

		if jorge.jumping:
			for floor in level.floor:
				if jorge.animation.collided(floor):
					jorge.jumping = False
					break
			for obstacle in level.obstacles:
				if jorge.animation.collided(obstacle):
					jorge.jumping = False
					break
			jorge.animation.set_position(jorge.animation.x, jorge.animation.y - 3)
	
		background.draw()
		level.update()
		jorge.update()
		window.update()

if __name__ == "__main__":
	main()
