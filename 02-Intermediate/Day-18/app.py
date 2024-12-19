from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import requests
import pandas as pd

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('request_data')
def handle_request_data():
    data = fetch_real_time_data()
    emit('update_data', data)

def fetch_real_time_data():
    response = requests.get('https://www.data.gov.in/catalog/resource/579b464db66ec23bdd000001af9ab0c2e1754fe67f8fed62ed70928e')
    
    # Print the raw response content for debugging
    print(response.text)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return []

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []

    if 'records' not in data:
        print("Error: 'records' key not found in JSON response")
        return []

    df = pd.DataFrame(data['records'])
    # Process your data as needed
    return df.to_dict(orient='records')


if __name__ == '__main__':
    socketio.run(app, debug=True)
