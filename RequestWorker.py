__author__ = 'Admin'

from PyQt4.QtCore import pyqtSignal

import json
from urllib.request import urlopen

class RequestWorker:
    def __init__( self, serverPath ):
        self.serverPath = serverPath
        self.data = None

        ready = pyqtSignal()

    def request(self):
        self.data = json.load( urlopen( self.serverPath ) )
        #TODO: parse request

