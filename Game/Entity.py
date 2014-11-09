from pygame import math

class Entity:

    pos = math.Vector2

    def __init__(self, vector, texture_holder, id):
        self.pos = vector
        self.texture = texture_holder.get(id)
        self.health_bar = False

    def set_pos(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def set_pos(self, vector):
        self.pos = vector

    def set_texture(self, texture_holder, id):
        self.texture = texture_holder.get(id)

    def update(self):
        pass

    def render(self, screen):
        '''stationary render'''
        pass
