from flask import request, jsonify
from app import app, db
from models import Game


# Create a new game
@app.route('/games', methods=['POST'])
def add_game():
    data = request.json
    if not all(key in data for key in ['title', 'year', 'platform', 'status']):
        return jsonify({"error": "Missing required fields"}), 400

    new_game = Game(
        title=data['title'],
        year=data['year'],
        platform=data['platform'],
        status=data['status']
    )

    db.session.add(new_game)
    db.session.commit()

    return jsonify({"message": "Game added successfully", "game": new_game.to_dict()}), 201


# Get all games
@app.route('/games', methods=['GET'])
def get_games():
    games = Game.query.all()
    return jsonify([game.to_dict() for game in games])


# Get a specific game by ID
@app.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404
    return jsonify(game.to_dict())


# Update a game status
@app.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404

    data = request.json
    if 'status' in data:
        game.status = data['status']

    db.session.commit()
    return jsonify({"message": "Game updated successfully", "game": game.to_dict()})


# Delete a game
@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404

    db.session.delete(game)
    db.session.commit()

    return jsonify({"message": "Game deleted successfully"})
