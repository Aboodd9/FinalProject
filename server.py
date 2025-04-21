from flask import Flask, request, jsonify
from database import init_db, insert_insecure, insert_secure, view_logs
from utils import sanitize_input

app = Flask(__name__)
init_db()

# Choose whether to use secure or insecure insert method
USE_SECURE_MODE = True

@app.route('/submit', methods=['POST'])
def handle_message():
    data = request.get_json()
    device_id = data.get('device_id', '')
    message = data.get('message', '')

    if not sanitize_input(device_id) or not sanitize_input(message):
        return jsonify({'status': 'error', 'message': 'Input contains invalid characters'}), 400

    if USE_SECURE_MODE:
        insert_secure(device_id, message)
    else:
        insert_insecure(device_id, message)

    return jsonify({'status': 'success', 'message': 'Data stored successfully'})

@app.route('/logs', methods=['GET'])
def show_logs():
    logs = view_logs()
    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(debug=True)
