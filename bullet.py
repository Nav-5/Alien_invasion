# Bullet class inherits from Sprite class - pygame.sprite module
# Sprite -can group related elements &act on all elements at once
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """create a bullet object at ship's current position"""
        super().__init__()
        # super() method inherits property from sprite
        self.screen = ai_game.screen
        self.SETTings = ai_game.SETTings
        self.color = self.SETTings.bullet_color

        self.rect = pygame.Rect(0,0,self.SETTings.bullet_width,self.SETTings.bullet_height)
        #pygame.Rect() class -need X , y co-ord. & bullet's width + height
        self.rect.midtop = ai_game.ship.rect.midtop
        # Match the bullet's midtop attribute to ship's midtop
        # this make bullet emerge from Top of the ship

        self.y = float(self.rect.y)
        # store bullet's Y - Coordinates as a decimal value
        # to make fine adjustment to bullet's speed

    def update(self):
        """manages bullet's position -when bullet is fired
        it moves up the screen & decreasing the Y-Coord. value"""
        self.y = self.y - self.SETTings.bullet_speed
        # update decimal position of bullet
        self.rect.y = self.y
        # set value self.rect.y equal to self.y

    def draw_bullet(self):
        """Draw the bullet's on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        # draw.rect() method- fills the screen defined by bullet's rect
        # with the color stored in self.color
