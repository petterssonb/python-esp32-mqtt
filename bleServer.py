import asyncio
from bleak import BleakClient, BleakScanner
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CHARACTERISTIC_UUID = os.getenv("CHARACTERISTIC_UUID")
SERVICE_UUID = os.getenv("SERVICE_UUID")
cert_path = os.path.join(os.path.dirname(__file__), "cert.pem")

if not CHARACTERISTIC_UUID or not SERVICE_UUID:
    raise ValueError("Please define CHARACTERISTIC_UUID and SERVICE_UUID in the .env file")

def notification_handler(sender, data):
    json_data = data.decode('utf-8')
    print(f"Received data from ESP32: {json_data}")

    url = os.getenv("FLASK_URL")
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, data=json_data, headers=headers, verify=cert_path)
        print(f"Flask server response: {response.json()}")
    except Exception as e:
        print(f"Failed to send data to Flask server: {e}")

async def main():
    devices = await BleakScanner.discover()
    esp32_address = None

    for device in devices:
        if device.name and "ESP32_Sensor" in device.name:
            esp32_address = device.address
            break

    if not esp32_address:
        print("ESP32 not found")
        return

    async with BleakClient(esp32_address, timeout=30.0) as client:
        print("Connected to ESP32")

        services = await client.get_services()
        print("Services and Characteristics:")
        for service in services:
            print(f"Service: {service.uuid}")
            for characteristic in service.characteristics:
                print(f"  Characteristic: {characteristic.uuid}, Properties: {characteristic.properties}")

        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())