import paho.mqtt.client as mqtt
import base64
import math
import random, string
import requests
from time import sleep
def convertImageToBase64():
 with open("b.png", "rb") as image_file:
     encoded = base64.b64encode(image_file.read())
     return encoded
packet_size=3000
rpi = mqtt.Client("p1")
rpi.connect("10.200.200.100", 1883)
def on_connect(rpi, obj, flags, rc):
    print("rc: " + str(rc))
    rpi.subscribe("image/json")
def on_message(rpi, obj, msg):
    print("Messages arrived:" + str(msg.payload))
    js=json.loads(str(msg.payload))
    with open('data.json', 'w') as outfile:
        json.dump(js, outfile, sort_keys = True, indent=4, separators= (',', ':'  ))
rpi.on_connect = on_connect
rpi.on_message = on_message
rpi.publish("json")

def publishEncodedImage(encoded):
 end = packet_size
 start = 0
 length = len(encoded)
 picId = randomword(8)
 pos = 0
 no_of_packets = math.ceil(length/packet_size)
 while start <= len(encoded):
     data = {"data": encoded[start:end], "pic_id":picId, "pos": pos, "size": no_of_packets}
     client.publishEvent("Image-Data",json.JSONEncoder().encode(data))
     end += packet_size
     start += packet_size
     pos = pos +1
def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))
