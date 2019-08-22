from typing import Optional, List, Tuple, Dict
from flask import Flask, jsonify, request, abort, Response
from game import Game

app = Flask(__name__)
app.config.from_pyfile("flaskconfig.py")

game_cnt = 0
games: Dict[str,Game] = {}

def create_new_game() -> Tuple[str, Game]:
    global game_cnt
    global games
    game_id = str(game_cnt)
    games[game_id] = Game()
    game_cnt += 1
    return (game_id), games[game_id]

def missing_json_fields(field_names:List[str]) -> Response:
    return abort(Response(f'Json is missing required fields: {field_names}'))

def missing_json_field(field_name:str)-> Response:
    return abort(Response(f'Missing field: "{field_name}", required in json request'))

def missing_json_data() -> Response:
    return abort(Response("No JSON-data supplied"))

@app.route("/")
def root():
    return jsonify(dict(
        dice=[1,2,3,4,5],
        msg = "This is just a test route, to check for working connection."
        )
    )

@app.route("/error_test")
def error_test():
    return str(app.config)

@app.route("/game", methods=["GET", "POST"])
def new_game():
    if request.json is None:
        return missing_json_data()

    if "player_names" not in request.json:
        return missing_json_field("player_names")

    game_id, game = create_new_game()
    game.add_players(request.json["player_names"])
    game.start_game()
    
    return jsonify(
        game_id=game_id,
        players=game.to_dict(),
    )

@app.route("/game/<game_id>/start", methods=["GET"])
def start_game(game_id: str):
    global games
    game = games[game_id] 
    return jsonify(
            current_player= game.current_player_name if game.is_started else game.start_game()
        )

@app.route("/game/<game_id>", methods=["GET"])
@app.route("/game/<game_id>/scores", methods=["GET"])
def game(game_id:str):
    global games
    if game_id not in games.keys():
        return (
            jsonify(dict(
                error=f'No game available with id {game_id}'
            )), 
            404
        )
    return jsonify(games[game_id].to_dict())

@app.route("/game/<game_id>/<player_name>", methods=["GET"])
def player(game_id:str, player_name:str):
    global games
    return jsonify(games[game_id].player_scores(player_name))

@app.route("/game/<game_id>/<player_name>/combinations", methods=["GET", "POST"])
def combinations(game_id:str, player_name:str):
    global games
    request_data = request.json
    if request_data is None:
        return missing_json_data()

    if "dice" not in request_data:
        return missing_json_field("dice")

    dice = request_data["dice"]
    game = games[game_id]
    return jsonify(
        combinations = game.possible_actions(dice, player_name)
    )

@app.route("/game/<game_id>/<player_name>/make_decision", methods=["POST"])
def make_decision(game_id: str, player_name:str):
    global games
    game = games[game_id]
    
    if not game.is_started:
        game.start_game()
    
    if game.current_player_name != player_name:
        return abort(401)

    request_data = request.json
    if request_data is None:
        return missing_json_data()
    if "dice" not in request_data:
        return missing_json_field("dice")
    if "decision" not in request_data:
        return missing_json_field("decision")

    if not game.make_decision(request_data["dice"], player_name, request_data["decision"]) :
        return abort(Response(f'Failed to make decision\nInput data:\n{request_data}\nPossible actions:\n{game.possible_actions(request_data["dice"],player_name)}'))

    return jsonify(
        scores = game.all_player_scores(),
        next_player=game.next_player(),
    )


if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"])