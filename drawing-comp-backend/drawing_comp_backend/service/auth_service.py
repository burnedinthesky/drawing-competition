from datetime import timezone, datetime

class AuthService:
    def __init__(self, logger, team):
        self.logger = logger
        self.team = team
    def create_team(self, token):
        team_token = self.team.create_team(token)
        return team_token
    def update_team(self, token, name):
        team_id = self.team.update_team(token, name)
        return team_id
    def query_team(self, team_token):
        team = self.team.query_team(team_token)
        return team
    def query_all_teams(self):
        teams = self.team.query_all_teams()
        return teams