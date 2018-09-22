import paho.mqtt.client as mqtt
def on_publish(mosq, userdata, mid):
    mosq.disconnect()
client = mqtt.Client()
client.connect("10.200.200.100", 1883)
client.on_publish = on_publish
f=open("b.png", "rb")
fileContent = f.read()
byteArr = bytearray(fileContent)
client.publish("image",byteArr,0)
client.loop_forever()