class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def score(self):
        if (self.player1_score < 4 and self.player2_score < 4) and (self.player1_score + self.player2_score < 6):
            points = ["Love", "Fifteen", "Thirty", "Forty"]
            player1_score = points[self.player1_score]
            return player1_score + "-All" if (self.player1_score == self.player2_score) else player1_score + "-" + points[self.player2_score]

        if self.player1_score == self.player2_score:
            return "Deuce"

        leading_player = self.player1_name if self.player1_score > self.player2_score else self.player2_name

        if abs(self.player1_score - self.player2_score) == 1:
            return f"Advantage {leading_player}"
        else:
            return f"Win for {leading_player}"
