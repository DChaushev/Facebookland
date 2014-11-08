__author__ = 'Admin'

from PyQt4.QtCore import pyqtSignal

import json
import urllib

class RequestWorker:
    def __init__( self, serverPath ):
        self.serverPath = serverPath
        self.data = None

        ready = pyqtSignal()

    def request(self):
        self.data = json.load( urllib.urlopen( self.serverPath ) )
        #TODO: parse request

