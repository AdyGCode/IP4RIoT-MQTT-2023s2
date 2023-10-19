# Program: Publisher
# Author:  Adrian Gould <Adrian.Gould@nmtafe.wa.edu.au>
# Purpose: Used to demonstrate how to publish to an MQTT topic
#          using the Paho MQTT Client in Python

import time
import paho.mqtt.client as paho

MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "test"

listening_client = paho.Client()
listening_client.connect(MQTT_BROKER, MQTT_PORT)

listening_client.publish(MQTT_TOPIC, "This is a message")
listening_client.publish("demo", "This is another message in a different topic")
