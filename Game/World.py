from Game import TextureHolder
from Game import Layer
import math

# class World:
#
#     def __init__(self, window):
#         self._window = Window(window) #from library
#         self._world_view = View(window.get_default_view()) #from library
#         self._textures = TextureHolder()
#         self._scene_graph = SceneNode() #maybe some list instead
#         self._scene_layers = 0 #list of graphs for the different layers
#         self._command_queue = 0
#         self._world_bounds = 0 #rectangle
#         self._spawn_position = self._world_view.get_size().x / 2, self._world_view.height - self._world_view.get_size().y / 2 #initial player coordinates
#         self._player = Player()
#
#         self._load_textures()
#         self._build_scene()
#         self._world_view.set_center(self._spawn_position)
#
#     def update(self, delta_time):
#         self._player.set_velocity(0, 0)
#
#         #Forward commands to scene graph, adapt velocity (scrolling, diagonal correction)
#         while not self._command_queue.is_empty():
#             self._scene_graph.on_command(self._command_queue.pop(), delta_time)
#
#         self._adapt_player_velocity()
#
#         #Regular update step, adapt position (correct if outside view)
#         self._scene_graph.update(delta_time)
#         self._adapt_player_velocity()
#
#     def draw(self):
#         self._window.set_view(self._world_view)
#         self._window.draw(self._scene_graph)
#
#     def get_command_queue(self):
#         return self._command_queue
#
#     def _load_textures(self):
#         self._textures.load(Texture.BACKGROUND, "Resources/Textures/Background/bluerock.jpg")
#         self._textures.load(Texture.PLAYER, "Resources/Textures/Units/player.png")
#         self._textures.load(Texture.ZOMBIE, "Resources/Textures/Units/zombie.png")
#
#     def _build_scene(self):
#
#         # Initialize the different layers
#         for layer in Layer:
#             layer = SceneNode()
#             self._scene_layers.add(layer)
#             self._scene_graph.attach_child(layer)
#
#         # Prepare the tiled background
#         texture = self._textures.get(Texture.BACKGROUND)
#         texture_rect = Rectangle(self._world_bounds)
#         texture.set_repeated(True) #library
#
#         # Add the background sprite to the scene
#         background_sprite = SpriteNode(texture, texture_rect) #SpriteNode is ours
#         background_sprite.setPosition(self._world_bounds.left, self._world_bounds.top)
#         self._scene_layers[Layer.BACKGROUND].attachChild(background_sprite)
#
#         # Add player
#         player = Player(_textures)
#         _player = player.get()
#         _player.set_position(self._spawn_position)
#         self._scene_layers[Layer.UNITS].attach_child(player)
#
#     def _adapt_player_position(self):
#         # Keep player's position inside the screen bounds, at least borderDistance units from the border
#
#         view_bounds = (self._world_view.get_enter() - self._world_view.get_size() / 2.0, self._world_view.get_size()) # float rectangle
#         border_distance = 40
#
#         position = self._player.get_position() #vector
#         position.x = max(position.x, view_bounds.left + border_distance)
#         position.x = min(position.x, view_bounds.left + view_bounds.width - border_distance)
#         position.y = max(position.y, view_bounds.top + border_distance)
#         position.y = min(position.y, view_bounds.top + view_bounds.height - border_distance)
#
#         self._player.set_position(position)
#
#     def _adapt_player_velocity(self):
#         velocity = self._player.get_velocity() # vector
#
#         # If moving diagonally, reduce velocity (to have always same velocity)
#         if velocity.x != 0 and velocity.y != 0:
#             self._player.set_velocity(velocity / math.sqrt(2))