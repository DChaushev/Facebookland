USE_PYQT = True

FACEBOOK_INFO_SERVER_ADDRESS = ""

from random import random
import json
from Game.Global import *

class Person:
    def __init__( self, aName, aData ):
        self.name = aName
        self.data = aData

    def name(self):
        return self.name

class Level:
    def __init__(self, data ):
        cities =  [ "Dungeon", "Castle", "Rampart", "Conflux" ]
        self.city = cities[ int( data[ 0 ] ) % len( cities ) ]
        self.enemiesDifficulty = int( data[ 1 ] ) % 5
        self.enemiesCount =  int( data[ 2 ] ) * 4
        self.enumTexture = backgrounds_list[ int( data[ 3 ] ) % len ( backgrounds_list ) ]

    @staticmethod
    def LevelDifficultyToString( difficulty ):
        if ( difficulty == 0 ):
            return "Easy"
        elif ( difficulty == 1 ):
            return "Medium"
        elif ( difficulty == 2 ):
            return "Hard"
        elif ( difficulty == 3 ):
            return "Extreme"
        else:
            return "Impossible"


def testLevelParsing ():

    jsonString = '[{"name":"Nikolay Boshnakov","data":"12345678"},{"name":"Nikolay Todorov","data":"12345678"},{"name":"Svetlin Nakov","data":"12345678"},{"name":"Stefan Kanev","data":"12345678"},{"name":"Nadejda Miteva","data":"12345678"},{"name":"Alexander Georgiev","data":"12345678"},{"name":"Dimitar Chaushev","data":"12345678"}]'

    data = json.loads( jsonString )

    sampleLevel = Level( data[ 0 ][ 'data' ] )
    print ( sampleLevel.city )
    print ( sampleLevel.enemiesDifficulty )
    print ( sampleLevel.enemiesCount )

if __name__ == "__main__":
    testLevelParsing()