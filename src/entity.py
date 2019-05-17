from library.PPlay.animation import Animation 
from library.PPlay.gameimage import load_image
from library.PPlay.keyboard import Keyboard
from pygame.transform import flip
import globals

class Entity(object):
	def __init__(self, sprite_path, frames):
		self.animation = Animation(sprite_path, frames)
		self.animation.set_position(globals.WIDTH/2 - self.animation.width/2, globals.HEIGHT - self.animation.height - 20)
		self.animation.set_total_duration(frames * globals.FRAME_SPEED)
		self.animation.play()

		self.state = "idle" 
		self.direction = "right"

		self.dx = 0
		self.dy = 0
		self.y0 = self.animation.y
		self.y_time = 0

		self.strg = 1 
		self.dex = 1
		self.life = 20
		self.lvl = 1

	def update(self, dt, level):
		if self.state == "walking":
			if self.direction == "left":
				self.dx = -globals.X_VELOCITY_PLAYER
			elif self.direction == "right":
				self.dx = globals.X_VELOCITY_PLAYER
		elif self.state == "idle":
			self.dx = 0
		elif self.state == "jumping":
			self.dy = globals.Y_VELOCITY_PLAYER
			self.jump(self.dy, dt)

		self.walk(self.dx * dt)
		self.set_behavior(level)
	
	def render(self):
		if self.state == "idle":
			self.set_animation("./src/assets/jorge_idle.png", 8)
			if self.direction == "left":
				self.animation.image = flip(self.animation.image, True, False)
		elif self.state == "walking":
			self.set_animation("./src/assets/jorge_running.png", 8)
			if self.direction == "left":
				self.animation.image = flip(self.animation.image, True, False)

		self.animation.update()
		self.animation.draw()
	
	def set_behavior(self, level):
		keyboard = Keyboard()

		# IDLE
		if self.state == "idle":
			# MOVING LEFT
			if keyboard.key_pressed("left") and keyboard.key_pressed("right") == False:
				self.set_direction("left")
				self.set_state("walking")
			# MOVING RIGHT
			elif keyboard.key_pressed("right") and keyboard.key_pressed("left") == False:
				self.set_direction("right")
				self.set_state("walking")
			# JUMPING
			elif keyboard.key_pressed("up"):
				self.set_state("jumping")

		# MOVING
		elif self.state == "walking":
			# STOPPED MOVING
			if (keyboard.key_pressed("left") == False and keyboard.key_pressed("right") == False or 
				keyboard.key_pressed("left") and keyboard.key_pressed("right")):
				self.set_state("idle")
			# JUMPING
			elif keyboard.key_pressed("up"):
				self.set_state("jumping")
			#TODO COLLISION
			for obstacle in level.obstacles:
				if self.animation.collided(obstacle):
					self.set_state("idle")

		# JUMPING
		elif self.state == "jumping":
			# MOVING LEFT
			if keyboard.key_pressed("left") and keyboard.key_pressed("right") == False:
				self.set_direction("left")
			# MOVING RIGHT
			elif keyboard.key_pressed("right") and keyboard.key_pressed("left") == False:
				self.set_direction("right")

	def set_state(self, state):
		if state == "idle" or state == "walking" or state == "jumping":
			self.state = state
		else:
			self.state = "idle"
			print("error: set_state entity")

	def set_direction(self, direction):
		if direction == "right" or direction == "left":
			self.direction = direction
		else:
			self.direction = "right"
			print("error: set_direction entity")

	def set_animation(self, sprite_path, frames):
		self.animation.image, self.animation.rect = load_image(sprite_path, alpha=True)
		self.animation.set_total_duration(frames * globals.FRAME_SPEED)
	
	def walk(self, dx):
		self.animation.x += dx

	def jump(self, dy, dt):
		self.animation.y = self.y0 - dy * self.y_time - (globals.GRAVITY * (self.y_time)**2)/2
		self.y_time += globals.FALL_TIME * dt
	
	def attack(self):
		pass
	
