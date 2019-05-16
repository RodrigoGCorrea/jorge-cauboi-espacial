from library.PPlay.animation import Animation 
from library.PPlay.gameimage import load_image
import globals

class Entity(object):
	def __init__(self, sprite_path, frames, level_control_obj=0):
		self.level_control_obj = level_control_obj

		self.frames = frames
		self.animation = Animation(sprite_path, frames)
		self.animation.set_position(globals.WIDTH/2 - self.animation.width/2, globals.HEIGHT - self.animation.height - 20)
		self.animation.set_total_duration(self.frames * globals.FRAME_SPEED)
		self.animation.play()

		self.strg = 1 
		self.dex = 1
		self.life = 20
		self.lvl = 1

		self.collided_right = False
		self.collided_left = False
		self.moving = 1
		self.jumping = False
		self.y_vel = 0
		self.y0 = self.animation.y
		self.time = 0

		self.idle = True

	def update(self):
		self.animation.update()
		self.animation.draw()
	
	def walk(self, x_velocity):
		if self.collided_left == False and self.collided_right == False:
			self.animation.x += x_velocity

	def jump(self, delta_time):
		if self.jumping == False:
			self.y_vel = globals.Y_VELOCITY_PLAYER
			self.y0 = self.animation.y
			self.time = 0
		else:
			self.animation.y = self.y0 - self.y_vel * self.time - (globals.GRAVITY * (self.time)**2)/2
			self.time += globals.FALL_TIME * delta_time
			print(self.animation.y, - self.y_vel * self.time - (globals.GRAVITY * (self.time)**2)/2, self.y0)

	
	def attack(self):
		pass
	
	def change_animation(self, sprite_path, frames):
		self.frames = frames
		self.animation.image, self.animation.rect = load_image(sprite_path, alpha=True)
		self.animation.set_total_duration(self.frames * globals.FRAME_SPEED)
