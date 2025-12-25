import pygame
from constants import *
from logger import log_state
from player import *


def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	player_pos_x=SCREEN_WIDTH /2
	player_pos_y=SCREEN_HEIGHT/2
	player = Player(player_pos_x,player_pos_y)

	game_running = True
	while game_running == True:
		log_state()

		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

		screen.fill("black")

		player.update(dt)
		player.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
