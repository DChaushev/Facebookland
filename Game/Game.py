__author__ = 'Yani Maltsev'

SCREEN_WIDTH  = 200
SCREEN_HEIGHT = 200
BG_COLOR = 150, 150, 80

import pygame
from Game.Global import textureHolder
from Game.Texture import Texture

from Game.Player import Player

class Game:
    def __init__(self):
        self.player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT/2, textureHolder, Texture.PLAYER  )
        self.monsters = []
        self.projectiles = []
        #self.environment = []

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ), 0, 32)
        clock = pygame.time.Clock()
        while True:
            # Limit frame speed to 50 FPS
            time_passed = clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return#exit_game()
                elif event.type == pygame.K_UP:
                    self.player.set_direction( pygame.math.Vector2( 0 , -1 ) )
                elif event.type == pygame.K_DOWN:
                    self.player.set_direction( pygame.math.Vector2( 0, +1 ) )
                elif event.type == pygame.K_LEFT:
                    self.player.set_direction( pygame.math.Vector2( -1, 0 ) )
                elif event.type == pygame.K_RIGHT:
                    self.player.set_direction( pygame.math.Vector2( +1, 0 ) )

                self.player.move()

            # Redraw the background
            screen.fill(BG_COLOR)

            # Update and redraw all creeps
            for player in self.players:
                player.update()
                player.render()

            for monster in self.monstes:
                monster.update()
                monster.render()

            for projectile in self.projectiles:
                projectile.update()
                projectile.render()

            pygame.display.flip()

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
#
#     def _render(self):
#         self._window.clear()
#         self._world.draw()
#         self._window.set_view(self._window.get_default_view())
#         self._window.display()