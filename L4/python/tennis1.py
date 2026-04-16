class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            tie_scores = ("Love-All", "Fifteen-All", "Thirty-All")
            if self.p1points < 3:
                return tie_scores[self.p1points]
            return "Deuce"

        if self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                return f"Advantage {self.player1_name}"
            if minus_result == -1:
                return f"Advantage {self.player2_name}"
            if minus_result >= 2:
                return f"Win for {self.player1_name}"
            return f"Win for {self.player2_name}"

        point_names = ("Love", "Fifteen", "Thirty", "Forty")
        return f"{point_names[self.p1points]}-{point_names[self.p2points]}"
