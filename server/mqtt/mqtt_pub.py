# python 3.8

import time

from paho.mqtt import client as mqtt_client

# 订阅主题
def publish(client,topic,msg):
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

# 断开连接
def disconnect(client: mqtt_client):
    client.loop_stop()
    client.disconnect()
