from Game import TextureHolder
from Game.Direction import *

class Unit:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.walk_up = []
        self.walk_down = []
        self.walk_left = []
        self.walk_right = []

    def get_sprite(self, texture_id):
        pass

    def set_speed(self, s):
        self.speed = s

    def move(self, direction):
        if direction == Direction.LEFT:
            self.x -= self.speed
        if direction == Direction.RIGHT:
            self.x += self.speed
        if direction == Direction.UP:
            self.y -= self.speed
        if direction == Direction.DOWN:
            self.y += self.speed

    def shoot(self):
        #TODO
        pass

