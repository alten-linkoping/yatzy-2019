from typing import Optional, List, Tuple, Dict
from flask import Flask, jsonify, request, abort
from game import Game

app = Flask(__name__)

game_cnt = 0
games: Dict[int,Game] = {}

def create_new_game(player_names: Optional[List[str]]=None) -> Tuple[int, Game]:
    global game_cnt
    global games
    game_id = game_cnt
    games[game_id] = Game(lambda score: 50 if score >= 63 else None)
    game_cnt += 1
    return game_id, games[game_id]

@app.route("/")
def root():
    return jsonify(dict(
        dice=[1,2,3,4,5],
        msg = "This is just a test route, to check for working connection."
        )
    )

@app.route("/game", methods=["GET", "POST"])
def new_game():
    game_id, game = create_new_game()
    if request.json is not None and "player_names" in request.json:
        game.add_players(request.json["player_names"])
    return jsonify(
        game_id=game_id,
        players=game.to_dict(),
    )

@app.route("/game/<game_id>", methods=["GET"])
@app.route("/game/<game_id>/scores", methods=["GET"])
def game(game_id:str):
    global games
    _game_id = int(game_id)
    if _game_id not in games.keys():
        return (
            jsonify(dict(
                error=f'No game available with id {game_id}'
            )), 
            404
        )
    return jsonify(games[_game_id].to_dict())

@app.route("/game/<game_id>/<player_name>", methods=["GET"])
def player(game_id:str, player_name:str):
    global games
    return jsonify(games[int(game_id)].player_scores(player_name))

@app.route("/game/<game_id>/<player_name>/unused_fields", methods=["GET"])
def get_unused_fields(game_id:str, player_name:str):
    global games
    return jsonify(
        unused_fields = games[int(game_id)].get_unused_fields(player_name)
    )