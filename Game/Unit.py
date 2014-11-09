
from Game.Entity import Entity
from pygame.math import Vector2
from pygame import transform
from Game.Game import ARENA_WIDTH
from Game.Game import ARENA_HEIGHT
from pygame import draw
from pygame import Rect

class Unit(Entity):
    def __init__(self, x, y, texture_holder, id):
        Entity.__init__(self, (x, y), texture_holder, id)
        self.walk = []
        self.default_speed = 1
        self.speed = 1
        self.health = 100
        self.direction = Vector2(0,0)
        self.animation_count = 0
        self.animation_count_max = 30
        self.last_vector = Vector2(0, -1)
        self.damage = 20
        self.is_bullet=False

    def get_sprite(self, texture_id):
        pass

    def add_direction(self, dir):
        self.set_direction(self.direction + dir)

    def set_direction(self, dir):
        self.last_vector = self.direction
        self.direction = dir

    def reduce_health(self, dmg):
        self.health -= dmg

    def get_orientation(self):
        if self.direction == Vector2(0, 0):
            return self.last_vector
        else:
            return self.direction

    def set_speed(self, s):
        self.speed = s

    def set_damage(self, dmg):
        self.damage = dmg

    def move(self):
        if self.direction != Vector2(0, 0):
            self.pos += (self.direction).normalize() * self.speed
        else:
            self.pos += self.direction * self.speed
        if self.is_bullet:
            return
        if self.pos.x < 10:
            self.pos.x = 10
        if self.pos.x > ARENA_WIDTH - self.walk[0].get_height() - 10:
            self.pos.x = ARENA_WIDTH - self.walk[0].get_height() - 10
        if self.pos.y < 10:
            self.pos.y = 10
        if self.pos.y > ARENA_HEIGHT - self.walk[0].get_height() - 10:
            self.pos.y = ARENA_HEIGHT - self.walk[0].get_height() - 10

    def update(self):
        self.move()

    def render(self, screen):
        if self.animation_count == self.animation_count_max:
            self.animation_count = 0
        else:
            self.animation_count += 1

        angle = 0
        if (self.direction.x != 0 or self.direction.y != 0):
            angle = self.direction.angle_to((0, -1))
            animation_index = int(int((self.animation_count * len(self.walk)) - 1)/self.animation_count_max)
            #print(animation_index)

            screen.blit(transform.rotate(self.walk[animation_index], angle), self.pos)
        else:
            angle = self.last_vector.angle_to((0, -1))
            if self.idle_animation != None:
               screen.blit(transform.rotate(self.idle_animation, angle), self.pos)

        if self.health_bar and len(self.walk) > 0:
            health = (self.health * self.walk[0].get_width())/100
            if health < 0:
                health = 0
            health_bar = Rect(self.pos.x, self.pos.y, health, -5)
            draw.rect(screen, (255, 0, 0), health_bar, 0)


    def generate_animations(self):
         pass
