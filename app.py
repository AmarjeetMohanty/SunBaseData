from flask import Flask, request, jsonify
import pickle  # For loading the trained MLP model
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained MLP model and scaler
with open('mlp_model.pkl', 'rb') as model_file:
    mlp_model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def index():
    return "Welcome to the Customer Churn Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()
        features = data['features']

        # Preprocess the input data (assuming the same preprocessing used during training)
        scaled_features = scaler.transform([features])

        # Make predictions using the trained model
        prediction = mlp_model.predict(scaled_features)

        # Return the prediction as JSON response
        response = {'prediction': int(prediction[0])}
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
