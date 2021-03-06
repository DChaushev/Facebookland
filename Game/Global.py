from enum import Enum

from Game.TextureHolder import TextureHolder

class Texture(Enum):
    PLAYER = 'Game/Resources/textures/Units/hero.png'
    ZOMBIE = 'Game/Resources/textures/Units/zombie.png'
    BULLET = 'Game/Resources/textures/Misc/bullet.png'
    BACKGROUND = 'SELECTED DOWN'
    TREE1 = 'Game/Resources/textures/Entities/tree1.png'
    TREE2 = 'Game/Resources/textures/Entities/tree2.png'
    TREE3 = 'Game/Resources/textures/Entities/tree3.png'

class Background(Enum):
    LAVA = 'Game/Resources/textures/Background/lava.jpg'
    ICE = 'Game/Resources/textures/Background/ice.jpg'
    GRASS = 'Game/Resources/textures/Background/grass.jpg'
    BLUEROCK = 'Game/Resources/textures/Background/bluerock.jpg'
    FLAGSTONE = 'Game/Resources/textures/Background/flagston.jpg'
    WATER = 'Game/Resources/textures/Background/water.jpg'
    CIRCUIT = 'Game/Resources/textures/Background/circuit5.jpg'
    GREENY = 'Game/Resources/textures/Background/greeny.jpg'
    FLOWER1 = 'Game/Resources/textures/Background/tile09.jpg'
    BOLTS = 'Game/Resources/textures/Background/rivits.gif'

backgrounds_list = []

for bg in Background:
        backgrounds_list.append(bg)

#use single instance of Texture Holder
textureHolder = TextureHolder()

MUSIC = 'Game/Resources/Sounds/theme.mp3'

for texture in Texture:
    if not texture == Texture.BACKGROUND:
        textureHolder.load(texture, texture.value)

textureHolder.load( Texture.BACKGROUND, Background.BLUEROCK.value)