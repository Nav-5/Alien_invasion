# bullets will disappear when they reach at the top of screen
# but actually the bullets exists in background- slowdown the process of game
# & continuously consumes the memory & system resources

# when bottom value of a bullet's 'rect' = 0
# shows that bullet has passed off the Top of screen
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
from bullet import Bullet
# importing Bullet class
from ALIEN import Alien
# importing alien class

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

        self.aliens = pygame.sprite.Group()
        # group to hold fleet of aliens
        self._create_fleet()


    def run_game(self):

        while True:

            self._check_events()   #1
            """This will simplify run_game & isolate the event mngmt loop """
            self._update_screen()  #2

            self.ship.update()
            # real time update method of ship -it can calls throughout the program

            self._update_bullets()
            # checks for bullets fired & update in real time

            self._update_aliens()
            # call to update aliens position

    def _update_bullets(self): #3
        """to make AlienInvasion class well organized """

        self.bullets.update()
        # update each bullet fired

        for bullet in self.bullets.copy():
            # copy() method enable us to modify bullets inside loop
            # check for each bullet
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                """removing bullets that have disappeared"""
        print(len(self.bullets))
        # how many bullets currently exist in game

    def _update_aliens(self):
        """update positions of all aliens in fleet"""
        self.aliens.update()




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

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            # when spacebar is pressed
            # then fire the bullets

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a new bullet & add it to bullets group"""
        if len(self.bullets) < self.SETTings.bullets_allowed :
        #compare len of bullets available on screen to the no.of bullets allowed
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # add() method is similar to append() method

    def _create_fleet(self):
        """create the fleet of aliens"""
        alien = Alien(self)
        # making an alien
        alien_width, alien_height = alien.rect.size
        available_space_x = self.SETTings.screen_width - (2 * alien_width)
        """spacing between each alien is = 1 alien width + 1 width for empty space to its right = (2*alien_width)"""
        number_aliens_x = available_space_x // (2 * alien_width)
        """ find the number of aliens in a row """

        ship_height = self.ship.rect.height
        available_space_y = ( self.SETTings.screen_height - (3 * alien_height) - ship_height )
        number_rows = available_space_y // (2 * alien_height)
        """determine no. of rows of aliens that fit on the screen"""

        # create full fleet of aliens
        for row_number in range(number_rows):
            """count from 0 to no.of rows we want"""
            for alien_number in range(number_aliens_x):
                # create the 1st row of aliens
                self._create_alien(alien_number, row_number)
                # creating a new helper method -refactoring

    def _create_alien(self, alien_number, row_number):
        # create an alien & put it in the Row
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size

        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        """When alien is not in the 1st row -then update its Y-coordinate's value"""

        self.aliens.add(alien)
        # storing the alien into self.aliens group
        # Refactoring -allows us to add new rows & create an entire fleet






    def _update_screen(self): #2
        """update images on screen & flip to the new screen """

        self.screen.fill(self.SETTings.bg_color)
        """ 2. Redraw the screen during each pass """
        """ fill the screen with self.bg_color () """

        self.ship.blitme()
        # draw the ship on Middle-Bottom screen

        for bullet in self.bullets.sprites():
            # draw all fired bullets to screen
            # we loop through sprites in bullets
            bullet.draw_bullet()
            # & call draw_bullet on each one

        self.aliens.draw(self.screen)
        # draws each element to position defined by its 'rect' attribute
        # draw()-needs an argument - to declare a surface on which elements are drawn

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


