__author__ = 'Yani Maltsev'

SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 720
BG_COLOR = 150, 150, 80

import pygame
import sys

from Game.Global import textureHolder, Texture
from Game.Player import Player
from Game.Enemy import Enemy
from random import randint

def exit_game():
    sys.exit()

class Game:
    def __init__(self, level_options):
        self.level_options = level_options
        self.player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT/2, textureHolder, Texture.PLAYER  )
        self.monsters = [Enemy( 0, 0, textureHolder, Texture.ZOMBIE)]
        for i in range(2):
            self.monsters.append(Enemy (randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT), textureHolder, Texture.ZOMBIE))
        self.projectiles = []
        self.isOver = False
        #self.tree = Unit()
        #self.air = [Unit()]
        #self.environment = []

    def background_render(self, bg, screen):
        x = 0
        while x < SCREEN_WIDTH:
            y = 0
            while y < SCREEN_HEIGHT:
                screen.blit(bg, (x, y))
                y += bg.get_height()
            x += bg.get_width()

    def collision_detection(self, surface_1, surface_2):
        if len(surface_2.walk) > 0 and len(surface_1.walk) > 0:
            rect1 = pygame.Rect(surface_1.pos.x, surface_1.pos.y, surface_1.walk[0].get_width(), surface_1.walk[0].get_height())
            rect2 = pygame.Rect(surface_2.pos.x, surface_2.pos.y, surface_2.texture.get_width(), surface_2.texture.get_width())
            if rect1.colliderect(rect2):
                return True
        else: return False


    def game_over(self, screen, text):
        font1 = pygame.font.Font(None, 140)
        text = font1.render(text, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2

        scale = 1.0/float(5)
        surf_size = screen.get_size()
        scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
        surf = pygame.transform.smoothscale(screen, scale_size)
        surf = pygame.transform.smoothscale(surf, surf_size)


        while 1:
            screen.blit(surf, (0,0))
            screen.blit(text, [text_x, text_y])

            for event in pygame.event.get():
                if event.type in [pygame.K_ESCAPE, pygame.QUIT]:
                    exit_game()

            pygame.display.update()


    def run(self, levelOptions):
        pygame.init()
        screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ), pygame.DOUBLEBUF | pygame.HWSURFACE, 32)
        clock = pygame.time.Clock()
        while True:
            # Limit frame speed to 50 FPS
            time_passed = clock.tick(50)

            if not self.isOver:

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
                            self.projectiles.append( self.player.shoot() )

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
                textureHolder.load(levelOptions.enumTexture, levelOptions.enumTexture.value)
                bg = textureHolder.get(levelOptions.enumTexture)

                self.background_render(bg, screen)
                # Update and redraw all creeps
                #for player in self.players:
                self.player.update()
                self.player.render(screen)

                if len(self.monsters) > 0:
                    for monster in self.monsters:
                        monster.set_target(self.player)
                        monster.update()

                        if self.player.health < 0:
                            self.isOver = True

                        monster.render(screen)
                        if monster.health <= 0:
                            if monster in self.monsters:
                                self.monsters.remove(monster)
                else: #TODO: win after killing all 3 waves of zombies
                    self.game_over(screen, "You Win")

                for bullet in self.projectiles:
                    bullet.update()

                    for monster in self.monsters:
                        if self.collision_detection(monster, bullet):
                            monster.reduce_health(self.player.damage)
                            if bullet in self.projectiles:
                                self.projectiles.remove(bullet)
                            print(monster.health)


                    bullet.render( screen )

                #for cloud in self.air:
                #    cloud.update()
                 #   cloud.render(screen)

                pygame.display.flip()

            else:
                self.game_over(screen, "Game Over")