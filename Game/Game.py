__author__ = 'Yani Maltsev'

from Game.Player import Player


import time

# class Game:
#     def __init__(self):
#         self.time_per_frame = 1 / 60
#         self._window = Window() # from library
#         self._world = World(self._window) # from library
#         self._player = Player() # desc of Unit
#
#     def run(self):
#         elapsed_time = time.time()
#         time_since_last_update = 0
#         while self._window.is_open():
#             elapsed_time = time.time() - elapsed_time
#             time_since_last_update += elapsed_time
#             while time_since_last_update > self.time_per_frame:
#                 time_since_last_update -= self.time_per_frame
#                 self._process_input()
#                 self._update(self.time_per_frame)
#             self._render()
#
#     def _process_input(self):
#         commands = self._world.get_command_queue()
#         event = 0 # from library
#         while self._window.poll_event(event):
#             self._player.handle_event(event, commands)
#             if event.type == "Closed":
#                 self._window.close()
#         self._player.handle_realtime_input(commands)
#
#     def _update(self, elapsed_time):
#         self._world.update(elapsed_time)

    # def _render(self):
    #     self._window.clear()
    #     self._world.draw()
    #     self._window.set_view(self._window.get_default_view())
    #     self._window.display()