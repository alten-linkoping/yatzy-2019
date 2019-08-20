from typing import List, Callable, Optional, Dict, Any, Iterable
from functools import wraps
from collections import OrderedDict
from player import Player
from scoresection import UpperSectionScore, LowerSectionScore


class Game:
    def __init__(self,bonus_calc_rule:Callable[[int], Optional[int]]):
        self._is_started = False
        self._is_finished = False
        self._players: OrderedDict[str, Player] = OrderedDict()
        self.current_player_name: Optional[str] = None
        self.bonus_calc_rule = bonus_calc_rule

    def __repr__(self):
        return f'started: {self.is_started}\nfinished: {self.is_finished}\nplayer_names: {self.player_names}'

    def add_players(self, names:List[str]):
        for name in names:
            self.add_player(name)

    def add_player(self, name:str):
        self._players[name] = Player(name, UpperSectionScore(self.bonus_calc_rule), LowerSectionScore())

    def to_dict(self) -> Dict[str, Any]:
        return dict(
            player_names=self.player_names,
            scores=[p.to_dict() for p in self._players.values()],
        )

    def get_unused_fields(self, player_name:str) -> List[str]:
        return self._players[player_name].unused_fields

    def player_scores(self, player_name:str) -> Optional[Dict[str, Any]]:
        player = next((p for p in self._players.values() if p.name == player_name), None)
        return player.to_dict() if player is not None else None

    @property
    def player_names(self) -> List[str]:
        return [name for name in self._players.keys()]

    @property
    def is_started(self) -> bool:
        return self._is_started
    
    @property
    def is_finished(self)-> bool:
        return self._is_finished


    def player_loop(self) -> Iterable[str]:
        """
            Returns a generator which returns the name of the next player 
            until all players are finished.
            Also sets self.current_player_name to the current player.
        """
        def loop(player_names: Iterable[str]) -> Iterable[str]:
            saved: List[str] = []
            self._is_started = True
            for player_name in player_names:
                self.current_player_name = player_name
                yield player_name
                saved.append(player_name)
            while saved:
                for player_name in saved:
                    self.current_player_name = player_name
                    yield player_name
                    if self._players[player_name].is_finished():
                        saved.remove(player_name)
            self._is_finished = True
        return loop(self._players.keys())
