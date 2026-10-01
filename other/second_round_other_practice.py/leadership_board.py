class Leaderboard:
    def __init__(self):
        self.players = {}
    

    def add_score(self, player_id, score):
        if score >= 0:
            self.players[player_id] = self.players.get(player_id, 0) + score
            return True
        return False
    
    def top(self, k):
        if k > len(self.players):
            return False
        total = 0
        scores = sorted(list(self.players.values()), reverse=True)

        for i in range(k):
            total += scores[i]

        return total
    
    def reset(self, player_id):
        if player_id in self.players:
            self.players[player_id] = 0
            return True
        return False





lb = Leaderboard()

lb.add_score(1, 73)
lb.add_score(2, 56)
lb.add_score(3, 39)
lb.add_score(4, 51)
lb.add_score(5, 4)

print(lb.top(1))  # expected 73
print(lb.top(3))  # expected 180 -> 73 + 56 + 51

lb.reset(1)
lb.reset(2)

print(lb.top(3))  # expected 94 -> 51 + 39 + 4

lb.add_score(2, 51)

print(lb.top(3))  # expected 141 -> 51 + 51 + 39


