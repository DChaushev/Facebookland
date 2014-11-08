from pygame import math

class Entity:

    pos = math.Vector2

    def __init__(self):
        self.pos.x = 0
        self.pos.y = 0

    def __init__(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def __init__(self, vector):
        self.pos = vector

    def set_pos(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def set_pos(self, vector):
        self.pos = vector