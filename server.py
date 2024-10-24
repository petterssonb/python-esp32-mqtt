from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import json
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

broker_ip = os.getenv('BROKER_IP')
broker_port = int(os.getenv('BROKER_PORT'))
mqtt_topic = os.getenv('MQTT_TOPIC')

client = mqtt.Client()

client.connect(broker_ip, broker_port, keepalive=120)

@app.route('/sensor', methods=['POST'])
def handle_sensor_data():
    data = request.json
    print(f"Received data: {data}")

    client.publish(mqtt_topic, json.dumps(data))
    return jsonify({"status": "Data received and published to MQTT"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, ssl_context=('cert.pem', 'key.pem'))