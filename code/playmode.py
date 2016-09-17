# playmode.py
# i am the playmode where the actual game takes place.
# this mode is the most fun part of the game.
# all levels will be handled here somehow

import pygame
import gameovermode


class PlayMode(gameovermode.GameMode):
    """ I am the most fun making class called PlayMode. The
    actual gameplay takes places here """

    def __init__(self, screen, game, message="PlayMode"):
        super().__init__(screen, game, message)
        self.name = 'PlayMode'


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    gameover_mode = gameovermode.GameOverMode(self.screen, self.game, "Game Over, You Lost!!!")
                    self.game.enter_mode(gameover_mode)
        return False
