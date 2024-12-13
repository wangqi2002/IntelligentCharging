# python3.8

import random

from paho.mqtt import client as mqtt_client

# 发布消息
def subscribe(client: mqtt_client,topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message
    return

# 取消订阅
def unsubscribe(client: mqtt_client,topic):
    client.on_message = None
    client.unsubscribe(topic)