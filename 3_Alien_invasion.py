""""1. setting background color"""
# by default the screen is BLACK
"""2. Redraw the screen during each pass"""
# we have to make changes in MAIN_CLASS __init()__ method

import sys  # sys module exits game - when user want to quit

import pygame  # pygame contains functionality -we need to make an game

from SETTings import Setting
"""importing Setting  class from SETTings.py module 
                                & we have to create an instance of this in main  class"""
from SHIP import Ship
#importing Ship class

class AlienInvasion:
    """overall class to manage game Assets & Behaviors"""

    def __init__(self):
        """initialize the game & create game Resources """

        pygame.init()
        """ fn - initializes the background settings of pygame """

        self.SETTings = Setting()  # creating an instance of SETTings module-to call it throughout program

        self.screen = pygame.display.set_mode((self.SETTings.screen_width, self.SETTings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # creating instance of Ship class


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

            self.screen.fill(self.SETTings.bg_color)
            """ 2. Redraw the screen during each pass """
            """ fill the screen with self.bg_color () """

            self.ship.blitme()
            # draw the ship on Middle-Bottom screen

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
