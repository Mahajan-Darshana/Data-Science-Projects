import json
import pickle
import numpy as np

# Global variables
__locations = None
__data_columns = None
__model = None
__scaler = None  # Add scaler variable

def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())  # Find location index
    except ValueError:
        loc_index = -1  # If location is not found, set -1

    x = np.zeros(len(__data_columns))  # Initialize with zeros
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:  # Check if location exists
        x[loc_index] = 1  # Apply one-hot encoding

    # Standardize input using the scaler
    if __scaler:
        x_scaled = __scaler.transform([x])  # Standardize the input
    else:
        x_scaled = [x]  # If no scaler, use raw values

    return round(__model.predict(x_scaled)[0], 2)  # Predict and round price

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    global __scaler  # Load scaler globally

    # Load column names
    with open(r"C:\Users\darsh\OneDrive\Desktop\BengluruProject\Server\artifacts\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    # Load the trained model
    with open(r"C:\Users\darsh\OneDrive\Desktop\BengluruProject\Server\artifacts\banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    # Load the scaler (if used during training)
    try:
        with open(r"C:\Users\darsh\OneDrive\Desktop\BengluruProject\Server\artifacts\scaler.pickle", "rb") as f:
            __scaler = pickle.load(f)
    except FileNotFoundError:
        print("Warning: Scaler not found, proceeding without standardization.")
        __scaler = None  # Explicitly setting None to avoid errors

    print("Done loading artifacts")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())  # Print available locations
    print(predict_price('1st Phase JP Nagar', 1000, 2, 2))  # Predict price for 1st Phase JP Nagar
    print(predict_price('1st Phase JP Nagar', 1000, 3, 3))  # Predict price for 1st Phase JP Nagar
    print(predict_price('Ejipura', 1000, 2, 2))  # Predict price for Ejipura
