__author__ = 'Yani Maltsev'

from Game.Unit import Unit
from Game.Arrow import Arrow
import pygame
import math

class Player(Unit):
     def __init__(self, x, y, texture_holder, id):
        Unit.__init__(self, x, y, texture_holder, id)

     def Shoot_arrow(self):
        pass

     def load_animations(self):
         x = 0
         for i in range(3):
            #self.walk_up.append(self.texture)#pygame.transform.chop(self.texture, (x, 0, 100, 150)))
            sheet = self.texture
            sheet.set_clip(pygame.Rect(x, 0, 100, 150))
            draw_me = sheet.subsurface(sheet.get_clip())
            draw_me = pygame.transform.scale(draw_me, (50, 75))
            self.walk_up.append(draw_me)
            #self.walk_down.append(pygame.transform.flip(draw_me, True, True))
            x += 130
         self.animation_count_max *= len(self.walk_up)-1
