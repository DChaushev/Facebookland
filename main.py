from PyQt4 import QtGui

__author__ = 'Admin'

from Common import *
from Game.Player import Player
from Game.TextureHolder import TextureHolder
from Game.Texture import Texture
import pygame

if USE_PYQT:
    from PyQt4 import QtGui
else:
    from PySide import QtGui

import sys

app = QtGui.QApplication(sys.argv)

from MainWidget import MainWidget

testPeople = [ Person("Georgi Sinekliev"), Person( "Spas Kiuchukov" ), Person( "Dimitar Chaushev" ) ]

def main():
    w = MainWidget()
    w.resize( 550, 350)
    w.setWindowTitle('Simple')

    #test
    w.setPeople( testPeople )

    w.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    #main()


    ##TODO DELME

    h = 400
    w = 800

    screen = pygame.display.set_mode( (w, h) )
    clock = pygame.time.Clock()

    th = TextureHolder()
    th.load(Texture.PLAYER, Texture.PLAYER.value)

    player = Player(100, 100, th, Texture.PLAYER)
    player.load_animations()


    while 1:
        screen.fill( (255, 255, 255) )
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    player.add_direction((0, -1))
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    player.add_direction((0, 1))
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    player.add_direction((-1, 0))
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    player.add_direction((1, 0))


            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_w):
                    player.add_direction((0, 1))
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    player.add_direction((0, -1))
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    player.add_direction((1, 0))
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    player.add_direction((-1, 0))

        player.update()

        #screen.blit(pygame.transform.rotate(player.walk_up[0], player.direction.angle_to((0, -1))), (player.pos.x, player.pos.y))
        player.render(screen)

        pygame.display.update()




    print ("Hello world" )