# Relationships: 
# Game = can have multiple players, and many results
# Player = can play multiple games, and many results
# Results = each result belongs to a single player and a game
# Game - Player is a "many to many" relationship



class Game:
    def __init__(self, title):
        self.title = title

    def print_title(self, title):
        if not isinstance(title, str) and (title > 0):
            return title

    def results(self):
        pass

    def players(self):
        pass

    def average_score(self, player):
        pass

class Player:
    def __init__(self, username):
        self.username = username

    def results(self):
        pass

    def games_played(self):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score