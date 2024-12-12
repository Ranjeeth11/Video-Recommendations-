from flask import Blueprint, request, jsonify
from ..recommender import recommend_posts

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    username = data.get('username')
    category_id = data.get('category_id')
    mood = data.get('mood')

    # Call the recommender logic
    recommendations = recommend_posts(username, category_id, mood)
    return jsonify(recommendations)
