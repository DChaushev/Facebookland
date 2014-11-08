from enum import Enum

from Game.TextureHolder import TextureHolder

class Texture(Enum):
    PLAYER = 'Game/Resources/textures/Units/hero.png'
    ZOMBIE = 'Game/Resources/textures/Units/zombie.png'

    BG_LAVA = 'Game/Resources/textures/Background/lava.jpg'
    BG_ICE = 'Game/Resources/textures/Background/ice.jpg'
    BG_GRASS = 'Game/Resources/textures/Background/grass.jpg'

#use single instance of Texture Holder
textureHolder = TextureHolder()
textureHolder.load(Texture.PLAYER, Texture.PLAYER.value)
textureHolder.load(Texture.ZOMBIE, Texture.ZOMBIE.value)
textureHolder.load(Texture.BG_LAVA, Texture.BG_LAVA.value)
textureHolder.load(Texture.BG_ICE, Texture.BG_ICE.value)
textureHolder.load(Texture.BG_GRASS, Texture.BG_GRASS.value)
