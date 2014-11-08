USE_PYQT = True

FACEBOOK_INFO_SERVER_ADDRESS = ""

from random import random
import json

class Person:
    def __init__( self, name ):
        self.name = name;

    def name(self):
        return self.name

class Level:
    def __init__(self, data ):
        cities =  [ "Dungeon", "Castle", "Rampart", "Conflux" ]
        self.city = cities[ int( data[ 0 ] ) % len( cities ) ]
        self.enemiesDifficulty = int( data[ 1 ] ) % 5
        self.enemiesCount =  int( data[ 2 ] ) * 4

def testLevelParsing ():

    jsonString = '[{"name":"Nikolay Boshnakov","data":"12345678"},{"name":"Nikolay Todorov","data":"12345678"},{"name":"Svetlin Nakov","data":"12345678"},{"name":"Stefan Kanev","data":"12345678"},{"name":"Nadejda Miteva","data":"12345678"},{"name":"Alexander Georgiev","data":"12345678"},{"name":"Dimitar Chaushev","data":"12345678"}]'

    data = json.loads( jsonString )

    sampleLevel = Level( data[ 0 ][ 'data' ] )
    print ( sampleLevel.city )
    print ( sampleLevel.enemiesDifficulty )
    print ( sampleLevel.enemiesCount )

if __name__ == "__main__":
    testLevelParsing()