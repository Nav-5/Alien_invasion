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
from time import sleep
# to give pause for a moment -when alien-ship hits
from game_stats import GameStats
# importing game_stats class
from button import Button
# importing button class
from scoreboard import Scoreboard
# importing Scoreboard class

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

        self.stats = GameStats(self)
        # instance of GameStats class- to store game statistics
        self.sb = Scoreboard(self)
        # creating an scoreboard

        self.play_button = Button(self, "Play")
        # Make the play button




    def run_game(self):

        while True:

            self._check_events()   #1
            """This will simplify run_game & isolate the event mngmt loop """

            if self.stats.game_active:
                # identifying which part should run & when
                # the Game should Freeze when You used up all the Aliens = 3
                # i.e. max collision of Alien-Ship allowed is 3
                self.ship.update()
                # real time update method of ship -it can calls throughout the program
                self._update_bullets()
                # checks for bullets fired & update in real time
                self._update_aliens()
                # call to update aliens position

            self._update_screen()  # 2



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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        """detects collisions between aliens & bullets & respond accordingly """
        """ if so ,get rid of bullet & aliens """
        # when 'rects' of alien & bullet overlaps each other - collision
        # then groupcollide() maintains a dictionary of key(bullet) - value(alien) pairs
        # 2 True - tells Pygame to delete bullets & aliens that collided
        # Super bullet- that not destroyed after collision - make 1st arg FALSE

        if collisions:

            for aliens in collisions.values():

                self.stats.score = self.stats.score + self.SETTings.alien_points * len(aliens)

            self.sb.prep_score()
            # updated score
            self.sb.check_high_score()


        if not self.aliens:
            """Destroy existing aliens & create new fleet"""
            self.bullets.empty()
            # check whether alien group is empty or not
            # if empty then call to _create_fleet() method- to create a new fleet
            self._create_fleet()

            self.SETTings.increase_speed()
            # instance to settings's increase_speed method

            # Increase level- if fleet is destroyed
            self.stats.level = self.stats.level + 1
            self.sb.prep_level()

    def _update_aliens(self):
        """update positions of all aliens in fleet"""
        self._check_fleet_edges()
        # check if the fleet at an edge ,
        # then update the positions of all aliens in the fleet

        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship , self.aliens):
            self._ship_hit()
            """Look for alien - ship collision"""
            # print("Ship hit !!!")

        self._check_aliens_bottom()
        # look for any alien hit the bottom



    def _ship_hit(self):
        """Respond to ship being hit by an alien"""
        if self.stats.ships_left > 0 :

            self.stats.ships_left = self.stats.ships_left - 1
            # Decrement the no. of ship_left & Update Scoreboard
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()
            # get rid of any remaining bullets & aliens
            self._create_fleet()
            self.ship.center_ship()
            # create a new fleet & center the ship
            sleep(0.5)
             # Pause
        else:
            self.stats.game_active = False
            # when player used up all their ships - FALSE
            pygame.mouse.set_visible(True)
            # make Start button visible -after game has stopped


    def _check_aliens_bottom(self):
        """check if any alien have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # then treat this as a ship hit
                self._ship_hit()
                break






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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # checks for Mouse clicks &
                mouse_pos = pygame.mouse.get_pos()
                # get the position of mouse clicks
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:

            self.SETTings.initialize_dynamic_settings()
            # Reset the game settings after Restarting the game

            self.stats.reset_stats()
            # Reset  game statistics
            self.stats.game_active = True

            self.sb.prep_score()
            # Reseting the game score

            self.sb.prep_level()
            # updates level images

            self.sb.prep_ships()

            # Get rid of any remaining aliens & bullets
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet & center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor
            pygame.mouse.set_visible(False)





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

    def _check_fleet_edges(self):
        """Respond appropriately if any alien reaches at any edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet & change the fleet's direction """
        for alien in self.aliens.sprites():

            alien.rect.y = alien.rect.y + self.SETTings.fleet_drop_speed

        self.SETTings.fleet_direction *= -1


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

        # Draw the play Button -if the game is INACTIVE

        self.sb.show_score()
        # draw the score information

        if not self.stats.game_active:
            self.play_button.draw_button()

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


