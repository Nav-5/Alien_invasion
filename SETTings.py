"""Each time we want new functions - &we have to declare separate Settings"""
# let's create Settings module -to access it throughout the program

class Setting:
    """ A class to store all settings for Alien_invasion """

    def __init__(self):
        # Initialize the game's settings
        # screen's  Settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)


        self.ship_speed = 1.5
        # ship settings - by default it's 1 pixel per cycle through the while loop
        # rect -attributes only store the int value of X

        self.ship_limit = 3
        # limits no.of ship at a given time

        """Adding Bullet settings"""
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        # these settings create dark grey bullets

        self.bullets_allowed = 3
        # bullets allowed at a time on screen
        #limits player to 3 bullets at a time

        self.alien_speed = 1.0
        # Alien setting

        """setting for fleet's movement from RIGHT edge to next LEFT corner & so on."""
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # fleet_direction 1 shows RIGHT & -1 shows LEFT

        """How quickly the game speeds up - after moving to next alien fleet"""
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

        self.score_scale = 1.5
        # How quickly the alien point values increase

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1
        # 1  RIGHT , -1 LEFT

        self.alien_points = 50
        # each time an alien shoot - returns 50 points on Scoreboard

    def increase_speed(self):
        """increase the speed settings"""
        self.ship_speed = self.ship_speed * self.speedup_scale
        self.bullet_speed = self.bullet_speed * self.speedup_scale
        self.alien_speed = self.alien_speed * self.speedup_scale

        self.alien_points = int( self.alien_points * self.score_scale )
        print(self.alien_points)
