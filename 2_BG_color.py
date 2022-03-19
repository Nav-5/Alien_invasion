""""1. setting background color"""
# by default the screen is BLACK
"""2. Redraw the screen during each pass"""
# we have to make changes in MAIN_CLASS __init()__ method

import sys  # sys module exits game - when user want to quit

import pygame  # pygame contains functionality -we need to make an game

from SETTings import Setting

class AlienInvasion:
    """overall class to manage game Assets & Behaviors"""

    def __init__(self):
        """initialize the game & create game Resources """

        pygame.init()
        """ fn - initializes the background settings of pygame """

        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230)
        """ 1. setting background color - as RGB in pygame varies ( 0-255 )"""

    def run_game(self):

        while True:

            for event in pygame.event.get():
                """ Event loop - checks for all the (actions) / events occurs """
                """ & make a list of such events """
                if event.type == pygame.QUIT:
                    # when player click to close pygame's window
                    # then Pygame.QUIT event is detected &
                    # we call sys.exit()- to exit the game
                    sys.exit()

            self.screen.fill(self.bg_color)
            """ 2. Redraw the screen during each pass """
            """ fill the screen with self.bg_color () """

            pygame.display.flip()
            """make recently drawn screen visible"""
            """ erase the old screen & Continually Update the screen """


if __name__ == '__main__':
    # make a game instance & run the game
    # run_game runs only -if file is called directly

    ai = AlienInvasion()
    # class instantiation
    ai.run_game()
    # calling run_game method
