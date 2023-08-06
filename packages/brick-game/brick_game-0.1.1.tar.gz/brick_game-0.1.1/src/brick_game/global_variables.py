"""
Created on Nov 25 00:00:00 2021
"""

import pygame

cell_number, cell_size, h_ = 56, 20, 1.5
resolution = cell_number * cell_size
width, height = int(resolution / 2.25), int(resolution / h_)
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
