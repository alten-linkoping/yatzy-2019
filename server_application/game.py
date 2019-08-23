from typing import List, Callable, Optional, Dict, Any, Iterable
from functools import wraps
from collections import OrderedDict
from player import Player
from scoresection import UpperSectionScore, LowerSectionScore


class Game:
    def __init__(self):
        self._is_started = False
        self._is_finished = False
        self._players: Dict[str, Player] = OrderedDict()
        self.current_player_name: Optional[str] = None
        self._player_order: Optional[Iterable[str]] = None

    def __repr__(self):
        return f'started: {self.is_started}\nfinished: {self.is_finished}\nplayer_names: {self.player_names}'

    def add_players(self, names:List[str]):
        for name in names:
            self.add_player(name)

    def add_player(self, name:str):
        self._players[name] = Player(name)

    def to_dict(self) -> Dict[str, Any]:
        return OrderedDict(
            player_names=self.player_names,
            scores=self.all_player_scores(),
        )

    def possible_actions(self, dice:List[int], player_name:str) -> Dict[str, int]:
        return self._players[player_name].possible_actions(dice)

    def all_player_scores(self) -> List[Dict[str,Optional[int]]]:
        return [p.to_dict() for p in self._players.values()]

    def get_unused_fields(self, player_name:str) -> List[str]:
        return self._players[player_name].unused_fields

    def player_scores(self, player_name:str) -> Optional[Dict[str, Any]]:
        player = next((p for p in self._players.values() if p.name == player_name), None)
        return player.to_dict() if player is not None else None

    def start_game(self):
        self._is_started = True
        self._player_order = self._create_player_order_generator()
        self.current_player_name = next(self._player_order)
        return self.current_player_name

    def winner_name(self) -> Optional[str]:
        winner:Optional[Player] = None
        max_score = 0
        for player in self._players.values():
            if player.total_score() > max_score:
                winner = player

        return winner.name if winner is not None else None

    def make_decision(self, dice:List[int], player_name:str, decision:str) -> bool:
        actions = self.possible_actions(dice, player_name)
        if decision not in actions.keys():
            print(f'Decision: {decision}')
            print("actions:")
            print(actions)
            return False
        action = actions[decision]
        self._players[player_name].set_field(decision, action if action!=0 else "-")
        return True


    def next_player(self) -> Optional[str]:
        if self._player_order is None:
            return self.start_game()
        else:
            for player_name in self._player_order:
                self.current_player_name = player_name
                return  player_name
        return None


    @property
    def player_names(self) -> List[str]:
        return [name for name in self._players.keys()]

    @property
    def is_started(self) -> bool:
        return self._is_started
    
    @property
    def is_finished(self)-> bool:
        return self._is_finished


    def _create_player_order_generator(self) -> Iterable[str]:
        """
            Returns a generator which returns the name of the next player 
            until all players are finished.
            Also sets self.current_player_name to the current player.
        """
        def loop(player_names: Iterable[str]) -> Iterable[str]:
            saved: List[str] = []
            for player_name in player_names:
                yield player_name
                saved.append(player_name)
            while saved:
                for player_name in saved:
                    yield player_name
                    if self._players[player_name].is_finished():
                        saved.remove(player_name)
            self._is_finished = True
        return loop(self._players.keys())
