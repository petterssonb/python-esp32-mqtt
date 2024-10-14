from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import json
import ssl
import os

app = Flask(__name__)

broker_ip = os.getenv('BROKER_IP')
broker_port = int(os.getenv('BROKER_PORT'))
mqtt_topic = os.getenv('MQTT_TOPIC')

client = mqtt.Client()

client.connect(broker_ip, broker_port, 60)

@app.route('/sensor', methods=['POST'])
def handle_sensor_data():
    data = request.json
    print(f"Received data: {data}")

    client.publish(mqtt_topic, json.dumps(data))
    return jsonify({"status": "Data received and published to MQTT"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)