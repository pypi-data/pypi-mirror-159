"""
Created on Nov 25 00:00:00 2021
"""

import pygame

try:
    import global_variables as gv
    from misc import V
except ImportError:
    from . import global_variables as gv
    from .misc import V


class Player:

    def __init__(self):
        pos_ = int(gv.cell_number / gv.h_) - 1
        self.body = [V(1, pos_ - 4), V(3, pos_ - 4), V(5, pos_ - 4),
                     V(2, pos_ - 3), V(3, pos_ - 3), V(4, pos_ - 3),
                     V(3, pos_ - 2),
                     V(2, pos_ - 1), V(3, pos_ - 1), V(4, pos_ - 1),
                     V(1, pos_ - 0), V(3, pos_ - 0), V(5, pos_ - 0)]
        self.direction_vector = V(5, 0)

    def draw_player(self):
        for block in self.body:
            player_x = int(block.x * gv.cell_size)
            player_y = int(block.y * gv.cell_size)
            player_rect = pygame.Rect(player_x, player_y, gv.cell_size, gv.cell_size)
            pygame.draw.rect(gv.screen, pygame.Color('blue'), player_rect)

    def move_player(self):
        for block in self.body:
            block += self.direction_vector
