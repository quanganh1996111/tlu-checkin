import picamera
import base64
import mqtt
from time import sleep

def convertImageToBase64():
	with open("image_test.jpg", "rb") as image_file:
		encoded = base64.b64encode(image_file.read())
		return encoded

camera = picamera.PiCamera()

try: 
 camera.start_preview()
 sleep(1)
 camera.capture('image_test.jpg', resize=(500,281))
 camera.stop_preview()
 pass
finally:
 camera.close()