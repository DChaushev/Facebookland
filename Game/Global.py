from enum import Enum

from Game.TextureHolder import TextureHolder

class Texture(Enum):
    PLAYER = 'Game/Resources/textures/Units/hero.png'
    ZOMBIE = 'Game/Resources/textures/Units/zombie.png'

#use single instance of Texture Holder
textureHolder = TextureHolder()
textureHolder.load(Texture.PLAYER, Texture.PLAYER.value)
