__author__ = 'Yani Maltsev'

from Game.Unit import Unit

class Bullet(Unit):
    def __init__(self, x, y, texture_holder, id):
        Unit.__init__(self, x, y, texture_holder, id)
        self.load_animations()
        self.speed = 4
        self.is_bullet = True


    def update(self):
        super( Bullet, self ).update()

    def load_animations( self ):
        self.walk.append( self.texture )
        self.idle_animation = self.walk[ 0 ]
