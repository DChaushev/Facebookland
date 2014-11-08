from PyQt4 import QtGui

__author__ = 'Admin'

from Common import *
from Game.Player import Player
from Game.TextureHolder import TextureHolder
import pygame

if USE_PYQT:
    from PyQt4 import QtGui
else:
    from PySide import QtGui

import sys

app = QtGui.QApplication(sys.argv)

from MainWidget import MainWidget

testPeople = [ Person("Georgi Sinekliev", "1235" ), Person( "Spas Kiuchukov", "213234" ), Person( "Dimitar Chaushev", "9346" ) ]

def main():
    w = MainWidget()
    w.resize( 550, 350)
    w.setWindowTitle('Simple')

    #test
    w.setPeople( testPeople )

    w.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    print ("Hello world" )