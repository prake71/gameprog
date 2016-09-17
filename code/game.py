# This is the Game class, the bracket for everything from starships over bullets
# to enemies
# filename: game.py

from modehandler import *

class Game():
    """ Game Class """

    def __init__(self, screen, fps=60):
        """ Constructor """
        # technical variables
        self.screen = screen
        self.framerate = fps
        self.scr_w = screen.get_width()
        self.scr_h = screen.get_height()
        self.mode = None
        # logical variables (Level Handling, Game Mode Handling)
        startmode = AttractMode(self.screen, self, "Welcome!")
        self.enter_mode(startmode)


    def process_events(self):
        # processing events
        done = self.mode.process_events()
        return done

    def run_logic(self):
        """ run game logic """
        self.mode.run_logic()

    def display_frame(self):
        """ draw all objects on screen """
        self.mode.display_frame()


    def enter_mode(self, new_mode):
        if self.mode:
            print ("Exiting mode: ", self.mode.name)
            self.mode.exit()
        self.mode = new_mode
        print ("Entering mode: ", self.mode.name)
        self.mode.enter()