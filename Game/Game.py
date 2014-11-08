__author__ = 'Yani Maltsev'

SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 720
BG_COLOR = 150, 150, 80

import pygame
import sys

from Game.Global import textureHolder, Texture
from Game.Player import Player

def exit_game():
    sys.exit()

class Game:
    def __init__(self):
        self.player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT/2, textureHolder, Texture.PLAYER  )
        self.monsters = []
        self.projectiles = []
        #self.environment = []

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ), 0, 32)
        clock = pygame.time.Clock()
        while True:
            # Limit frame speed to 50 FPS
            time_passed = clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.player.add_direction((0, -1))
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.player.add_direction((0, 1))
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        self.player.add_direction((-1, 0))
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.player.add_direction((1, 0))


                elif event.type == pygame.KEYUP:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.player.add_direction((0, 1))
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.player.add_direction((0, -1))
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        self.player.add_direction((1, 0))
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.player.add_direction((-1, 0))

            # Redraw the background
            screen.fill(BG_COLOR)

            # Update and redraw all creeps
            #for player in self.players:
            self.player.update()
            self.player.render(screen)

            for monster in self.monsters:
                monster.update()
                monster.render(screen)

            for projectile in self.projectiles:
                projectile.update()
                projectile.render(screen)

            pygame.display.flip()