import Common

from Game.Game import Game

if ( __name__== '__main__'):
    print ( "Let's debug this" )

if ( Common.USE_PYQT ):
    from PyQt4.QtCore import QModelIndex
    from PyQt4.QtGui import QWidget, QPixmap
    from PyQt4.QtGui import QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QListView, QLabel, QListWidget
    from PyQt4.QtGui import QListWidgetItem, QFormLayout
else:
    from PySide.QtGui import QWidget, QPixmap
    from PySide.QtGui import QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QListView, QLabel, QListWidget
    from PySide.QtGui import QListWidgetItem, QFormLayout

from RequestWorker import RequestWorker

class MainWidget( QWidget ):
    def __init__(self, parent = None ):
        super(MainWidget, self).__init__( parent )

        self.people = []
        self.selectedPerson = None
        self.requestWorker = RequestWorker( Common.FACEBOOK_INFO_SERVER_ADDRESS )
        self.levelOptions = None

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
        self.playerSpeedLabel     = QLabel()
        self.enemySpeedLabel      = QLabel()
        self.playerDamage         = QLabel()
        self.backgroundTexture    = QLabel()
        self.person_name          = ""

        self.logWithFacebookButton = QPushButton( "Log With Facebook ")
        self.logWithFacebookButton.clicked.connect( self.onLogButtonClicked)

        self.launchButton = QPushButton( "Launch" )
        self.launchButton.setEnabled(False)
        self.launchButton.clicked.connect( self.onLaunchButtonClicked )

        formLayout.addRow( self.logWithFacebookButton  , self.launchButton )
        formLayout.addRow( QLabel( "Level Difficulty" ), self.levelDifficultyLabel )
        formLayout.addRow( QLabel( "Enemies"          ), self.numberOfEnemiesLabel )
        formLayout.addRow( QLabel( "Player Speed"     ), self.playerSpeedLabel )
        formLayout.addRow( QLabel( "Enemy Speed"      ), self.enemySpeedLabel )
        formLayout.addRow( QLabel( "Damage"           ), self.playerDamage )
        formLayout.addRow( QLabel( "World"            ), self.backgroundTexture )

        subLayout.addLayout( formLayout, 1 )

        mainLayout.addLayout( subLayout )
        # DO NOT REMOVE COPYRIGHT INFORMATION! Licensed under CC BY SA
        mainLayout.addWidget(QLabel("Theme song: 'Free Software Song 2' by Jono Bacon CC BY SA"))

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
        self.levelOptions = Common.Level( self.selectedPerson.name, self.selectedPerson.data )
        self.updateFormFromSelectedUser()
        self.launchButton.setEnabled(True)

    def onLaunchButtonClicked( self ):
        game = Game(self.levelOptions)
        game.run()
        print ( "Launch Button Clicked" )

    def onLogButtonClicked(self):
        people = self.requestWorker.request()
        self.setPeople( people )

    def updateFormFromSelectedUser(self):
        self.levelDifficultyLabel.setText( Common.Level.LevelDifficultyToString( self.levelOptions.enemiesDifficulty ) )
        self.numberOfEnemiesLabel.setText( str( self.levelOptions.enemiesCount ) )
        self.enemySpeedLabel.setText( str(self.levelOptions.enemySpeed))
        self.playerSpeedLabel.setText( str(self.levelOptions.playerSpeed))
        self.playerDamage.setText( str(self.levelOptions.damage))

        pix = QPixmap( self.levelOptions.enumTexture.value )

        self.backgroundTexture.setStyleSheet("border-image:url(:/2.png);")
        self.backgroundTexture.setPixmap( pix.scaled( 150, 150 ) )
