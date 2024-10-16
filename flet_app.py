import flet as ft
import paho.mqtt.client as mqtt
import json
import os
from dotenv import load_dotenv
import time

load_dotenv()

BROKER_IP = os.getenv("BROKER_IP")
BROKER_PORT = int(os.getenv("BROKER_PORT"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    data = json.loads(payload)
    
    page = userdata["page"]
    data_display = userdata["data_display"]
    
    data_display.value = "Loading new measurement..."
    data_display.color = ft.colors.GREY
    page.update()
    
    time.sleep(0.5)
    
    data_display.value = f"Received Data: {json.dumps(data, indent=2)}"
    data_display.color = ft.colors.BLACK
    
    data_display.opacity = 1
    data_display.update()

mqtt_client = mqtt.Client()

def connect_mqtt(page, data_display):
    mqtt_client.user_data_set({"page": page, "data_display": data_display})
    mqtt_client.on_message = on_message
    mqtt_client.connect(BROKER_IP, BROKER_PORT, 60)
    mqtt_client.subscribe(MQTT_TOPIC)
    mqtt_client.loop_start()

def main(page: ft.Page):
    page.title = "MQTT Sensor Data Dashboard"
    
    data_display = ft.Text(
        "Waiting for sensor data...", 
        size=18, 
        selectable=True, 
        color=ft.colors.BLACK, 
        opacity=1,
        animate_opacity=500
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Sensor Data", size=30, weight="bold"),
                ft.Card(
                    content=ft.Container(
                        content=data_display,
                        padding=10,
                        border_radius=5,
                        bgcolor=ft.colors.LIGHT_BLUE_100,
                        width=400,
                        height=200,
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    connect_mqtt(page, data_display)

ft.app(target=main, view=ft.WebView)