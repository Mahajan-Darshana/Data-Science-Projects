from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

import util

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Load saved artifacts (model, scaler, and columns) before handling requests
util.load_saved_artifacts()


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()  # Fetch locations from util.py
    })
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()

    try:
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])
    except Exception as e:
        return jsonify({"error": "Invalid input data"}), 400

    predicted_price = util.predict_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': predicted_price
    })
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction")
    app.run(debug=True)
