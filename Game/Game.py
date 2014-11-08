__author__ = 'Yani Maltsev'

SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 720
BG_COLOR = 150, 150, 80

import pygame
import sys

from Game.Global import textureHolder, Texture
from Game.Player import Player
from Game.Enemy import Enemy

def exit_game():
    sys.exit()

class Game:
    def __init__(self):
        self.player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT/2, textureHolder, Texture.PLAYER  )
        self.monsters = [Enemy( 0, 0, textureHolder, Texture.ZOMBIE)]
        self.projectiles = []
        self.tree = Unit()
        self.air = [Unit()]
        #self.environment = []

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ), pygame.DOUBLEBUF | pygame.HWSURFACE, 32)
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
                    if event.key == pygame.K_ESCAPE:
                        exit_game()
                    if event.key == pygame.K_SPACE:
                        self.player.Shoot_arrow()
                        
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
            bg = textureHolder.get(Texture.BACKGROUND)

            x = 0
            while x < SCREEN_WIDTH:
                y = 0
                while y < SCREEN_HEIGHT:
                        screen.blit(bg, (x, y))
                        y += bg.get_height()
                x += bg.get_width()
            #screen.blit(textureHolder.get(Texture.BG_LAVA), (0, 0))

            # Update and redraw all creeps
            #for player in self.players:
            self.player.update()
            self.player.render(screen)

            for monster in self.monsters:
                monster.set_target(self.player)
                monster.update()
                monster.render(screen)

            for projectile in self.projectiles:
                projectile.update()
                projectile.render(screen)

            for cloud in self.air:
                cloud.update()
                cloud.render(screen)

            pygame.display.flip()