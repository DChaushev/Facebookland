from pygame import image

class TextureHolder:

    def __init__(self):
        self.textures = {}

    def load(self, texture_id, file_name):
        texture = image.load(file_name)
        self.textures[texture_id, texture]

    def get(self, texture_id):
        if texture_id in self.textures:
            return self.textures[texture_id]