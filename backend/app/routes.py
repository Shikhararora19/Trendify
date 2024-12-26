from flask import Blueprint, jsonify, request
from .utils import main  # Function to fetch trends

api_bp = Blueprint('api', __name__)

@api_bp.route('/trends', methods=['GET'])
def get_trends():
    try:
        location = request.args.get('location', 'US')  # Default location is 'US'
        trends_data = main(location)  # Pass the location to scrapers
        return jsonify(trends_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
