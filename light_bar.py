from wsgiref import headers
import requests
import os
import board
import neopixel
import time
import datetime

pixels = neopixel.NeoPixel(
    board.D18,
     20,
     brightness=1.0,
     auto_write=False
)

URL = "192.168.4.223"
KEY = os.getenv("KEY")
while True: #runs everything in a loop
    def task_light(): #sets second 1/2 of lights to white
        for i in range(10,20):
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
        progress = int((progress / 100) * 20)

    if state == "Operational":
        task_light()
        for i in range(10):
            pixels[i] = (0,200,0)
            pixels.show()   
            time.sleep(0.05)#adjust to change chasing speed
    if state == "Offline":
        task_light()
    elif state == "Printing":
        task_light()
        for i in range(progress):
            pixels[i] = (0,200,0)
            pixels.show() 
    elif state == "Error":
        task_light()
        for i in range(10):
            pixels[i] = (255,0,0)
            pixels.show()   
            time.sleep(0.5)
            pixels[i] = (0,0,0)
            pixels.show()
            time.sleep(0.5)  
    else:
        for i in range(20):
            pixels[i] = (0,0,0)
            pixels.show()

    #turns off lights at night
    current_time = datetime.datetime.now().time()
    if current_time.hour >= 22 or current_time.hour < 7:
        for i in range(20):
            pixels[i] = (0,0,0)
            pixels.show()
    print(state)
    data = r.json()
    print(data)
    time.sleep(60) #checks every minute