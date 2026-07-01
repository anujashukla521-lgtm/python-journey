class Team:
    def __init__(self,team_name,no_of_players):
        self.team_name = team_name
        self.no_of_players = no_of_players

    def __str__(self):
        return f"Team name: {self.team_name} No of players: {self.no_of_players}"

team = Team("RCB",12)
print(team)