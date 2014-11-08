__author__ = 'Yani Maltsev'

from Game.Unit import Unit
from Game.Arrow import Arrow

class Player(Unit):
     def __init__(self, x, y, texture_holder, id):
        Unit.__init__(self, x, y, texture_holder, id)

     def Shoot_arrow(self):
        pass

