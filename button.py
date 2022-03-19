# in this ,we'll add a Play button
# that Appears before a game begins & reappears after game ends
# so the player can play again
# & game should start in an Inactive state

import pygame.font
#lets pygame to render text on the screen

class Button:
    """create a filled rectangle with a label"""
    def __init__(self, ai_game, msg):
        # initialize attributes of  button class
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions & properties of the Button
        self.width, self.height = 200, 50
        self.button_color = ( 0 , 255 , 0 ) # green -RGB
        self.text_color = ( 255, 255, 255 ) # white
        self.font = pygame.font.SysFont(None, 48)  # NOne -default font


        # Build button's rect attribute & center it
        self.rect = pygame.Rect( 0, 0, self.width, self.height )
        self.rect.center = self.screen_rect.center

        # Button message needs to be prepared only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Pygame works with text -by rendering String as an Image """
        # Turn msg into rendered image & center text on the Button
        self.msg_image = self.font.render( msg, True, self.text_color, self.button_color )
        # True -antialiasing ON -makes text edges smoother
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw the blank button & then draw the message
        self.screen.fill(self.button_color, self.rect)
        # draw the rectangular portion of button
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # draw the text image to screen
