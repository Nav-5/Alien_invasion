
class GameStats:
    """Track statistics for alien invasion"""

    def __init__(self, ai_game):
        # initialize statistics
        self.SETTings = ai_game.SETTings
        self.reset_stats()

        self.game_active = False
        # start alien invasion in an active state

        self.high_score = 0
        # high score should never be reset

        self.level = 1

    def reset_stats(self):
        """initialize stats that can change during the game"""
        self.ships_left = self.SETTings.ship_limit
        self.score = 0
        # to reset score each time new game start- declare score in reset_stats
        # rather than the __init__ 
