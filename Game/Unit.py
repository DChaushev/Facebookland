from Game.Direction import Direction
from Game.Entity import Entity

class Unit(Entity):

    def __init__(self, x, y, texture_holder, id):
        Entity.__init__(self, x, y, texture_holder, id)
        self.walk_up = []
        self.walk_down = []
        self.walk_left = []
        self.walk_right = []
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

    def generate_animations(self):
        pass

    def shoot(self):
        pass
