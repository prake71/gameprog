# modehandler.py

"""
AttractMode -> HiScoreListMode
            -> PlayMode          -> GameOverMode -> HiScoreInputMode -> HiScoreListMode -> AttractMode
                                                 -> AttractMode

"""

from attractmode import *
from playmode import *

class ModeHandler:

    def __init__(self, screen, initial_mode):
        # create list of Game Modes
        self.gmlist = [AttractMode(screen, "AttractMode"), PlayMode(screen, "PlayMode")]
        self.gm_current = self.gmlist[initial_mode]
        self.gm_current.enter(self.gmlist[initial_mode].message)


    def process_modes(self):
        pass

    def get_active_mode(self):
        return self.gm_current


