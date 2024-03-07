class Game:
    def __init__(self, title):
        self._title = title
        self._players = []
        self._results = []

    @property
    def title(self):
        return self._title

    def add_player(self, player):
        if isinstance(player, Player) and player not in self._players:
            self._players.append(player)

    def add_result(self, result):
        if isinstance(result, Result) and result not in self._results:
            self._results.append(result)

    def results(self):
        return self._results

    def players(self):
        return self._players

    def average_score(self, player):
        player_results = [result.score for result in self._results if result.player == player]
        if player_results:
            return sum(player_results) / len(player_results)
        else:
            return None


class Player:
    def __init__(self, username):
        self._username = username
        self._results = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username

    def add_result(self, result):
        if isinstance(result, Result):
            self._results.append(result)

    def results(self):
        return self._results

    def games_played(self):
        return list(set([result.game for result in self._results]))

    def played_game(self, game):
        return any(result.game == game for result in self._results)

    def num_times_played(self, game):
        return sum(result.game == game for result in self._results)


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score