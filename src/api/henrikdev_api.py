########################################################################################################
########################################################################################################
# API Created by HENRIKDEV - https://docs.henrikdev.xyz/valorant.html
#
#
#
########################################################################################################
########################################################################################################
import requests
import asyncio
import aiohttp


class HenrikApi():

    def __init__(self):
        self.api_link = "https://api.henrikdev.xyz/valorant/"

    def account_validate(self, username, tagline):
        try:
            self.response = requests.get(
                self.api_link + f"v1/account/{username}/{tagline}")
            if self.response.ok:
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def get_general_account_data(self, username, tagline):
        # https://api.henrikdev.xyz/valorant/v1/account/AverageTea/1111
        try:
            self.response = requests.get(
                self.api_link + f"v1/account/{username}/{tagline}")
            if self.response.ok:
                return self.response.json()
            else:
                return self.response.status_code
        except Exception as e:
            print(e)

    def get_elo_data(self, version, region, username, tagline):
        # https://api.henrikdev.xyz/valorant/v1/mmr/eu/AverageTea/1111
        try:
            self.response = requests.get(
                self.api_link + f"{version}/mmr/{region}/{username}/{tagline}")
            if self.response.ok:
                return self.response.json()
            else:
                return self.response.status_code
        except Exception as e:
            print(e)

    def get_match_history(self, username, tagline, filter="competitive"):
        # Returns 5 Latest Matches
        # https://api.henrikdev.xyz/valorant/v3/matches/eu/AverageTea/1111?filter=competitive
        pass

    def get_match_data(self, match_id):
        # Returns full details of match (who killed who, where, how, how much damage, etc)
        # https://api.henrikdev.xyz/valorant/v2/match/b46c2c50-3271-441d-9cc6-963f200a18a6
        pass
