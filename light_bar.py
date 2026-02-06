from wsgiref import headers
import requests
import os
import board
import neopixel
import time
import datetime

pixels = neopixel.NeoPixel(
    board.D18,
     30,
     brightness=1.0,
     auto_write=False
)

URL = "192.168.4.206"
KEY = os.getenv("KEY")
while True: #runs everything in a loop
    def task_light(): #sets second 1/2 of lights to white
        for i in range(15,30):
            pixels[i] = (255,255,255)
            pixels.show()


    r = requests.get(f"http://{URL}/api/job", headers={"X-Api-Key": KEY})
    r.raise_for_status()

    progress = r.json()["progress"]["completion"]
    state = r.json()["state"]

    if progress is None:
        progress = 0
    else:
        progress = int(progress)
        progress = 30 / progress 
        progress =progress *100
        progress = int((progress / 100) *30)

    if state == "Operational":
        task_light()
        for i in range(15):
            pixels[i] = (0,200,0)
            pixels.show()   
            time.sleep(0.05)#adjust to change chasing speed
    if state == "Printing":
        task_light()
        for i in range(progress):
            pixels[i] = (0,200,0)
            pixels.show() 
    if state == "Error":
        task_light()
        for i in range(15):
            pixels[i] = (255,0,0)
            pixels.show()   
            time.sleep(0.5)
            pixels[i] = (0,0,0)
            pixels.show()
            time.sleep(0.5)  
    else:
        for i in range(30):
            pixels[i] = (0,0,0)
            pixels.show()

    #turns off lights at night
    time = datetime.datetime.now().time()
    if time.hour >= 22 or time.hour <= 7:
        for i in range(30):
            pixels[i] = (0,0,0)
            pixels.show()
    print(state)
    data = r.json()
    print(data)
    time.sleep(60) #checks every minute