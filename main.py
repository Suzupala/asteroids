import pygame
import sys

from constants import *
from logger import log_state, log_event

from circleshape import *
from asteroid import *
from player import *
from shot import *
from asteroidfield import AsteroidField

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	shots = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Shot.containers = (shots, updatable, drawable)
	Player.containers = (updatable , drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	player_pos_x=SCREEN_WIDTH /2
	player_pos_y=SCREEN_HEIGHT/2
	player = Player(player_pos_x,player_pos_y)
	asteroidfield = AsteroidField()

	game_running = True
	while game_running == True:
		log_state()

		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

		screen.fill("black")

		updatable.update(dt)
		for sprite in drawable:
			sprite.draw(screen)

		for asteroid in asteroids:
			if player.collides_with(asteroid):
				log_event("player_hit")
				print("Game over!")
				sys.exit()

		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					log_event("asteroid_shot")
					shot.kill()
					asteroid.split()

		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
