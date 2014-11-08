__author__ = 'Yani Maltsev'

from Game.Unit import Unit

class Arrow(Unit):
    def __init__(self, x, y, texture_holder, id):
        Unit.__init__(self, x, y, texture_holder, id)
        speed = 3

    def update(self):
        pass
