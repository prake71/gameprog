# gameovermode.py
# game over :-( i will appear if the player has lost all his
# lifes.

from gamemode import *
import attractmode

class GameOverMode(GameMode):
    """ The Game is over and the Game Over Screen appears. """

    def __init__(self, screen, game, message='Game Over!'):
        super().__init__(screen, game, message)
        self.name = "GameOverMode"

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    attract_mode = attractmode.AttractMode(self.screen, self.game, "Welcome!!! Be Attracted, Honey!!")
                    self.game.enter_mode(attract_mode)
        return False

