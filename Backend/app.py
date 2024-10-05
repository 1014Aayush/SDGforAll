from flask import Flask, jsonify
from flask_cors import CORS  # <-- Import CORS

app = Flask(__name__)
CORS(app)  # <-- Enable CORS for all routes

# Data for Sustainable Development Goals
sdg_data = [
    {"id": 1, "title": "No Poverty", "description": "End poverty in all its forms everywhere."},
    {"id": 2, "title": "Zero Hunger", "description": "End hunger, achieve food security and improved nutrition."},
    {"id": 3, "title": "Good Health and Well-being", "description": "Ensure healthy lives and promote well-being for all."},
    # Add remaining 17 SDGs here
]

@app.route('/sdgs', methods=['GET'])
def get_sdgs():
    return jsonify(sdg_data)

if __name__ == '__main__':
    app.run(debug=True)
