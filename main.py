# import RPi.GPIO as GPIO
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
from datetime import datetime
# from picamera import PiCamera
from time import sleep
import os

import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyC-BUMN0WB14YUuebX-97Jv_oNCVn3__D4",
    "authDomain": "rpi-images-a1244.firebaseapp.com",
    "databaseURL": "https://rpi-images-a1244-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "rpi-images-a1244",
    "storageBucket": "rpi-images-a1244.appspot.com",
    "messagingSenderId": "994685609465",
    "appId": "1:994685609465:web:9250687bff32c971780928",
    "measurementId": "${config.measurementId}"
}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()
storage = firebase.storage()

# camera = PiCamera()

# while True:
#     try:
#         if GPIO.input(10) == GPIO.HIGH:
#             print("pushed")
#             now = datetime.now()
#             dt = now.strftime("%d%m%Y%H:%M:%S")
#             name = dt+".jpg"
#             camera.capture(name)
#             print(name+" saved")
#             storage.child(name).put(name)
#             print("Image sent")
#             os.remove(name)
#             print("File Removed")
#             sleep(2)
#
#
#     except:
#         camera.close()
if __name__ == '__main__':
    now = datetime.now()
    dt = now.strftime("%d%m%Y%H:%M:%S")
    name = "test.jpg"
    previous = database.child('images').get()
    previous = previous.each()[0]
    previous = previous.val()['name']

    storage.delete(previous,'')
    storage.child(dt + '.jpg').put(name)
    url = storage.child(dt + '.jpg').get_url('')
    print(url)
    database.child('images').remove()
    database.child('images').child(dt).set({'name': dt + '.jpg', 'path': url})
