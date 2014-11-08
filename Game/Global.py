from enum import Enum

from Game.TextureHolder import TextureHolder

class Texture(Enum):
    PLAYER = 'Game/Resources/textures/Units/hero.png'
    ZOMBIE = 'Game/Resources/textures/Units/zombie.png'
    BACKGROUND = 'SELECTED DOWN'

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

for texture in Texture:
    if not texture == Texture.BACKGROUND:
        textureHolder.load(texture, texture.value)

textureHolder.load( Texture.BACKGROUND, Background.BLUEROCK.value)