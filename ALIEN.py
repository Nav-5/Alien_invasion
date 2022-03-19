# Placing a Alien on screen is same as placing a ship
# Creating the Alien Class

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent single alien in fleet"""

    def __init__(self, ai_game):
        """initialize class & set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.SETTings = ai_game.SETTings

        self.image = pygame.image.load('images/alien.bmp')
        # load the alien image
        self.rect = self.image.get_rect()
        # setting rectangular Coordinates of image

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # start each new alien -near the top left of the screen

        self.x = float(self.rect.x)
        # store alien's exact horizontal position

    def check_edges(self):
        """checks if alien at any of the edge or not"""
        """If alien is at any edge - return TRUE"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien to the right"""
        self.x = ( self.x + self.SETTings.alien_speed * self.SETTings.fleet_direction )
        # move alien right with alien_speed = 1.0
        self.rect.x = self.x

