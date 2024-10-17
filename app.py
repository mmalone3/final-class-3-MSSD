# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

activity_history = []

@app.route('/track', methods=['POST'])
def track_activity():
    data = request.json
    activity = data.get('activity')
    color = data.get('color')
    
    if activity:
        session = {
            'name': activity,
            'startTime': 'Mocked Start Time',
            'endTime': None
        }
        activity_history.append(session)
        return jsonify({'message': 'Tracking started', 'activity': session}), 200
    return jsonify({'error': 'Activity not provided'}), 400

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(activity_history), 200

if __name__ == '__main__':
    app.run(debug=True)