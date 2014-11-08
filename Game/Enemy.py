__author__ = 'Yani Maltsev'

from Game.Unit import Unit
from Game.Entity import Entity
from pygame.math import Vector2


class Enemy(Unit):

    target_pos = Vector2()
    def __init__(self, x, y, texture_holder, id):
        Unit.__init__(self, x, y, texture_holder, id)
        self.target = Entity
        self.attack_distance = 1

    def set_target(self, target_):
        self.target = target_

    def remove_target(self):
        target = None

    def update(self):
        direction = (self.target.pos - self.pos).normalize
        Unit.update()
        if (self.target.pos-self.pos).length <= self.attack_distance:
            self.target.reduce_health()
