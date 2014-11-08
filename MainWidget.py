import Common

from Game.Game import Game

if ( __name__== '__main__'):
    print ( "Let's debug this" )

if ( Common.USE_PYQT ):
    from PyQt4.QtCore import QModelIndex
    from PyQt4.QtGui import QWidget
    from PyQt4.QtGui import QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QListView, QLabel, QListWidget
    from PyQt4.QtGui import QListWidgetItem, QFormLayout
else:
    from PySide.QtGui import QWidget
    from PySide.QtGui import QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QListView, QLabel, QListWidget
    from PySide.QtGui import QListWidgetItem, QFormLayout

from RequestWorker import RequestWorker

class MainWidget( QWidget ):
    def __init__(self, parent = None ):
        super(MainWidget, self).__init__( parent )

        self.people = []
        self.selectedPerson = None
        self.requestWorker = RequestWorker( Common.FACEBOOK_INFO_SERVER_ADDRESS )
        self.gameInstance = Game()

        mainLayout = QVBoxLayout( self )
        title = QLabel( "Faceland" )
        mainLayout.addWidget( title )

        subLayout = QHBoxLayout()
        self.peopleView = QListWidget()
        self.peopleView.itemClicked.connect( self.onPersonSelected )
        subLayout.addWidget( self.peopleView, 1 )

        #form layout
        formLayout = QFormLayout()
        self.levelNameLabel       = QLabel()
        self.levelDifficultyLabel = QLabel()
        self.numberOfEnemiesLabel = QLabel()
        self.backGroundTexture    = QLabel()

        self.logWithFacebookButton = QPushButton( "Log With Facebook ")
        self.logWithFacebookButton.clicked.connect( self.onLogButtonClicked)

        self.launchButton = QPushButton( "Launch" )
        self.launchButton.clicked.connect( self.onLaunchButtonClicked )

        formLayout.addRow( QLabel( "Level Name"       ), self.levelNameLabel )
        formLayout.addRow( QLabel( "Level Difficulty" ), self.levelNameLabel )
        formLayout.addRow( QLabel( "Enemies"          ), self.levelNameLabel )
        formLayout.addRow( QLabel( "World"            ), self.levelNameLabel )
        formLayout.addRow( self.logWithFacebookButton  , self.launchButton   )
        subLayout.addLayout( formLayout, 1 )

        mainLayout.addLayout( subLayout )
        self.setLayout( mainLayout )

    def resetPeoplesWidget(self, aPeople ):
        self.peopleView.clear()
        self.people = aPeople
        for person in aPeople:
            item = QListWidgetItem( str(person.name) )
            # item.
            self.peopleView.addItem( item )

    def setPeople( self, aPeople ):
        self.resetPeoplesWidget( aPeople )

    def onPersonSelected( self, item ):
        row = self.peopleView.row( item )
        self.selectedPerson = self.people[ row ]
        print ( "{0} is selected".format( self.selectedPerson.name ) )

    def onLaunchButtonClicked( self ):
        self.gameInstance.run()
        print ( "Launch Button Clicked" )

    def onLogButtonClicked(self):
        self.requestWorker.request()