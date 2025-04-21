import requests
import json

SERVER_URL = 'http://127.0.0.1:5000/submit'

def send_data(device_id, message):
    payload = {
        "device_id": device_id,
        "message": message
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(SERVER_URL, data=json.dumps(payload), headers=headers)
    print(response.json())

# Example of a normal message
send_data("sensor001", "Temperature is 25°C")

# Example of a spoofed client performing SQL injection attempt
send_data("attacker_device", "'); DROP TABLE sensor_logs; --")
