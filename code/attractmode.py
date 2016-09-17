# attractmode.py
# i am the entry game state which should motivate the user to
# play this amazing game

from gamemode import *
from playmode import *

class AttractMode(GameMode):
    """ I am the first attractive part of the game to motivate the
    user to play this amazing game """

    def __init__(self, screen, game, message="AttractMode"):
        super().__init__(screen, game, message)
        self.name = "AttractMode"


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    play_mode = PlayMode(self.screen, self.game, "Play!!!")
                    self.game.enter_mode(play_mode)
        return False

    def run_logic(self):
        pass



