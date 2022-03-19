# Refactoring - simplifies the structure of the code -written before
# run_game() method is breaked into 2 helper methods
# because it's getting very lengthy-to handle complete code
# 1.   _check_events()- a single leading underscore both sides shows an helper method
# 2.   _update_screen()
""" we'll Move the code that manages the Events to _check_events() method """
import sys  # sys module exits game - when user want to quit

import pygame  # pygame contains functionality -we need to make an game

from SETTings import Setting
"""importing Setting  class from SETTings.py module 
                                & we have to create an instance of this in main  class"""
from SHIP import Ship
# importing Ship class

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

            self._check_events()   #1
            """This will simplify run_game & isolate the event mngmt loop """
            self._update_screen()  #2

    def _check_events(self): #1
        """ Respond to all Keypresses & Mouse Events """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                sys.exit()

    def _update_screen(self): #2
        """update images on screen & flip to the new screen """

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
