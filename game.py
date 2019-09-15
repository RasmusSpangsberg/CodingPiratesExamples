# Lav jeres eget spil!
# Ideer:
# lav en scetch til et spil og skriv lidt om hvad man skal kunne gøre

# Lav små opgaver inden pygame så de kan lære lidt at tænkte

import pygame
pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

GREY = (200, 200, 200)
GREEN = (0, 255, 0)

BACKGROUND_COLOR = GREY

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(GREY)

def draw_player():
	ground = pygame.Rect([0, SCREEN_HEIGHT // 3, SCREEN_WIDTH, SCREEN_HEIGHT])
	pygame.draw.rect(screen, GREEN, ground)

class Player:
	def __init__(self):
		self.speed = 5
		self.direction = "left"
		self.body = pygame.Rect([SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 50, 50])
		
		self.velocity_x = 0
		self.velocity_y = 0

	def update(self, keys_pressed, events):
		pygame.draw.rect(screen, GREEN, self.body)
		
		# This is the easiest to understand approach that i have found.
		if keys_pressed[pygame.K_LEFT]:
			self.body.x -= self.speed
		if keys_pressed[pygame.K_RIGHT]:
			self.body.x += self.speed
		if keys_pressed[pygame.K_UP]:
			self.body.y -= self.speed
		if keys_pressed[pygame.K_DOWN]:
			self.body.y += self.speed

		# Other examples of movements:
		# we can't use "pygame.event.get()" here, because
		# we have already used it once (in the while-loop,
		# the method dequeues all events from a queue), 
		# so we need to store the output the first time in 
		# a variable (events), and then pass it to this function
		'''
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.velocity_x -= self.speed
				if event.key == pygame.K_RIGHT:
					self.velocity_x += self.speed
				if event.key == pygame.K_UP:
					self.velocity_y -= self.speed
				if event.key == pygame.K_DOWN:
					self.velocity_y += self.speed

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.velocity_x += self.speed
				if event.key == pygame.K_RIGHT:
					self.velocity_x -= self.speed
				if event.key == pygame.K_UP:
					self.velocity_y += self.speed
				if event.key == pygame.K_DOWN:
					self.velocity_y -= self.speed
		
		self.body.x += self.velocity_x
		self.body.y += self.velocity_y
		'''

player = Player()

playing = True
while playing:
	keys_pressed = pygame.key.get_pressed()

	if keys_pressed[pygame.K_ESCAPE]:
		playing = False

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.fill(BACKGROUND_COLOR)
	
	player.update(keys_pressed, events)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()