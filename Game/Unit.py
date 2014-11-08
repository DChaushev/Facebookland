
from Game.Entity import Entity
from pygame.math import Vector2
from pygame import transform

class Unit(Entity):
    def __init__(self, x, y, texture_holder, id):
        Entity.__init__(self, (x, y), texture_holder, id)
        self.walk = []
        self.speed = 1
        self.health = 100
        self.direction = Vector2(0,0)
        self.animation_count = 0
        self.animation_count_max = 30
        self.last_vector = Vector2(0, -1)

    def get_sprite(self, texture_id):
        pass

    def add_direction(self, dir):
        self.set_direction(self.direction + dir)

    def set_direction(self, dir):
        self.last_vector = self.direction
        self.direction = dir

    def reduce_health(self):
        self.health -= 1

    def set_speed(self, s):
        self.speed = s

    def move(self):
        self.pos += self.direction * self.speed

    def update(self):
        self.move()

    def render(self, screen):
        if self.animation_count == self.animation_count_max:
            self.animation_count = 0
        else:
            self.animation_count += 1

        angle = 0
        if not self.direction.x == 0 or not self.direction.y == 0:
            angle = self.direction.angle_to((0, -1))
            animation_index = int(int((self.animation_count * len(self.walk)) - 1)/self.animation_count_max)
            print(animation_index)

            screen.blit(transform.rotate(self.walk[animation_index], angle), self.pos)
        else:
            angle = self.last_vector.angle_to((0, -1))
            if self.idle_animation != None:
               screen.blit(transform.rotate(self.idle_animation, angle), self.pos)



    def generate_animations(self):
         pass
