"""
Created on Nov 25 00:00:00 2021
"""

import sys

import pygame

try:
    import global_variables
    import misc
    from enemy_class import WALL, pick_enemy_type
    from player_class import Player
except ImportError:
    from . import global_variables
    from . import misc
    from .enemy_class import WALL, pick_enemy_type
    from .player_class import Player


def main():
    pygame.init()

    game_on, game_over, first_time = True, True, True

    while game_on:
        for event in pygame.event.get():
            if game_over:
                game_over, first_time = misc.show_game_over_screen(game_over=game_over,
                                                                   first_time=first_time)

                score = []
                player = Player()
                wall, enemy = WALL(), pick_enemy_type()

                SCREEN_UPDATE = pygame.USEREVENT
                pygame.time.set_timer(SCREEN_UPDATE, 35)

            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
            if event.type == SCREEN_UPDATE:
                enemy.move_enemy()
            if event.type == pygame.KEYDOWN:
                misc.key_press(event=event, player=player)
            if enemy.body[0].y > player.body[-1].y:
                score.append(misc.getting_current_score(enemy=enemy))
                enemy = pick_enemy_type()

                pygame.time.set_timer(SCREEN_UPDATE, 30) if enemy.type_ == 'type4' else \
                    pygame.time.set_timer(SCREEN_UPDATE, 20)

            result = misc.enemy_player_collision(enemy=enemy, player=player)
            if result == 0:
                misc.saving_score(score=score)
                game_over = True

        wall.draw_wall()
        enemy.draw_enemy()
        player.draw_player()
        misc.displaying_high_score()
        misc.displaying_score(score=score)

        pygame.display.update()
        global_variables.clock.tick(60)
        global_variables.screen.fill(pygame.Color('gray'))


if __name__ == '__main__':
    sys.exit(main())
