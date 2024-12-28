from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)
    return jsonify({'sentiment': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
