# we have to load the image 1st & using BLIT() -method draw the image
# pygame loads .bmp files by default - with transparent / solid background
# image's bg_color should match with Game's bg
# download an image & save it in Your Project directory
# pygame treats each element as an RECTANGLE

"""creating an SHIP.py module to declare an Ship Class -
that stores the behaviors of player's ship """

import pygame
from pygame._sprite import Sprite

class Ship(Sprite):
    """ A class to manage the ship """

    def __init__(self, ai_game):
        """ initialize the ship & set its current position """
        # ai_game defined here-give ship access to all the alien_invasion resources
        super().__init__()

        self.screen = ai_game.screen

        self.SETTings = ai_game.SETTings
        """creating a SETTings attribute- to use in update() method"""

        self.screen_rect = ai_game.screen.get_rect()
        # getting the screen's rect attribute - to place ship in correct locn of the screen
        # get_rect() - is the method that done this


        self.image = pygame.image.load('images/ship.bmp')
        # loading the image
        self.rect = self.image.get_rect()
        # getting image's Rectangular Coordinates

        self.rect.midbottom = self.screen_rect.midbottom
        """ start each new ship from screen's middle of the bottom """

        self.x = float(self.rect.x)
        """store a decimal value for ship's horizontal position in attribute 'self.x' """

        self.moving_right = False
        """By default the flag is FALSE - we can update it using a separate method"""
        #1 movement flag - moving_right() is an attribute
        self.moving_left = False
        # left movement flag

    def update(self):
        """ update ship's position based on the movement flag """
        # update the ship's X value, not the rect

        if self.moving_right and self.rect.right < self.screen_rect.right:
            #checks ship's position before changing value of self.x
            # self.rect.right -return X-coordinates of right edge of ship's rect
            self.x = self.x + self.SETTings.ship_speed

        if self.moving_left and self.rect.left > 0:
            # left side of rect is > 0 -the ship has'nt reached the left edge of the screen
            # This ensures ship's within inbound to LR & stops moving beyond wall

            self.x = self.x - self.SETTings.ship_speed

        self.rect.x = self.x
        """ update rect object from self.x """


    def blitme(self):
        """ draw the ship image at position - defined by self.rect """

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        # center at the bottom
        self.x = float(self.rect.x)
        # self.x keeps track of ship's exact position