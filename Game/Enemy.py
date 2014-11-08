__author__ = 'Yani Maltsev'

from Game.Unit import Unit
from Game.Entity import Entity
from pygame.math import Vector2
import pygame

class Enemy(Unit):

    target_pos = Vector2()
    def __init__(self, x, y, texture_holder, id):
        Unit.__init__(self, x, y, texture_holder, id)
        self.target = Entity
        self.speed = 2.5
        self.attack_distance = 50
        self.load_animations()

    def set_target(self, target_):
        self.target = target_

    def remove_target(self):
        target = None

    def update(self):
        if (self.target.pos - self.pos).length() < self.speed:
            self.direction = Vector2(0, 0);
        else:
            self.set_direction((self.target.pos - self.pos).normalize())
        Unit.update(self)
        if (self.target.pos-self.pos).length() <= self.attack_distance:
            self.target.reduce_health()

    def load_animations(self):
        x = 0
        for i in range(8):
           sheet = self.texture
           sheet.set_clip(pygame.Rect(x, 0, 45, 40))
           draw_me = sheet.subsurface(sheet.get_clip())
           draw_me = pygame.transform.scale(draw_me, (50, 75))
           self.walk.append(draw_me)
           x += 45
        self.idle_animation = self.walk[0]