from flask import Blueprint, jsonify, request
from .utils import main  # Function to fetch trends
import openai
import re


api_bp = Blueprint('api', __name__)

PREDEFINED_CATEGORIES = ['Sports', 'Entertainment', 'Technology', 'Politics', 'Business']


@api_bp.route('/trends', methods=['GET'])
def get_trends():
    try:
        location = request.args.get('location', 'US')  # Default location is 'US'
        trends_data = main(location)  # Pass the location to scrapers
        return jsonify(trends_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@api_bp.route('/categorize', methods=['POST'])
def categorize_trends():
    try:
        data = request.json
        
        # Ensure the payload has the expected structure
        if not data or "trends" not in data:
            return jsonify({"error": "Invalid payload"}), 400

        trends = data["trends"]
        titles = [item["name"] for source in trends.values() for item in source if "name" in item]
        print("Titles for Categorization:", titles)

        # Call OpenAI API to categorize
        openai.api_key = "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"
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a data categorization assistant."},
                {"role": "user", "content": f"Categorize these titles into predefined categories: {titles}"}
            ]
        )

        # Extract and parse the response content
        gpt_response = response["choices"][0]["message"]["content"]
        print("Raw GPT Response:", gpt_response)

        # Initialize categories dictionary and a placeholder for the current category
        categories = {}
        current_category = None

        # Split the GPT response by lines for parsing
        for line in gpt_response.split("\n"):
    # Explicitly match `### Header` format
            if line.startswith("###"):
                current_category = line.replace("###", "").strip(":").strip()
                categories[current_category] = []  # Initialize the category list
            # Explicitly match `** Header:**` format
            elif line.startswith("**"):
                current_category = line.replace("**", "").strip(":").strip()
                categories[current_category] = []  # Initialize the category list
            # Handle list items (e.g., `- item` or `1. item`)
            elif current_category and (line.strip().startswith("- ") or re.match(r"^\d+\.\s", line)):
                item = re.sub(r"^(-\s*|\d+\.\s*)", "", line.strip())  # Remove leading `-` or `1. `
                item = item.strip("`'\"")  # Remove surrounding quotes or backticks
                categories[current_category].append(item)

        # Debugging output to verify parsing
        print("Parsed Categories:", categories)

        # Return the parsed categories as JSON
        return jsonify({"categories": categories}), 200

    except Exception as e:
        print("Error in /api/categorize:", str(e))
        return jsonify({"error": str(e)}), 500