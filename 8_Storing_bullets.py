# we'll give the ability to player to move ship L or R
# 1st build movement to Right side , then same for left
""" Responding to a Keypress """
# each keypress is picked -up by pygame.event.get()-method
# we need to specify _check_events() method - & declare the events we want the game to check for .
# Each keypress is registered as a KEYDOWN event

# when pygame detects a KEYDOWN- we need to check whether the Key pressed is that one
# that triggers an action

# eg. if player presses an RIGHT ARROW key -
# we want to increase ship's "rect.X" value to move ship to the Right

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

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # fullscreen display mode
        self.SETTings.screen_width = self.screen.get_rect().width
        self.SETTings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # creating instance of Ship class

        self.bullets = pygame.sprite.Group()
        """pygame.sprite.Group() -class to manage all live bullets &fired bullets
        This class acts as an LIST & helps to Update bullets on each pass """


    def run_game(self):

        while True:

            self._check_events()   #1
            """This will simplify run_game & isolate the event mngmt loop """
            self._update_screen()  #2

            self.ship.update()
            # real time update method of ship -it can calls throughout the program

            self.bullets.update()
            # update each bullet fired

    def _check_events(self): #1
        """ Respond to all Keypresses & Mouse Events """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            # making 2 helper methods to Refactor _check_events
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            # Moves the ship to the Right

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            # Moves ship to Left

        elif event.key == pygame.K_q:
            # if Q is pressed than QUIT
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


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
