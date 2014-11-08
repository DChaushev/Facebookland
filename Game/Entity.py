from pygame import math

class Entity:

    pos = math.Vector2

    def __init__(self, x, y, texture_holder, id):
        self.pos.x = x
        self.pos.y = y
        self.texture = texture_holder.get(id)

    def __init__(self, vector, texture_holder, id):
        self.pos = vector
        self.texture = texture_holder.get(id)

    def set_pos(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def set_pos(self, vector):
        self.pos = vector

    def set_texture(self, texture_holder, id):
        self.texture = texture_holder.get(id)