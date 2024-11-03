from flask import Flask, request, jsonify
import joblib
import logging

# Initialize the Flask application
app = Flask(__name__)

# Load your trained model (ensure you have saved your model previously)
model_path = 'my_model.pkl'  # Update with your model path
try:
    model = joblib.load(model_path)
except Exception as e:
    logging.error(f"Error loading model: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Log the incoming data for debugging purposes
    app.logger.info(f"Incoming request data: {data}")

    # Extracting the text and language from the request
    text = data.get('Text')
    language = data.get('Language')

    # Check if text and language are provided
    if text and language:
        try:
            # Perform prediction (you may need to preprocess the text based on your model requirements)
            prediction = model.predict([text])  # Assuming your model takes text input
            return jsonify({'predicted_language': prediction[0]})  # Adjust based on your model's output
        except Exception as e:
            logging.error(f"Prediction error: {e}")
            return jsonify({'error': 'Prediction failed'}), 500
    else:
        return jsonify({'error': 'Invalid input: Text and Language are required'}), 400

if __name__ == '__main__':
    # Set logging level
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
