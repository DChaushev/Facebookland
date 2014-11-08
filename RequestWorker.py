__author__ = 'Admin'

from PyQt4.QtCore import pyqtSignal

import json
from urllib.request import urlopen

class RequestWorker:
    def __init__( self, serverPath ):
        self.serverPath = serverPath
        self.data = None
        self.peoplesList = [];
        ready = pyqtSignal()

    def request(self):
        self.data = json.load( urlopen( self.serverPath ) )
        print( self.data )
        for name in self.data['name']:
            self.peoplesList.append( name )

        return self.peoplesList;

