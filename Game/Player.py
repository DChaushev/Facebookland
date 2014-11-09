from pygame import transform, draw
from pygame.rect import Rect

__author__ = 'Yani Maltsev'

from Game.Unit import Unit
from Game.Bullet import Bullet
import pygame
import math
from Game.Global import Texture, textureHolder


class Player(Unit):

    def __init__(self, x, y, texture_holder, id):
        Unit.__init__(self, x, y, texture_holder, id)
        self.load_animations()
        self.default_speed = 5
        self.speed = 0
        self.health_bar = True

    def shoot( self ):
        bullet = Bullet( self.pos.x, self.pos.y, textureHolder, Texture.BULLET )
        bullet.set_direction(self.get_orientation())
        bullet.set_speed( 15 )
        return bullet

    def set_speed(self, s):
        self.default_speed = s

    def render(self, screen):
        if self.animation_count == self.animation_count_max:
            self.animation_count = 0
        else:
            self.animation_count += 1

        angle = self.direction.angle_to((0, -1))

        if self.speed != 0:
            animation_index = int(int((self.animation_count * len(self.walk)) - 1)/self.animation_count_max)
            screen.blit(transform.rotate(self.walk[animation_index], angle), self.pos)
        else:
            if self.idle_animation != None:
               screen.blit(transform.rotate(self.idle_animation, angle), self.pos)

        if self.health_bar and len(self.walk) > 0:
            health_bar = Rect(self.pos.x, self.pos.y, (self.health * self.walk[0].get_width())/100, -5)
            draw.rect(screen, (255, 0, 0), health_bar, 0)

    def load_animations(self):
        x = 0
        for i in range(3):
            sheet = self.texture
            sheet.set_clip(pygame.Rect(x, 0, 101, 151))
            draw_me = sheet.subsurface(sheet.get_clip())
            draw_me = pygame.transform.scale(draw_me, (50, 75))
            self.walk.append(draw_me)
            x += 132
        self.walk.append(self.walk[1])
        self.idle_animation = self.walk[1]
