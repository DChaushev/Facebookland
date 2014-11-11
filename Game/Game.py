SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
ARENA_WIDTH = 1500
ARENA_HEIGHT = 1000
#ZOOM = 1
BG_COLOR = 150, 150, 80

import pygame
import sys

from Game.Global import textureHolder, Texture, Background
from Game.Player import Player
from Game.Unit import Unit
from Game.Enemy import Enemy
from Game.Entity import Entity
from random import randint, choice
from pygame import math, transform
from Game.Global import MUSIC
from pygame import math


class Game:
    def __init__(self, level_options):
        self.level_options = level_options
        self.view_x = (ARENA_WIDTH - SCREEN_WIDTH) / 2
        self.view_y = (ARENA_HEIGHT - SCREEN_HEIGHT) / 2
        self.player = Player(self.view_x + SCREEN_WIDTH / 2, self.view_y + SCREEN_HEIGHT / 2, textureHolder, Texture.PLAYER)
        self.monsters = []
        self.projectiles = []
        self.moonwalk = False
        self.shoot = False
        self.air = []
        print(self.level_options.person_name)
        self.generate_level()
    
    def run(self):
        pygame.init()
        pygame.key.set_repeat(25, 25)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE,)
        arena = pygame.Surface((ARENA_WIDTH, ARENA_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
        clock = pygame.time.Clock()
        
        # pygame.mixer.music.load(MUSIC)
        # pygame.mixer.music.play()
        seconds = (700 + 100 * (self.level_options.enemiesCount - 1)) / (self.player.damage * 4) * 1000
        print(seconds)
        scoreIncrementTimer = 0
        lastFrameTicks = pygame.time.get_ticks()
        
        while True:
            # Limit frame speed to 50 FPS
            time_passed = clock.tick(50)
        
            thisFrameTicks = pygame.time.get_ticks()
            ticksSinceLastFrame = thisFrameTicks - lastFrameTicks
            lastFrameTicks = thisFrameTicks

            scoreIncrementTimer = scoreIncrementTimer + ticksSinceLastFrame
            if scoreIncrementTimer > seconds:
                self.gen_monsters()
                scoreIncrementTimer = 0

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

            #Draw the view on the screen
            screen.blit(arena, (0, 0), pygame.Rect(self.view_x, self.view_y, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.flip()

    def random_coords(self):
        uy = randint(0, int(self.view_y))
        dy = randint(int(self.view_y) + SCREEN_HEIGHT, ARENA_HEIGHT)
        lx = randint(0, int(self.view_x))
        rx = randint(int(self.view_x) + SCREEN_WIDTH, ARENA_WIDTH)
        spawn_x = choice([lx, rx])
        spawn_y = choice([uy, dy])
        
        return  spawn_x, spawn_y

    def gen_monsters(self):
        for i in range(self.level_options.enemiesCount - 1):
            spawn_x, spawn_y = self.random_coords()
            monster = Enemy(spawn_x, spawn_y, textureHolder, Texture.ZOMBIE)
            monster.set_speed(self.level_options.enemySpeed)
            monster.letter = self.level_options.person_name[i]
            self.monsters.append(monster)

    def generate_level(self):

        self.gen_monsters()

        spawn_x, spawn_y = self.random_coords()

        monster = Enemy(spawn_x, spawn_y, textureHolder, Texture.ZOMBIE)
        monster.set_speed(self.level_options.enemySpeed - 0.5)
        #monster.set_damage(monster.damage + 50)
        monster.letter = self.level_options.person_name.split(" ")[0]
        monster.set_health(700)
        self.monsters.append(monster)
        
        #add trees
        for i in range(10):
            self.air.append(Entity((randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)), textureHolder, Texture.TREE2))

        self.player.set_speed(self.level_options.playerSpeed)
        self.player.set_damage(self.level_options.damage)

    def exit(self):
        pygame.quit()

    def background_render(self, bg, screen):
        x = 0
        while x < ARENA_WIDTH:
            y = 0
            while y < ARENA_HEIGHT:
                screen.blit(bg, (x, y))
                y += bg.get_height()
            x += bg.get_width()

    def collision_detection(self, surface_1, surface_2):
        if len(surface_2.walk) > 0 and len(surface_1.walk) > 0:
            rect1 = pygame.Rect(surface_1.pos.x, surface_1.pos.y, surface_1.walk[0].get_width(), surface_1.walk[0].get_height())
            #TODO: check this walks arrays
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
                break
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

    def handle_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
                return True
            elif event.type == pygame.KEYDOWN:
                #event.key in (pygame.K_UP, pygame.K_w)
                if event.key == pygame.K_w:
                    self.player.speed = self.player.default_speed
                if event.key == pygame.K_a:
                    self.player.set_direction(self.player.get_orientation().rotate(-15))
                if event.key == pygame.K_d:
                    self.player.set_direction(self.player.get_orientation().rotate(15))
                if event.key == pygame.K_s:
                    if not self.moonwalk:
                        self.player.speed = -self.player.default_speed
                        self.player.set_direction(-self.player.direction)
                        self.moonwalk = True
                if event.key == pygame.K_SPACE:
                    if not self.shoot:
                        self.projectiles.append(self.player.shoot())
                        self.shoot = True
                if event.key == pygame.K_ESCAPE:
                    self.exit()
                    return True

            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    self.player.speed = 0
                    self.moonwalk = False
                if event.key == pygame.K_SPACE:
                    self.shoot = False
        return False

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