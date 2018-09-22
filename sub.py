import paho.mqtt.client as mqtt
def on_connect(client, userdate, rc):
	print("Connect" + str(rc))
	client.subcribe("image")
def on_message(client, userdate, msg):
	print ("Topic : ", msg.topic)
	f = open("b.png", "w")
	f.write(msg.payload)
	f.close()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.200.200.101", 1883)
client.loop_forever()