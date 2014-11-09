__author__ = 'Yani Maltsev'

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
ARENA_WIDTH = 1500
ARENA_HEIGHT = 1000
BG_COLOR = 150, 150, 80

import pygame
import sys

from Game.Global import textureHolder, Texture
from Game.Player import Player
from Game.Enemy import Enemy
from random import randint
from pygame import math


class Game:
    def __init__(self, level_options):
        self.level_options = level_options
        self.player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT/2, textureHolder, Texture.PLAYER  )
        self.monsters = [Enemy( 0, 0, textureHolder, Texture.ZOMBIE)]
        for i in range(2):
            self.monsters.append(Enemy (randint(0, ARENA_WIDTH - 1), randint(0, ARENA_HEIGHT - 1), textureHolder, Texture.ZOMBIE))
        self.projectiles = []
        self.view_x = (ARENA_WIDTH - SCREEN_WIDTH) / 2
        self.view_y = (ARENA_HEIGHT - SCREEN_HEIGHT) / 2
        #self.tree = Unit()
        #self.air = [Unit()]
        #self.environment = []

    def exit(self):
        #self.exitGame = True
        pygame.quit()

    def background_render(self, bg, screen):
        x = 0
        while x < ARENA_WIDTH:
            y=0
            while y < ARENA_HEIGHT:
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

        scale = 1.0/float(4)
        surf_size = screen.get_size()
        scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
        surf = pygame.transform.smoothscale(screen, scale_size)
        surf = pygame.transform.smoothscale(surf, surf_size)

        while True:
            screen.blit(surf, (0,0))
            screen.blit(text, [text_x, text_y])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exit()
                        return

            pygame.display.update()


    def handle_bullet(self, bullet, screen):
        bullet.update()

        if bullet.pos.x < 0 or bullet.pos.x > ARENA_WIDTH or bullet.pos.y < 0 or bullet.pos.y > ARENA_HEIGHT:
            self.projectiles.remove(bullet)
            return

        for monster in self.monsters:
            if self.collision_detection(monster, bullet):
                monster.reduce_health(self.player.damage)
                if bullet in self.projectiles:
                    self.projectiles.remove(bullet)
                #print(monster.health)
        bullet.render( screen )

    def handle_monsters(self, screen):
        for monster in self.monsters:
            monster.set_target(self.player)
            monster.update()
            monster.render(screen)
            if monster.health <= 0:
                if monster in self.monsters:
                    self.monsters.remove(monster)


    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF,)
        arena = pygame.Surface((ARENA_WIDTH, ARENA_HEIGHT), pygame.HWSURFACE)
        clock = pygame.time.Clock()
        #diagonal = False
        #diag_holdon = 0
        #diag_multi = math.Vector2(0, 0)

        while True:
            # Limit frame speed to 50 FPS
            time_passed = clock.tick(50)



            # Redraw the background
            arena.fill(BG_COLOR)
            textureHolder.load(self.level_options.enumTexture, self.level_options.enumTexture.value)
            bg = textureHolder.get(self.level_options.enumTexture)

            self.background_render(bg, arena)

            if self.handle_user_input():
                return

            # Update and redraw all creeps
            self.player.update()
            self.player.render(arena)

            if len(self.monsters) > 0:
                self.handle_monsters(arena)
            else: #TODO: win after killing all 3 waves of zombies
                self.game_over(screen, "You Win")
                return

            if self.player.health < 0:
                self.game_over(screen, "Game Over")
                return

            for bullet in self.projectiles:
                self.handle_bullet(bullet, arena)
                #print(len(self.projectiles))

            #for cloud in self.air:
            #    cloud.update()
            #   cloud.render(screen)

            self.update_view_coordinates()

            screen.blit(arena, (0, 0), pygame.Rect(self.view_x, self.view_y, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.flip()

    def handle_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
                return True
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
                    self.exit()
                    return True
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

        return False;

    def update_view_coordinates(self):
        if self.player.pos.x > 3/4 * SCREEN_WIDTH + self.view_x:
            self.view_x = self.player.pos.x - 3/4 * SCREEN_WIDTH
        if self.view_x > ARENA_WIDTH - SCREEN_WIDTH:
            self.view_x = ARENA_WIDTH - SCREEN_WIDTH
        if self.player.pos.x < 1/4 * SCREEN_WIDTH + self.view_x:
            self.view_x = self.player.pos.x - 1/4 * SCREEN_WIDTH
        if self.view_x < 0:
            self.view_x = 0
        if self.player.pos.y > 3/4 * SCREEN_HEIGHT + self.view_y:
            self.view_y = self.player.pos.y - 3/4 * SCREEN_HEIGHT
        if self.view_y > ARENA_HEIGHT - SCREEN_HEIGHT:
            self.view_y = ARENA_HEIGHT - SCREEN_HEIGHT
        if self.player.pos.y < 1/4 * SCREEN_HEIGHT + self.view_y:
            self.view_y = self.player.pos.y - 1/4 * SCREEN_HEIGHT
        if self.view_y < 0:
            self.view_y = 0