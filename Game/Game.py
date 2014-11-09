__author__ = 'Yani Maltsev'

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
ARENA_WIDTH = 1500
ARENA_HEIGHT = 1000
BG_COLOR = 150, 150, 80

import pygame
import sys

from Game.Global import textureHolder, Texture, Background
from Game.Player import Player
from Game.Enemy import Enemy
from Game.Entity import Entity
from random import randint, choice
from pygame import math


class Game:
    def __init__(self, level_options):
        self.level_options = level_options
        self.view_x = (ARENA_WIDTH - SCREEN_WIDTH) / 2
        self.view_y = (ARENA_HEIGHT - SCREEN_HEIGHT) / 2
        self.player = Player( self.view_x + SCREEN_WIDTH / 2, self.view_y + SCREEN_HEIGHT/2, textureHolder, Texture.PLAYER  )
        self.monsters = [Enemy( 0, 0, textureHolder, Texture.ZOMBIE)]
        self.projectiles = []
        #self.tree = Unit()
        self.air = []
        #self.environment = []

        self.generate_level()

    def generate_level(self):
        for i in range(self.level_options.enemiesCount):

            uy = randint(0, self.view_y)
            dy = randint(self.view_y + SCREEN_HEIGHT, ARENA_HEIGHT)
            lx = randint(0, self.view_x)
            rx = randint(self.view_x + SCREEN_WIDTH, ARENA_WIDTH)

            spawn_x = choice([lx, rx])
            spawn_y = choice([uy, dy])

            monster = Enemy (spawn_x, spawn_y, textureHolder, Texture.ZOMBIE)
            monster.set_speed(self.level_options.enemySpeed)
            self.monsters.append(monster)

        if self.level_options.enumTexture == Background.GRASS:
            for i in range(20):
                self.air.append(Entity((randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)), textureHolder, Texture.TREE2))

        self.player.set_speed(self.level_options.playerSpeed)
        self.player.set_damage(self.level_options.damage)


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
            rect2 = pygame.Rect(surface_2.pos.x, surface_2.pos.y, surface_2.texture.get_width(), surface_2.walk[0].get_width())
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


    def get_min(self, collisions):
        d = collisions[0]
        min_d = collisions[0].pos.distance_to(self.player.pos)
        for i, c in enumerate(collisions):
            if c.pos.distance_to(self.player.pos) <= min_d:
                min_d = c.pos.distance_to(self.player.pos)
                d = collisions[i]
        return d

    def handle_bullet(self, bullet, screen):
        bullet.update()

        if bullet.pos.x < 0 or bullet.pos.x > ARENA_WIDTH or bullet.pos.y < 0 or bullet.pos.y > ARENA_HEIGHT:
            self.projectiles.remove(bullet)
            return

        collisions = []

        for monster in self.monsters:
            if self.collision_detection(monster, bullet):
                collisions.append(monster)
            if len(collisions) > 0:
                m = self.get_min(collisions)
                m.reduce_health(self.player.damage)
                    #monster.reduce_health(self.player.damage)
                if bullet in self.projectiles:
                    self.projectiles.remove(bullet)
                # break
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

            self.update_view_coordinates()

            for cloud in self.air:
               cloud.update()
               cloud.render(arena)

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