from typing import List, Callable, Optional
from functools import wraps
from player import Player
from scoresection import UpperSectionScore, LowerSectionScore


class Game:
    def __init__(self, player_names: List[str], bonus_calc_rule:Callable[[int], Optional[int]]):
        self._players: List[Player] = []
        self.current_player: Optional[Player] = None
        for name in player_names:
            self._players.append(Player(name, UpperSectionScore(bonus_calc_rule), LowerSectionScore()))

    def player_loop(self):
        """
            Returns a generator which returns the name of the next player 
            until all players are finished.
            Also sets self.current_player to the current player.
        """
        def loop(player_list):
            saved = []
            for player in player_list:
                self.current_player = player
                yield player
                saved.append(player)
            while saved:
                for player in saved:
                    self.current_player = player
                    yield player
                    if player.is_finished():
                        saved.remove(player)
        return loop(self._players)
