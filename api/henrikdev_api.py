
class HenriApi():

    def __init__(self):
        pass

    def get_general_account_data(self, username, tagline):
        # https://api.henrikdev.xyz/valorant/v1/account/AverageTea/1111
        pass

    def get_mmr_data(self, version, username, tagline):
        # https://api.henrikdev.xyz/valorant/v1/mmr/eu/AverageTea/1111
        pass

    def get_match_history(self, username, tagline, filter="competitive"):
        # Returns 5 Latest Matches
        # https://api.henrikdev.xyz/valorant/v3/matches/eu/AverageTea/1111?filter=competitive
        pass

    def get_match_data(self, match_id):
        # Returns full details of match (who killed who, where, how, how much damage, etc)
        # https://api.henrikdev.xyz/valorant/v2/match/b46c2c50-3271-441d-9cc6-963f200a18a6
        pass
