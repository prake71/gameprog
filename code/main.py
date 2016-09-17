# Yet Another Space Shooter
# file: main.py

import pygame
import game
from constants import *

def main():
    """  Yet Another Space Shooter (YASS)
    """

    # initialize pygame objects
    pygame.init()

    # setting game surface
    screen = pygame.display.set_mode([scr_w, scr_h])
    pygame.display.set_caption("Yet Another Space Shooter")

    # game ended by closing window
    done = False

    # clock object for limiting game speed
    clock = pygame.time.Clock()
    my_game = game.Game(screen, FPS)

    # game  loop start
    print ("Entering Game Loop!!!!")
    while not done:
        # handle events
        done = my_game.process_events()
        print(done)
        # do logic
        my_game.run_logic()

        # redraw screen
        my_game.display_frame()

        # pause for the next frame
        clock.tick(FPS)


    # game loop end

    # close window and quit
    pygame.quit()

if __name__ == '__main__': main()