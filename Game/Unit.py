
from Game.Entity import Entity
from pygame.math import Vector2
from pygame import transform

class Unit(Entity):
    def __init__(self, x, y, texture_holder, id):
        Entity.__init__(self, (x, y), texture_holder, id)
        self.walk_up = []
        self.walk_down = []
        self.walk_left = []
        self.walk_right = []
        self.speed = 1
        self.health = 10
        self.direction = Vector2(0,0)
        self.animation_count = 0
        self.animation_count_max = 20



    def get_sprite(self, texture_id):
        pass

    def add_direction(self, dir):
        self.direction += dir
        print(self.direction.angle_to((0, -1)))

    def set_direction(self, dir):
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

        screen.blit(transform.rotate(self.walk_up[int(self.animation_count/20)], self.direction.angle_to((0, -1))), self.pos)

        # if self.direction.x<0 and self.direction.y<0:
        #     """ up-left animation"""
        #     return
        # if(self.direction.x<0 and self.direction.y>0):
        #     """ down-left animation"""
        #     return
        # if(self.direction.x>0 and self.direction.y<0):
        #     """ up-right animation"""
        #     return
        # if(self.direction.x>0 and self.direction.y>0):
        #     """ down-right animation"""
        #     return
        # if(self.direction.x<0):
        #     """ left animation"""
        #     return
        # if(self.direction.x>0):
        #     """ right animation"""
        #     return
        # if(self.direction.y<0):
        #     """ up animation"""
        #     return
        # if(self.direction.y>0):
        #     """ down animation"""
        #     return
        # if (self.direction.x == 0 and self.direction.y == 0):
        #     Entity.render(screen)



    def generate_animations(self):
         pass
