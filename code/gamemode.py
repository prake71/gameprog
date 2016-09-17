# file: gamemode.py

from constants import *
import pygame

class GameMode:
    """ This is the GameMode class where other, more specialized
    classes, can be derived from """

    def __init__(self, screen, game, message="GameMode"):
        self.name = None
        self.message = message
        self.game = game
        # getting screen properties
        self.screen = screen
        self.scr_w = screen.get_width()
        self.scr_h = screen.get_height()
        # select the font to use
        self.font = pygame.font.SysFont("impact", 20, True, False)
        self.text = self.font.render(str(message), True, WHITE)
        self.bg_colour = BLACK
        self.textheight = self.text.get_height()
        self.textwidth = self.text.get_width()
        self.active = False # mode active or not

    def enter(self):
        """ invoked when the game enters the mode """
        self.active = True # mode active now

    def exit(self):
        self.active = False # mode inactive

    def process_events(self):
        """ process all events. Returns true if window has to be closed """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if self.active:
                        self.active = False
                    else:
                        self.active = True
                    print (self.active)
        return False

    def run_logic(self):
        """ game logic handling, invoked each frame """
        if self.active == False:
            self.bg_colour = WHITE
        else:
            self.bg_colour = BLACK

    def display_frame(self):
        """ redraw screen """
        self.screen.fill(self.bg_colour)
        # draw text centered on screen
        self.screen.blit(self.text, [(self.scr_w - self.textwidth) // 2, (self.scr_h - self.textheight) // 2])
        pygame.display.flip()
