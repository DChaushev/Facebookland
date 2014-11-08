from Game.Direction import *
from pygame import math

class Unit:

    def __init__(self, x, y, type):
        self.pos = math.Vector2(x, y)
        self.walk_up = []
        self.walk_down = []
        self.walk_left = []
        self.walk_right = []
        self.textureID = type
        self.speed = 1

    def get_sprite(self, texture_id):
        pass

    def set_speed(self, s):
        self.speed = s

    def move(self, direction):
        if direction == Direction.LEFT:
            self.pos.x -= self.speed
        if direction == Direction.RIGHT:
            self.pos.x += self.speed
        if direction == Direction.UP:
            self.y -= self.speed
        if direction == Direction.DOWN:
            self.y += self.speed

    def shoot(self):
        #TODO
        pass

    def get_textureID(self):
        return self.textureID