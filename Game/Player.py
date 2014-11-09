__author__ = 'Yani Maltsev'

from Game.Unit import Unit
from Game.Arrow import Arrow
import pygame
import math
from Game.Global import Texture, textureHolder

class Player(Unit):
     def __init__(self, x, y, texture_holder, id):
        Unit.__init__(self, x, y, texture_holder, id)
        self.load_animations()
        self.speed = 3

     def Shoot_arrow( self ):
        arrow = Arrow( self.pos.x, self.pos.y, textureHolder, Texture.BULLET )
        arrow.set_direction(self.get_orientation())
        arrow.set_speed(15)
        return arrow


     def load_animations(self):
         x = 0
         for i in range(3):
            sheet = self.texture
            sheet.set_clip(pygame.Rect(x, 0, 101, 151))
            draw_me = sheet.subsurface(sheet.get_clip())
            draw_me = pygame.transform.scale(draw_me, (50, 75))
            self.walk.append(draw_me)
            x += 132
         self.walk.append(self.walk[1])
         self.idle_animation = self.walk[1]
