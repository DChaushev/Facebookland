from Game.TextureHolder import TextureHolder
from Game.Texture import Texture

#use single instance of Texture Holder
textureHolder = TextureHolder()
textureHolder.load(Texture.PLAYER, Texture.PLAYER.value)
