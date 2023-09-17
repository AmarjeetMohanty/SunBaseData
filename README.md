
# Customer Churn Prediction Flask App

This Flask application is designed to predict customer churn based on historical customer data using a pre-trained MLP (Multi-Layer Perceptron) model.

## Getting Started

These instructions will help you set up and run the Flask app on your local machine for testing and development purposes.

### Prerequisites

- Python 3.7 or higher
- Flask
- scikit-learn
- pickle (for model serialization)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/customer-churn-flask-app.git
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Ensure that you have saved your trained MLP model as `mlp_model.pkl` and your scaler as `scaler.pkl` in the same directory as `app.py`. Follow the model training and serialization steps in your project documentation.

2. Navigate to the directory containing `app.py` in your terminal.

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. The app will start and be accessible locally at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Making Predictions

You can make predictions by sending POST requests to the `/predict` endpoint. You can use tools like `curl`, Postman, or Python's `requests` library to send requests. Here's an example using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"features": [25, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0]}' http://127.0.0.1:5000/predict
```

This `curl` command sends a JSON payload with features to the `/predict` endpoint, and the app will return a JSON response with the prediction.

### Sample Response

The app will return a JSON response with the prediction:

```json
{
  "prediction": 1
}
```

- `"prediction"`: 1 indicates churn, 0 indicates no churn.

### Note

This setup is intended for testing and development purposes. In a production environment, you would deploy the Flask app on a production server with proper security, scalability, and performance considerations.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

