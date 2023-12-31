# Program: subscribe.py
# Author:  Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Purpose: Used to demonstrate how to subscribe to an MQTT topic
#          using the Paho MQTT Client in Python

import time
import paho.mqtt.client as paho

MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "test"


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    topic = msg.topic
    print(f"Received ({topic}): {message}")


client = paho.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC)

client.loop_forever()
