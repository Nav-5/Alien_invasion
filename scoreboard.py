# To display the current score, remaining ships, high score , Level of games

import pygame.font

from pygame.sprite import Group

from SHIP import Ship

class Scoreboard:
    """A class to report scoring information"""
    def __init__(self, ai_game):
        # initializing score keeping attributes
        self.ai_game = ai_game

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.SETTings = ai_game.SETTings
        self.stats = ai_game.stats

        # Font settings for scoring information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()

        self.prep_high_score()

        self.prep_level()
        # to display the current level

        self.prep_ships()


    def prep_score(self):
        """Turn the score into an rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        # insert commas between numbers - when converted to strings
        self.score_image = self.font.render(score_str, True, self.text_color, self.SETTings.bg_color)

        # display the score at right edge of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into an rendered image"""
        high_score = round(self.stats.high_score, -1)
        # rounding high score ~ 10
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.SETTings.bg_color)

        # Center the high score at Top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw scores , levels & Ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)

        self.screen.blit(self.high_score_image, self.high_score_rect)

        self.screen.blit(self.level_image, self.level_rect)

        self.ships.draw(self.screen)

    def check_high_score(self):
        """check to see if there is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into an rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.SETTings.bg_color)

        #Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """show how many ships are left"""
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

