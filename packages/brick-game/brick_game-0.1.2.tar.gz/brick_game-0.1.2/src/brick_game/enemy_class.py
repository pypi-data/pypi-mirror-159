"""
Created on Nov 25 00:00:00 2021
"""

import random

import pygame

try:
    import global_variables as gv
    from misc import V
except ImportError:
    from . import global_variables as gv
    from .misc import V

wall_right = [V(0, blocks) for blocks in range(gv.cell_number)]
wall_left = [V(16, blocks) for blocks in range(gv.cell_number)]


def spawn_position_type1():
    rand_ = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

    return 1 if rand_ in [1, 4, 7] else 6 if rand_ in [2, 5, 8] else 11


def spawn_position_type2():
    rand_ = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    return 1 if rand_ % 2 == 0 else 6


class WALL:

    def __init__(self):
        self.type_ = 'wall'
        self.wall_left = wall_left
        self.wall_right = wall_right

    def draw_wall(self):
        for block in self.wall_left:
            wall_left_x = int(block.x * gv.cell_size)
            wall_left_y = int(block.y * gv.cell_size)
            wall_left_rect = pygame.Rect(wall_left_x, wall_left_y, gv.cell_size,
                                         gv.cell_size)
            pygame.draw.rect(gv.screen, pygame.Color('red'), wall_left_rect)

        for block in self.wall_right:
            wall_right_x = int(block.x * gv.cell_size)
            wall_right_y = int(block.y * gv.cell_size)
            wall_right_rect = pygame.Rect(wall_right_x, wall_right_y, gv.cell_size,
                                          gv.cell_size)
            pygame.draw.rect(gv.screen, pygame.Color('red'), wall_right_rect)


class EnemyType1:

    def __init__(self):
        pos = spawn_position_type2()

        self.type_ = 'type1'
        self.body = [V(pos + 0, -6), V(pos + 2, -6), V(pos + 4, -6),
                     V(pos + 1, -5), V(pos + 2, -5), V(pos + 3, -5),
                     V(pos + 2, -4),
                     V(pos + 1, -3), V(pos + 2, -3), V(pos + 3, -3),
                     V(pos + 0, -2), V(pos + 2, -2), V(pos + 4, -2)]

        self.direction_vector = V(0, 1.5 if random.choice([0, 1, 2, 3, 4]) == 2 else 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x * gv.cell_size)
            enemy_y_pos = int(block.y * gv.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, gv.cell_size, gv.cell_size)
            pygame.draw.rect(gv.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class EnemyType2:

    def __init__(self):
        pos = spawn_position_type2()

        self.type_ = 'type2'
        self.body = [V(pos + 0, -6), V(pos + 2, -6), V(pos + 4, -6),
                     V(pos + 5, -6), V(pos + 7, -6), V(pos + 9, -6),
                     V(pos + 1, -5), V(pos + 2, -5), V(pos + 3, -5),
                     V(pos + 6, -5), V(pos + 7, -5), V(pos + 8, -5),
                     V(pos + 2, -4), V(pos + 7, -4),
                     V(pos + 1, -3), V(pos + 2, -3), V(pos + 3, -3),
                     V(pos + 6, -3), V(pos + 7, -3), V(pos + 8, -3),
                     V(pos + 0, -2), V(pos + 2, -2), V(pos + 4, -2),
                     V(pos + 5, -2), V(pos + 7, -2), V(pos + 9, -2)]

        self.direction_vector = V(0, 1.5 if random.choice([0, 1, 2, 3, 4]) == 2 else 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x * gv.cell_size)
            enemy_y_pos = int(block.y * gv.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, gv.cell_size,
                                     gv.cell_size)
            pygame.draw.rect(gv.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class EnemyType3:

    def __init__(self):
        self.type_ = 'type3'
        self.body = [V(1, -6), V(3, -6), V(5, -6), V(11, -6), V(13, -6), V(15, -6),
                     V(2, -5), V(3, -5), V(4, -5), V(12, -5), V(13, -5), V(14, -5),
                     V(3, -4), V(13, -4),
                     V(2, -3), V(3, -3), V(4, -3), V(12, -3), V(13, -3), V(14, -3),
                     V(1, -2), V(3, -2), V(5, -2), V(11, -2), V(13, -2), V(15, -2)]

        self.direction_vector = V(0, 1.5 if random.choice([0, 1, 2, 3, 4]) == 2 else 1)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x * gv.cell_size)
            enemy_y_pos = int(block.y * gv.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, gv.cell_size, gv.cell_size)
            pygame.draw.rect(gv.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        for block in self.body:
            block += self.direction_vector


class EnemyType4:

    def __init__(self):
        pos = spawn_position_type1()

        self.type_ = 'type4'
        self.body = [V(pos + 0, -6), V(pos + 2, -6), V(pos + 4, -6),
                     V(pos + 1, -5), V(pos + 2, -5), V(pos + 3, -5),
                     V(pos + 1, -4), V(pos + 2, -4), V(pos + 3, -4),
                     V(pos + 1, -3), V(pos + 2, -3), V(pos + 3, -3),
                     V(pos + 0, -2), V(pos + 2, -2), V(pos + 4, -2)]

        y_speed = 2 if random.choice([0, 1, 2, 3, 4]) == 2 else 1

        self.move_down = V(0, y_speed)
        self.move_down_right = V(5, y_speed)
        self.move_down_left = V(-5, y_speed)

    def draw_enemy(self):
        for block in self.body:
            enemy_x_pos = int(block.x * gv.cell_size)
            enemy_y_pos = int(block.y * gv.cell_size)
            enemy_rect = pygame.Rect(enemy_x_pos, enemy_y_pos, gv.cell_size, gv.cell_size)
            pygame.draw.rect(gv.screen, pygame.Color('red'), enemy_rect)

    def move_enemy(self):
        move_pos_array = [2, 7, 12, 17]
        for body1 in self.body:
            body1 += self.move_down
            if body1.y in move_pos_array:
                if body1.x == 1:
                    for body2 in self.body:
                        body2 += self.move_down_right
                elif body1.x == 6:
                    rand_int = random.randint(0, 10)
                    if rand_int % 2 == 0:
                        for body2 in self.body:
                            body2 += self.move_down_left
                    else:
                        for body2 in self.body:
                            body2 += self.move_down_right
                elif body1.x == 11:
                    for body3 in self.body:
                        body3 += self.move_down_left


def pick_enemy_type():
    rand_ = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    if rand_ in [1, 5, 9]:
        return EnemyType1()
    elif rand_ in [2, 6, 10]:
        return EnemyType2()
    elif rand_ in [3, 7, 11]:
        return EnemyType3()
    else:
        return EnemyType4()
