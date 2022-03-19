# Creating a Pygame window & Responding to user's Input

import sys  # sys module exits game - when user want to quit

import pygame  # pygame contains functionality -we need to make an game



class AlienInvasion:
    """overall class to manage game Assets & Behaviors"""

    def __init__(self):
        """initialize the game & create game Resources """

        pygame.init()
        """ fn - initializes the background settings of pygame """

        self.screen = pygame.display.set_mode((1200, 800))
        # create a blank display window of size...pixels X pixels
        # called " SURFACE " in pygame

        pygame.display.set_caption("Alien Invasion")
        # making a caption on the display

    def run_game(self):
        """controller of game - main loop of game starts here """

        while True:
            # looks for continuous changes on Screen.
            #  watch for keyboard & mouse events - that'll  cause screen Updates.

            for event in pygame.event.get():
                """ Event loop - checks for all the (actions) / events occurs """
                """ & make a list of such events """
                if event.type == pygame.QUIT:
                    # when player click to close pygame's window
                    # then Pygame.QUIT event is detected &
                    # we call sys.exit()- to exit the game
                    sys.exit()

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
