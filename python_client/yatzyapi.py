from typing import List, Optional, Dict, Any
import requests
import json

class YatzyApi:
    def __init__(self, base_url:str):
        self.base_url = base_url

    def new_game(self, player_names: List[str]) -> Optional[Dict[str, Any]]:
        respons = requests.get(
            f'{self.base_url}/game',
            json={
                "player_names":player_names,
                }
        )
        game_data = respons.json()
        return game_data

    def start_game(self, game_id:int) -> Optional[str]:
        respons = requests.get(
            f'{self.base_url}/game/{game_id}/start'
        )
        respons_json = respons.json() 
        if respons_json is not None and "current_player" in respons_json:
            return respons_json["current_player"] 
        else:
            return None

    
    def get_options(self, game_id:int, player_name:str, dice:List[int]) -> Dict[str, int]:
        respons = requests.get(
            f'{self.base_url}/game/{game_id}/{player_name}/combinations',
            json={
                "dice":dice,
            },
        )
        return respons.json()["combinations"]

    def submit_decision(self, game_id:int, player_name:str, dice:List[int], decision:str):
        respons = requests.post(
            f'{self.base_url}/game/{game_id}/{player_name}/make_decision',
            json={
                "dice":dice,
                "decision":decision
            },
        )
        respons_json = respons.json()
        return respons_json["next_player"], respons_json["scores"]