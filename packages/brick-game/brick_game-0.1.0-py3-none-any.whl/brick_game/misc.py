"""
Created on Nov 27 00:00:00 2021
"""

import os
import sys

import pygame

try:
    import global_variables as gv
except ImportError:
    from . import global_variables as gv

_path = os.path.dirname(__file__)

score_path = os.path.join(_path, 'high_score')
font_path = os.path.join(_path, 'Font')


def enemy_player_collision(enemy, player):
    name_ = enemy.type_
    enemy, player = enemy.body, player.body

    if name_ in ['type1', 'type4']:
        if enemy[-1].x == player[2].x and enemy[-1].y >= player[2].y:
            return 0
    elif name_ in ['type2', 'type3']:
        if enemy[-1].x == player[2].x or enemy[-4].x == player[2].x:
            if enemy[-1].y >= player[2].y:
                return 0


def key_press(event, player):
    if event.key == pygame.K_ESCAPE:
        pygame.quit(), sys.exit()
    elif event.key in [pygame.K_LEFT, pygame.K_a] and player.body[0].x != 1:
        player.direction_vector = V(-5, 0)
        player.move_player()
    elif event.key in [pygame.K_RIGHT, pygame.K_d] and player.body[0].x != 11:
        player.direction_vector = V(5, 0)
        player.move_player()


def display_text(font_size, text_to_display, text_color, pos_x, pos_y, display_position):
    font = pygame.font.Font(f'{font_path}/inconsolata.ttf', font_size)

    surface_ = font.render(str(text_to_display), True, pygame.Color(text_color))
    x_, y_ = int(pos_x), int(pos_y)

    rect_ = surface_.get_rect(
            center=(x_, y_)) if display_position == 'center' else surface_.get_rect(
            topright=(x_, y_))

    gv.screen.blit(surface_, rect_)


def show_game_over_screen(game_over, first_time):
    display_screen_text('WELCOME!', 'gray') if first_time else display_screen_text(
            'GAME OVER!', 'black')

    pygame.display.flip()

    while game_over:
        gv.clock.tick(60)
        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.K_ESCAPE]:
                pygame.quit(), sys.exit()
            elif event.type == pygame.KEYDOWN:
                if first_time:
                    if event.key == pygame.K_SPACE:
                        game_over, first_time = False, False
                else:
                    if event.key in [pygame.K_r, pygame.K_SPACE]:
                        game_over, first_time = False, False

    return game_over, first_time


def display_screen_text(big_text, color):
    gv.screen.fill(pygame.Color(color))
    display_text(font_size=72,
                 text_to_display=big_text,
                 text_color='red',
                 pos_x=gv.resolution / 4.5,
                 pos_y=gv.resolution / 8,
                 display_position='center')
    display_text(font_size=18,
                 text_to_display='Press the Space-bar key to start the game',
                 text_color='red',
                 pos_x=gv.resolution / 4.5,
                 pos_y=gv.resolution / 6,
                 display_position='center')
    display_text(font_size=18,
                 text_to_display='Press Left/Right arrow keys or A/D to move',
                 text_color='red',
                 pos_x=gv.resolution / 4.5,
                 pos_y=gv.resolution / 4,
                 display_position='center')
    display_text(font_size=22,
                 text_to_display='Press [Alt+F4] to quit',
                 text_color='red',
                 pos_x=gv.resolution / 4.5,
                 pos_y=gv.resolution / 2,
                 display_position='center')


def displaying_score(score=None, score_list=None):
    if score is not None:
        display_text(font_size=24,
                     text_to_display='CURRENT SCORE',
                     text_color='green',
                     pos_x=gv.width,
                     pos_y=50,
                     display_position='topright')

        display_text(font_size=32,
                     text_to_display=sum(score),
                     text_color='blue',
                     pos_x=gv.width,
                     pos_y=70,
                     display_position='topright')

    if score_list is not None:
        display_text(font_size=24,
                     text_to_display='Top 20 scores',
                     text_color='green',
                     pos_x=gv.resolution / 2.25,
                     pos_y=110,
                     display_position='topright')

        recent_ = sorted(score_list)[::-1][0:20]

        incr_ = 0

        for recent in recent_:
            display_text(font_size=24,
                         text_to_display=int(recent),
                         text_color='green',
                         pos_x=gv.width,
                         pos_y=135 + incr_,
                         display_position='topright')

            incr_ += 25


def getting_current_score(enemy):
    if enemy.type_ == 'type1':
        return 10
    elif enemy.type_ in ['type2', 'type3']:
        return 20
    else:
        return 25


def saving_score(score):
    high_score_file = open(f'{score_path}/high_score_file.txt', 'a')
    high_score_file.write(str(sum(score)) + '\n')
    high_score_file.close()


def displaying_high_score():
    try:
        read_high_score_file = open(f'{score_path}/high_score_file.txt', 'r')
        num_list = [float(num) for num in read_high_score_file.read().split()]
        max_val = max(num_list)
    except FileNotFoundError:
        try:
            os.mkdir(f'{_path}/high_score')
        except FileExistsError:
            pass
        open(f'{score_path}/high_score_file.txt', 'w').close()
        max_val = 0
    except ValueError:
        max_val = 0

    try:
        displaying_score(score_list=num_list)
    except UnboundLocalError:
        pass

    display_text(font_size=24,
                 text_to_display='HIGH SCORE',
                 text_color='green',
                 pos_x=gv.resolution / 2.25,
                 pos_y=0,
                 display_position='topright')

    display_text(font_size=32,
                 text_to_display=int(max_val),
                 text_color='green',
                 pos_x=gv.resolution / 2.25,
                 pos_y=20,
                 display_position='topright')


def V(x, y):
    return pygame.Vector2(x, y)
